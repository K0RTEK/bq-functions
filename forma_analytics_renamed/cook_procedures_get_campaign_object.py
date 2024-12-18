import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_campaign_object(date, parameters):
    parameters = [is_none(param.strip()) for param in parameters]

    if any(param == 'сюда id' for param in parameters):
        return 'Republic'

    # Регулярные выражения
    for param in parameters:
        if re.search(r'(^|.)(republic)($|.)', param):
            return 'Republic'
        elif re.search(r'(^|.)(moments)($|.)', param):
            return 'Moments'
        elif re.search(r'(^|.)(mono)($|.)', param):
            return 'Mono'
        elif re.search(r'(^|.)(forma)($|.)', param):
            return 'Brand FORMA'

    return None
