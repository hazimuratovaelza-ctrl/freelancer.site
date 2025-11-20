# Django Freelancer Site — Лиля Хажимуратова

Это готовый каркас Django-проекта (с регистрацией/входом) для портфолио и прайса.
Особенности:
- Django проект с приложениями `main` (контент) и `users` (регистрация/профиль).
- 7 страниц: home, services, portfolio, prices, about, contact, account.
- Реализация входа/регистрации (используется стандартная auth + простая форма регистрации).
- Современный светлый флет-дизайн, адаптивность (Bootstrap), плавная анимация появления текста и hover-эффекты.
- Модели `Service` и `PortfolioItem` для загрузки фото и указания цен через админку.

## Как запустить локально
1. Распакуй архив и перейди в папку проекта (там где manage.py):
   ```bash
   cd freelancer_django_site
   ```
2. Создай виртуальное окружение и активируй его:
   ```bash
   python -m venv venv
   source venv/bin/activate  # или venv\Scripts\activate на Windows
   ```
3. Установи зависимости:
   ```bash
   pip install Django Pillow
   ```
4. Сделай миграции и создай суперпользователя:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser
   ```
5. Запусти сервер:
   ```bash
   python manage.py runserver 0.0.0.0:8000
   ```
   Открой в браузере: `http://localhost:8000/` или на телефоне `http://<IP_компьютера>:8000/`

## Как добавить фото и цены
1. Войдите в админку: `http://localhost:8000/admin/` и добавьте записи в Services и Portfolio items.
2. Загруженные изображения будут сохранены в папке `media/`.

## Если что-то сломалось
- Убедитесь, что вы запускаете команды из папки с `manage.py`.
- Если получаете ошибку `[Errno 2] No such file or directory`, проверьте, что файл `manage.py` действительно там.
- При проблемах — скиньте текст ошибки сюда, помогу исправить.