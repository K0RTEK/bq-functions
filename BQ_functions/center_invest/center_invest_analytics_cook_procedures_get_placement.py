import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_placement(parameter):
    parameter = is_none(parameter)
    if re.search(r'yandex', parameter):
        return 'Яндекс Директ'
    elif re.search(r'avito', parameter):
        return 'Авито'
    elif re.search(r'vk', parameter):
        return 'Вконтакте'
    return 'Не определено'