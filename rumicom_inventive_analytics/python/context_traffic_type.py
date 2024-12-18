import re
import datetime as dt

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def context_traffic_type(campaign):
    campaign = is_none(campaign)
    if re.search(r'_p_', campaign):
        return ' '
    elif re.search(r'_s_', campaign):
        return ' '
    elif re.search(r'tov|perfomance', campaign):
        return ' / '
    else:
        return 'NaN'