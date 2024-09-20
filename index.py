import json

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory='app/templates')
app.mount('/telegram_bot/static', StaticFiles(directory='static'), 'static')

student = {
    "name": "string",
    "range": "string",
    "img": "https://img.razrisyika.ru/kart/125/499535-smeshariki-losyash-35.jpg",
    "rate": 45,
    "star": 3,
    "info": {
        'profile': 'HTTC',
        'variant': 3,
        'group': 34
    }
}

information = {
    'denied': 'Permission denied',
    'style': [
        # 'https://storage.yandexcloud.net/termex-bot/telegram-bot/static/style_tel.css',
        'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css',
        '/telegram_bot/static/style_tel.css'
    ]
    }


@app.get("/telegram_bot/bot={name}")
async def root(request: Request, name: str):
    name = int(name)
    if name:
        student['rate'] = name
        with open('static/ranger.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            for key, value in data.items():
                if name < int(key):
                    student['img'] = value['image']
                    student['range'] = value['name']
                    break

    return templates.TemplateResponse(name='students.html',
                                      context={'request': request,
                                               'student': student,
                                               'information': information})
