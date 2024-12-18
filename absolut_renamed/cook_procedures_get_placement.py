import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_placement(parameter):
    parameter = is_none(parameter)

    if re.search(r'yandex|яндекс', parameter) and not re.search(r'realty|недвижимость|navigator|навигатор', parameter):
        return 'Яндекс Директ'
    if re.search(r'avito|авито', parameter):
        return 'Авито'
    if re.search(r'cian|циан', parameter):
        return 'Циан'
    # Add more conditions based on original SQL function
    return 'Не определено'
