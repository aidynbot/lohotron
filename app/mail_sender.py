import os
from email.message import EmailMessage
import aiosmtplib
from dotenv import load_dotenv

load_dotenv()

async def send_gift_email(recipient_email: str, girl_name: str):
    # Настройки из .env
    SMTP_HOST = "smtp.gmail.com"
    SMTP_PORT = 465
    SENDER_EMAIL = os.getenv("EMAIL_ADDRESS")
    SENDER_PASSWORD = os.getenv("EMAIL_PASSWORD")

    msg = EmailMessage()
    msg["Subject"] = f"С 8 Марта, {girl_name}! 🌸 Твой подарок от парней АЖ-45"
    msg["From"] = SENDER_EMAIL
    msg["To"] = recipient_email
    
    # Текст письма
    msg.set_content(f"Привет, {girl_name}!\n\nТы выиграла сертификат в 'Колесе Фортуны'! Поздравляем тебя с праздником!")

    # Логика вложения файла (если файлы лежат в /certs)
    file_path = f"certs/certificate.pdf" # Можно сделать именные: f"certs/{girl_name.lower()}.pdf"
    
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            file_data = f.read()
            msg.add_attachment(
                file_data,
                maintype="application",
                subtype="pdf",
                filename="Certificate_8_March.pdf"
            )

    await aiosmtplib.send(
        msg,
        hostname=SMTP_HOST,
        port=SMTP_PORT,
        username=SENDER_EMAIL,
        password=SENDER_PASSWORD,
        use_tls=True
    )