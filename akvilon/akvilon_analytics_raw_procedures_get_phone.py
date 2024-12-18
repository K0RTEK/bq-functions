import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_phone(str_field):
    str_field = is_none(str_field)
    # Удаляет все символы, кроме цифр, для получения чистого номера телефона
    return re.sub(r'\..*|[^0-9]', '', str_field)