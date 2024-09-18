import awsgi
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory='app/templates')
app.mount('/static', StaticFiles(directory='app/static'), 'static')

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
    },
    "major_id": 1,
    "major": "stringstri",
    "course": 1,
    "special_notes": "string"
}

variant = 'Permission denied'

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse(name='students.html',
                                      context={'request': request, 'student': student, 'variant': variant})

def handler(event, context):
    return awsgi.response(app, event, context)