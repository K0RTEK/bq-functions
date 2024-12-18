import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_object(parameter):
    parameter = is_none(parameter)
    if re.search(r'(^|.)(republic)($|.)', parameter):
        return 'Republic'
    elif re.search(r'(^|.)(moments)($|.)', parameter):
        return 'Moments'
    elif re.search(r'(^|.)(mono)($|.)', parameter):
        return 'Mono'
    elif re.search(r'(^|.)(forma)($|.)', parameter):
        return 'Brand FORMA'
    return 'Не определено'