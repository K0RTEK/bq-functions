import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def str_num(numer):
    numer = is_none(numer)
    if numer == '':
        return None
    else:
        return float(re.sub(r',', '.', numer))