from app.database import db_phys, db_termex
from app.rate_maker import get_rate
from app.functool import study_score, get_range, get_fine


def termex_profile(user_id: int):
    try:
        data = db_termex.get_user(user_id)
    except IndexError:
        return None
    except KeyError:
        return None
    tasks = study_score(data)
    rater = get_range(tasks)

    if data['profile'] == "Преподаватель":
        rate_list = get_rate('НТТС', 'termex-bot')
    else:
        rate_list = get_rate(data['profile'], 'termex-bot')
    return {
        "name": data['name'],
        "range": rater['name'],
        "quote": rater['quote'],
        "rate": tasks,
        "img": rater['image'],
        "star": get_fine(tasks),
        "info": {
            'Профиль': data['profile'],
            'Группа': data['group'],
            'Вариант': data['var']['var_all'],
            'Вариант Д1': data['var']['var_d1']
        },
        "tasks": data['tasks'],
        "rate_list": rate_list
    }

def phys_profile(user_id: int):
    try:
        data = db_phys.get_user(user_id)
    except IndexError:
        return None
    except KeyError:
        return None
    tasks = study_score(data)
    rater = get_range(tasks)
    if data['profile'] == "Преподаватель":
        rate_list = get_rate('Агроинженерия', 'phys-bot')
    else:
        rate_list = get_rate(data['profile'], 'phys-bot')
    return {
        "name": data['name'],
        "range": rater['name'],
        "quote": rater['quote'],
        "rate": tasks,
        "img": rater['image'],
        "star": get_fine(tasks),
        "info": {
            'Профиль': data['profile'],
            'Группа': data['group']
        },
        "tasks": data['tasks'],
        "rate_list": rate_list
    }
