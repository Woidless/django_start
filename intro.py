'''


1. Создать виртуальное окружение (python3 -m venv venv)
2. Установка Джанго и библиотеки (pip install django, pip install psycopg2-binary)
pip freeze > requirements.txt
3. Создание проекта (django-admin startproject <Название проекта> .)
4. Создание приложения (django-admin startapp <название приложения>)
5. Записать название вашего приложения в installed apps в настройках подключение приложение в проект
6. Настройка БД и Приложения 
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': <name of your databases>,
            'USER': <user name in db>,
            'PASSWORD': <User password>,
            'HOST': 'localhost',
            'PORT': 5432
        }
    }

7. создание базы данных в постгресс
8. работа с миграцией
    8.1 создание файлы миграции
        python



'''