import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def str_num_v2(numer):
    numer = is_none(numer)
    return float(re.sub(r',', '.', numer.strip()))