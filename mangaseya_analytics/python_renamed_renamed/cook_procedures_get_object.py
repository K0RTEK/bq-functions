import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_object(parameter):
    parameter = is_none(parameter)
    if re.search(r'на\.речном|na\.rechnom', parameter):
        return 'Мангазея на Речном'
    else:
        return 'Не определено'