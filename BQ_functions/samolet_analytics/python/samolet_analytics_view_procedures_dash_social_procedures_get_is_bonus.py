import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_is_bonus(date, parameter):
    parameter = is_none(parameter)
    if re.search(r'bonus', parameter, re.I):
        return 'bonus'
    else:
        return '-'