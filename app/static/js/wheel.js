function spin() {
    const wheel = document.getElementById('wheel-img');
    const sectors = 8; // например: Сейшелы, Айфон, Камри, СЕРТИФИКАТ, Квартира...
    const prizeIndex = 3; // Индекс сектора с сертификатом (от 0)
    
    // Рассчитываем угол: полные круги + смещение до нужного сектора
    const stopAngle = (360 * 5) + (360 / sectors * (sectors - prizeIndex));
    
    wheel.style.transition = "transform 4s ease-out";
    wheel.style.transform = `rotate(${stopAngle}deg)`;

    // Через 4 секунды показываем форму ввода почты
    setTimeout(() => {
        document.getElementById('email-form').style.display = 'block';
    }, 4500);
}