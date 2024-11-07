import requests

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

def study_score(data: dict):
    tasks = sum_task(data['tasks'])
    tasks += sum_task(data['bonus'])
    tasks = round(tasks * (1 + data['prize'] / 100), 1) - int(data['fine'])
    return tasks