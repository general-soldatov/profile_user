import json
from app.database import UserVar

def sum_task(data: dict) -> float:
    return sum(map(int, data.values()))

def get_range(score: float | int):
    with open('static/ranger.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            for key, value in data.items():
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
