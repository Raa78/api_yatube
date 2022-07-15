# API project for Yatube - bloggers’ social network

## Описание проекта:
Создание API сервиса для социальной сети по публикации личных дневников.

## Технологии:
* Python 3.7
* Django 2.2
* Django REST Framework 3.12

### Инструкция для запуска проекта:
- Клонируйте репозиторий
```
git clone https://github.com/Raa78/api_yatube.git
```
- Перейдите в папку с проектом
```
cd api_yatube
```
- В папке с проектом установите виртуальное окружение
Windows
```
python -m venv имя_виртуального_окружения
```
_например_
```
python -m venv venv
```

MacOS/Unix
```
python3 -m venv имя_виртуального_окуржения
```
_например_
```
python3 -m venv venv
```
- Активируйте виртуальное окружение
Windows
```
source venv/Scripts/activate
```

MacOS/Unix
```
source venv/bin/activate
```
_или_
```
. venv/bin/activate
```
- Установите зависимости из файла requirements.txt
```
pip install -r requirements.txt
``` 
- Перейдите в папку yatube_api и выполните:
Миграции
```
python manage.py makemigrations
python manage.py migrate
```
Запустите сервер
```
python manage.py runserver
```
