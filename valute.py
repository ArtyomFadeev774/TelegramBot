import requests


def create_request():
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    result = requests.get(url).json()
    return result

def create_buttons():
    res = create_request()
    results = []
    for element in res['Valute']:
        results.append(element)
    return results

def get_data(key):
    res = create_request()
    return str(res['Valute'][key]['Value']) + 'руб.'