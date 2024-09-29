import json
from app.handler import profile
from app.database import UserVar
from base import code

def ranger():
    data = {
        10: {
            'name': 'Ёжик',
            'quote': 'Super',
            'image': 'https://avatars.mds.yandex.net/i?id=3fe0791a9a5fb1f0d69c307e941ce3ca_l-10769069-images-thumbs&n=13'
        },
        30: {
            'name': 'Крош',
            'quote': 'Super',
            'image': 'https://yt3.googleusercontent.com/ZDSAMV2E3sYowKeOaE-LnyX9k8pbm_kZkxUij2FVNwfGnX-yFyCdcvEOybw4t5jk0ey9Hw60wg=s900-c-k-c0x00ffffff-no-rj'
        },
        50: {
            'name': 'Копатыч',
            'quote': 'Super',
            'image': 'https://i.pinimg.com/originals/32/84/09/328409dc45e1e67ba42d3f90191e778f.jpg'
        },
        80: {
            'name': 'Пин',
            'quote': 'Super',
            'image': 'https://steamuserimages-a.akamaihd.net/ugc/2457357698622614042/FF58AA3A289A6F2FA9F63EEF9C0B2E4310ABEA25/?imw=512&amp;imh=512&amp;ima=fit&amp;impolicy=Letterbox&amp;imcolor=%23000000&amp;letterbox=true'
        },
        150: {
            'name': 'Лосяш',
            'quote': 'Super',
            'image': 'https://img.razrisyika.ru/kart/125/499535-smeshariki-losyash-35.jpg'
        }

    }

    with open('static/ranger.json', 'w', encoding='utf-8') as fl:
        json.dump(data, fl, ensure_ascii=False, indent=4)
        print('Success')


print(UserVar().get_user(980314213))
var = '1814265390'

# for i in code:
#     UserVar().put_item(user_id=int(i['user_id']), name=i['name'], profile=i['profile'], group=i['group'], var=i['var']['var_all'], var_d1=i['var']['var_d1'])

print(UserVar().all_users())
