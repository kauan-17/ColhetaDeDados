import json


def ler_json():
    with open('base_teste_json.json', 'r', encoding='utf8') as f:
        return json.load(f)

    data = ler_json()
    print(data)


