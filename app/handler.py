import requests
from app.database import UserVar
from app.database_phys import DBStudents

def sum_task(data: dict) -> float:
    return sum(map(int, data.values()))

def get_range(score: float | int):
    url = 'https://storage.yandexcloud.net/termex-bot/telegram-bot/static/ranger.json'
    page = requests.get(url)
    for key, value in page.json().items():
        if score < int(key):
            return value

def get_fine(score: float | int):
    star = {5: 60, 4: 50, 3: 40, 2: 25, 1: 10, 0: -100}
    for key, value in star.items():
        if score > value:
            return key

def profile(user_id: int):
    try:
        data = UserVar().get_user(user_id)
    except IndexError:
        return None
    tasks = sum_task(data['tasks'])
    tasks += sum_task(data['bonus'])
    tasks = round(tasks * (1 + data['prize'] / 100), 1) - int(data['fine'])
    rater = get_range(tasks)
    fine = get_fine(tasks)
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
        },
        "tasks": data['tasks']
    }

def phys_profile(user_id: int):
    try:
        data = DBStudents().get_user(user_id)
    except IndexError:
        return None
    tasks = sum_task(data['tasks'])
    tasks += sum_task(data['bonus'])
    tasks = round(tasks * (1 + data['prize'] / 100), 1) + int(data['fine'])
    rater = get_range(tasks)
    fine = get_fine(tasks)
    return {
        "name": data['name'],
        "range": rater['name'],
        "quote": rater['quote'],
        "rate": tasks,
        "img": rater['image'],
        "star": fine,
        "info": {
            'Профиль': data['profile'],
            'Группа': data['group']
        },
        "tasks": data['tasks']
    }
