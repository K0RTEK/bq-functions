import re
import datetime as dt

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_phone(str_field):
    cleaned_phone = re.sub(r'\..*|[^0-9]', '', str_field)
    return cleaned_phone