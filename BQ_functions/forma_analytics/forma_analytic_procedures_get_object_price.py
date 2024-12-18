import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_object_price(object_name):
    object_name = is_none(object_name)

    if re.search(r'republic', object_name):
        return 'Republic'
    elif re.search(r'moment', object_name):
        return 'Moments'
    else:
        return f'Иной проект - {object_name}'