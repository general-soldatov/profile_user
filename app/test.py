import json

def ranger():
    data = {
        10: {
            'name': 'Ёжик',
            'image': 'https://avatars.mds.yandex.net/i?id=3fe0791a9a5fb1f0d69c307e941ce3ca_l-10769069-images-thumbs&n=13'
        },
        30: {
            'name': 'Крош',
            'image': 'https://yt3.googleusercontent.com/ZDSAMV2E3sYowKeOaE-LnyX9k8pbm_kZkxUij2FVNwfGnX-yFyCdcvEOybw4t5jk0ey9Hw60wg=s900-c-k-c0x00ffffff-no-rj'
        },
        50: {
            'name': 'Копатыч',
            'image': 'https://i.pinimg.com/originals/32/84/09/328409dc45e1e67ba42d3f90191e778f.jpg'
        },
        80: {
            'name': 'Пин',
            'image': 'https://steamuserimages-a.akamaihd.net/ugc/2457357698622614042/FF58AA3A289A6F2FA9F63EEF9C0B2E4310ABEA25/?imw=512&amp;imh=512&amp;ima=fit&amp;impolicy=Letterbox&amp;imcolor=%23000000&amp;letterbox=true'
        },
        150: {
            'name': 'Лосяш',
            'image': 'https://img.razrisyika.ru/kart/125/499535-smeshariki-losyash-35.jpg'
        }

    }

    with open('static/ranger.json', 'w', encoding='utf-8') as fl:
        json.dump(data, fl, ensure_ascii=False, indent=4)
        print('Success')

# ranger()

data = """{'type': 'http', 'http_version': '1.1', 'method': 'GET', 'headers': [[b'accept', b'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'], [b'accept-encoding', b'gzip, deflate, br, zstd'], [b'accept-language', b'ru-RU,ru;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'], [b'cache-control', b'max-age=0'], [b'host', b'd5dvtf5ioi8q69ckjelk.apigw.yandexcloud.net'], [b'priority', b'u=0, i'], [b'sec-ch-ua', b'"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"'], [b'sec-ch-ua-mobile', b'?0'], [b'sec-ch-ua-platform', b'"Windows"'], [b'sec-fetch-dest', b'document'], [b'sec-fetch-mode', b'navigate'], [b'sec-fetch-site', b'none'], [b'sec-fetch-user', b'?1'], [b'uber-trace-id', b'924905fba4a01ed4:cc2e5ec39f214e68:1ea370d0861135fd:1'], [b'upgrade-insecure-requests', b'1'], [b'user-agent', b'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'], [b'x-api-gateway-function-id', b'd4egk2ovff8l2mtic5ir'], [b'x-envoy-external-address', b'176.59.70.195'], [b'x-envoy-original-path', b'/telegram_bot/203'], [b'x-forwarded-for', b'176.59.70.195'], [b'x-forwarded-proto', b'https'], [b'x-real-remote-address', b'176.59.70.195:6902'], [b'x-request-id', b'efc2d519-d01a-41ff-b5d7-0c12cdfbd4fc'], [b'x-serverless-certificate-ids', b'{}'], [b'x-serverless-gateway-id', b'd5dvtf5ioi8q69ckjelk'], [b'x-trace-id', b'6a2c61c3-3834-420d-b309-c16c3a3c81e8']], 'path': '/telegram_bot/{name+}', 'raw_path': None, 'root_path': '', 'scheme': 'https', 'query_string': b'', 'server': ('d5dvtf5ioi8q69ckjelk.apigw.yandexcloud.net', 80), 'client': ('176.59.70.195', 0), 'asgi': {'version': '3.0', 'spec_version': '2.0'}, 'aws.event': {'httpMethod': 'GET', 'headers': {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'Accept-Encoding': 'gzip, deflate, br, zstd', 'Accept-Language': 'ru-RU,ru;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6', 'Cache-Control': 'max-age=0', 'Host': 'd5dvtf5ioi8q69ckjelk.apigw.yandexcloud.net', 'Priority': 'u=0, i', 'Sec-Ch-Ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"', 'Sec-Ch-Ua-Mobile': '?0', 'Sec-Ch-Ua-Platform': '"Windows"', 'Sec-Fetch-Dest': 'document', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'none', 'Sec-Fetch-User': '?1', 'Uber-Trace-Id': '924905fba4a01ed4:cc2e5ec39f214e68:1ea370d0861135fd:1', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36', 'X-Api-Gateway-Function-Id': 'd4egk2ovff8l2mtic5ir', 'X-Envoy-External-Address': '176.59.70.195', 'X-Envoy-Original-Path': '/telegram_bot/203', 'X-Forwarded-For': '176.59.70.195', 'X-Forwarded-Proto': 'https', 'X-Real-Remote-Address': '176.59.70.195:6902', 'X-Request-Id': 'efc2d519-d01a-41ff-b5d7-0c12cdfbd4fc', 'X-Serverless-Certificate-Ids': '{}', 'X-Serverless-Gateway-Id': 'd5dvtf5ioi8q69ckjelk', 'X-Trace-Id': '6a2c61c3-3834-420d-b309-c16c3a3c81e8'}, 'url': '/telegram_bot/203?', 'params': {'name': '203'}, 'multiValueParams': {'name': ['203']}, 'pathParams': {'name': '203'}, 'multiValueHeaders': {'Accept': ['text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'], 'Accept-Encoding': ['gzip, deflate, br, zstd'], 'Accept-Language': ['ru-RU,ru;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'], 'Cache-Control': ['max-age=0'], 'Host': ['d5dvtf5ioi8q69ckjelk.apigw.yandexcloud.net'], 'Priority': ['u=0, i'], 'Sec-Ch-Ua': ['"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"'], 'Sec-Ch-Ua-Mobile': ['?0'], 'Sec-Ch-Ua-Platform': ['"Windows"'], 'Sec-Fetch-Dest': ['document'], 'Sec-Fetch-Mode': ['navigate'], 'Sec-Fetch-Site': ['none'], 'Sec-Fetch-User': ['?1'], 'Uber-Trace-Id': ['924905fba4a01ed4:cc2e5ec39f214e68:1ea370d0861135fd:1'], 'Upgrade-Insecure-Requests': ['1'], 'User-Agent': ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'], 'X-Api-Gateway-Function-Id': ['d4egk2ovff8l2mtic5ir'], 'X-Envoy-External-Address': ['176.59.70.195'], 'X-Envoy-Original-Path': ['/telegram_bot/203'], 'X-Forwarded-For': ['176.59.70.195'], 'X-Forwarded-Proto': ['https'], 'X-Real-Remote-Address': ['176.59.70.195:6902'], 'X-Request-Id': ['efc2d519-d01a-41ff-b5d7-0c12cdfbd4fc'], 'X-Serverless-Certificate-Ids': ['{}'], 'X-Serverless-Gateway-Id': ['d5dvtf5ioi8q69ckjelk'], 'X-Trace-Id': ['6a2c61c3-3834-420d-b309-c16c3a3c81e8']}, 'queryStringParameters': {}, 'multiValueQueryStringParameters': {}, 'requestContext': {'identity': {'sourceIp': '176.59.70.195', 'userAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'}, 'httpMethod': 'GET', 'requestId': 'efc2d519-d01a-41ff-b5d7-0c12cdfbd4fc', 'requestTime': '20/Sep/2024:06:04:06 +0000', 'requestTimeEpoch': 1726812246}, 'body': '', 'isBase64Encoded': True, 'path': '/telegram_bot/{name+}'}, 'aws.context': <runtime.RuntimeContext object at 0x7f641e23c200>}"""

with open('info.json', 'w') as fl:
    # sl = json.loads(data)
    json.dump(data, fl, indent=4)