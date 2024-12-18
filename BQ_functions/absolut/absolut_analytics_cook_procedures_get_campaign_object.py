import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_campaign_object(date, parameters):
    parameters = [is_none(param) for param in parameters]
    for param in parameters:
        if re.search(r'zuopt', param, re.IGNORECASE):
            return 'ЗУ Опт'
        elif re.search(r'omegaplaza', param, re.IGNORECASE):
            return 'Омега Плаза'
        elif re.search(r'gelendgik', param, re.IGNORECASE):
            return 'ЗУ Геленджик'
    return None
