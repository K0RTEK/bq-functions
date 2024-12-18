import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_campaign_object(date, *parameters):
    parameters = [is_none(x) for x in parameters]
    if any(x in parameters for x in ['don-sobytie-mg', 'sobytie', 'sob']):
        return ' '
    elif any(x in parameters for x in ['don-simvol-mg', 'simvol', 'sim']):
        return ' '
    elif any(x in parameters for x in ['don-regiony', ' ']):
        return ' '
    elif any(x in parameters for x in ['don-kommercia-mg', ' ']):
        return ' '
    elif any(x in parameters for x in ['don-brand-mg', 'donstroy.com']):
        return 'donstroy.com'
    elif all(re.search(r'^sobytie|^sob', x) for x in parameters):
        return ' '
    elif all(re.search(r'^simvol|^sim', x) for x in parameters):
        return ' '
    elif all(re.search(r'^donstroy', x) for x in parameters):
        return 'donstroy.com | | '
    else:
        return None