import json

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from app.handler import termex_profile, phys_profile
from app.rate_maker import handler

app = FastAPI()
templates = Jinja2Templates(directory='app/templates')
app.mount('/telegram_bot/static', StaticFiles(directory='static'), 'static')


information = {
    'denied': 'Permission denied',
    'style': [
        'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css',
        '/telegram_bot/static/style_tel.css'
    ]
    }


@app.get("/telegram_bot/bot={name}")
async def termex(request: Request, name: str):
    name = int(name)
    student = termex_profile(name)

    return templates.TemplateResponse(name='students.html',
                                      context={'request': request,
                                               'student': student,
                                               'information': information})

@app.get("/telegram_bot/phys/bot={name}")
async def phys(request: Request, name: str):
    name = int(name)
    student = phys_profile(name)

    return templates.TemplateResponse(name='students.html',
                                      context={'request': request,
                                               'student': student,
                                               'information': information})

@app.get("/telegram_bot/rate={name}")
async def dev_rate(name: str):
    return handler(name)
