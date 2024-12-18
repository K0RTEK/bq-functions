import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def str_num(numer):
    numer = is_none(numer)
    clean_numer = re.sub(r'\..*|[^0-9]', '', re.sub(r',', '.', re.sub(r'\.', 'pp', numer.strip())))
    if clean_numer in ['', '0', ',0', ',00', '0,00', '0,0', None]:
        return None
    return float(clean_numer)