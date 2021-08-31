# Написать скрипт, автоматизирующий сохранение данных в файле YAML-формата.


import yaml


items_dict = {'items': ['computer', 'printer', 'scanner'],
     'quantity': 5,
     'price': {'computer': '1000€',
                'printer': '200€',
                'scanner': '250€'}}

with open('items.yaml', 'w', encoding='utf-8') as f:
    yaml.dump(items_dict, f, default_flow_style=False, allow_unicode=True, sort_keys=False)


with open('items.yaml', 'r', encoding='utf-8') as f:
    data = yaml.load(f)

print(data)
