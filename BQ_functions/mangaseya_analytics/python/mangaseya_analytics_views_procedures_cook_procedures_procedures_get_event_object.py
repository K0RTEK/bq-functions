import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_event_object(date, parameters):
    parameters = [is_none(param) for param in parameters]
    if any(param in parameters for param in ['dummy','dummy']):
        return 'placeholder'
    elif any(re.search(r'dummy', param) for param in parameters):
        return 'placeholder'
    else:
        return get_campaign_object(is_none(date), parameters)