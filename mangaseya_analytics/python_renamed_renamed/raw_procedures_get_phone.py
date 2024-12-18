import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_phone(phone):
    return is_none(re.sub(r'\..*|[^0-9]', '', is_none(phone)))