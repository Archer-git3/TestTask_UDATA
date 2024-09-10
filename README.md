# Python Project Test Task

Цей проєкт являє собою тестове завдання на Python, яке використовує Selenium та Flask для веб застосунку.

## Вимоги

Перед запуском переконайтеся, що у вас встановлені наступні компоненти:
- Python 3.x
- pip (Python Package Manager)
- Microsoft Edge Browser
- Microsoft Edge WebDriver

## Інструкція з встановлення

1. **Клонування репозиторію**
   
   Спочатку клонувати репозиторій на ваш локальний комп'ютер за допомогою наступної команди:

   ```bash
   git clone https://github.com/username/repo-name.git
   ```
2. **Встановлення необхідних бібліотек**

   ```bash
   pip install -r requirements.txt
   ```
3. **Встановлення Microsoft Edge WebDriver**

   Завантажте [Microsoft Edge WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) для вашої версії браузера Edge. Після цього:

   Розпакуйте WebDriver.
   Додайте WebDriver до середовищя де знаходиться безпосередньо програми.
   Або вкажіть шлях до WebDriver безпосередньо в коді.

4. **Запуск програми**

   - Запустіть файл `make_json.py`, щоб створити початковий json файл і заповнити його

   - Після успішного виконання першого файлу, запустіть файл `app.py`


## Опис файлів
make_json.py – Генерує необхідні JSON-файли для подальшого використання.

app.py – Основний скрипт для запуску додатку.
