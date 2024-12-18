import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def str_num(numer):
    numer = is_none(numer)
    cleaned = re.sub(r'\..*|[^0-9,]', '', numer.replace('.', 'pp').replace(',', '.').strip())
    if cleaned in ['', '0', ',0', ',00', '0,00', '0,0', None]:
        return None
    return float(cleaned)
