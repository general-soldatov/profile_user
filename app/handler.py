import requests
from app.database import UserVar

def sum_task(data: dict) -> float:
    return sum(map(int, data.values()))

def get_range(score: float | int):
    url = 'https://storage.yandexcloud.net/termex-bot/telegram-bot/static/ranger.json'
    page = requests.get(url)
    for key, value in page.json().items():
        if score < int(key):
            return value

def profile(user_id: int):
    data = UserVar().get_user(user_id)
    tasks = sum_task(data['tasks'])
    tasks += sum_task(data['bonus'])
    tasks = round(tasks * (1 + data['prize'] / 100), 1)
    rater = get_range(tasks)
    fine = 5 - int(data['fine'])
    return {
        "name": data['name'],
        "range": rater['name'],
        "quote": rater['quote'],
        "rate": tasks,
        "img": rater['image'],
        "star": fine,
        "info": {
            'Профиль': data['profile'],
            'Группа': data['group'],
            'Вариант': data['var']['var_all'],
            'Вариант Д1': data['var']['var_d1']
        }
    }
