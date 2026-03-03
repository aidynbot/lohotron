from fastapi import FastAPI, Request, Form, BackgroundTasks
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from .mail_sender import send_gift_email

app = FastAPI()

# Подключаем статику (CSS/JS) и шаблоны (HTML)
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

# Список имен для проверки (белый список)
GIRLS_LIST = ["Аружан", "Мадина", "Айгерим", "Диана"] # Дополни своими 12-13 именами

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/claim-prize")
async def claim_prize(
    background_tasks: BackgroundTasks, 
    name: str = Form(...), 
    email: str = Form(...)
):
    # Простая проверка имени
    if name.strip() in GIRLS_LIST:
        # Отправляем письмо в фоновом режиме, чтобы юзер сразу увидел "Успех!"
        background_tasks.add_task(send_gift_email, email, name)
        return {"status": "success", "message": "Письмо с сертификатом уже летит к тебе!"}
    
    return {"status": "error", "message": "Имя не найдено в списке группы."}