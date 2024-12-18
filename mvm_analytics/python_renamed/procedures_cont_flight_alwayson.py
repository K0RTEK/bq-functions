import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def cont_fl_alwayson(campaign):
    campaign = is_none(campaign)

    if re.search(r'mg_', campaign) is None:
        return ' '
    elif re.search(r'flight', campaign) is not None and re.search(r'_fed_', campaign) is not None:
        return 'Flight  . '
    elif re.search(r'flight', campaign) is not None and re.search(r'_fed_', campaign) is None:
        return 'Flight  . '
    else:
        return 'AlwaysOn'