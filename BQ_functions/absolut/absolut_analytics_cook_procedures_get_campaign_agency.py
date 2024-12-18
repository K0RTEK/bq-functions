import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_campaign_agency(date, parameters):
    parameters = [is_none(param) for param in parameters]

    for param in parameters:
        if re.search(r'^mg|mg$|-mg_', param, re.IGNORECASE):
            return 'MGCom'
    return 'Other'
