import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_object(parameter):
    parameter = is_none(parameter)
    if re.search(r'sobytie|sob-', parameter):
        return 'Событие'
    elif re.search(r'simvol|sim-', parameter):
        return 'Символ'
    elif re.search(r'don-brand-mg', parameter):
        return 'donstroy.com'
    elif re.search(r'don-regiony', parameter):
        return 'РЕГИОНАЛЬНАЯ КАМПАНИЯ'
    elif re.search(r'don-kommercia-mg', parameter):
        return 'КОММЕРЧЕСКАЯ НЕДВИЖИМОСТЬ'
    else:
        return 'Другой'