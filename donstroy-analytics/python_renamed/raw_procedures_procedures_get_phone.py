import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_phone(phone):
    phone = is_none(phone)
    return re.sub(r'\..*|[^0-9]', '', phone)