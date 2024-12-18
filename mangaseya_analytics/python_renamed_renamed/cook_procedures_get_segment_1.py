import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_segment_1(parameter):
    parameter = is_none(parameter)
    if re.search(r'(_|^)mkb(_|$)', parameter):
        return 'МКБ'
    elif re.search(r'(_|^)srch(_|$)', parameter):
        return 'Поиск'
    elif re.search(r'(_|^)net(_|$)', parameter):
        return 'РСЯ'
    elif re.search(r'(_|^)mc-direct(_|$)', parameter):
        return 'МК'
    else:
        return ''