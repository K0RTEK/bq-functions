import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_object(parameter):
    parameter = is_none(parameter)
    if re.search(r'willtower', parameter):
        return 'Will Towers'
    elif re.search(r'диалог', parameter):
        return 'Диалог'
    elif re.search(r'forest', parameter):
        return 'Forest'
    return 'Не определено'