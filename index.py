import awsgi
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory='app/templates')

student = {
    "phone_number": "string",
    "first_name": "string",
    "last_name": "string",
    "date_of_birth": "2024-07-23",
    "email": "user@example.com",
    "address": "stringstri",
    "enrollment_year": 2002,
    "major_id": 1,
    "major": "stringstri",
    "course": 1,
    "special_notes": "string"
}

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse(name='students.html',
                                      context={'request': request, 'student': student})

def handler(event, context):
    return awsgi.response(app, event, context)