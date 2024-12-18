import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_traffic_type(parameter):
    parameter = is_none(parameter)
    if re.search(r'traf', parameter):
        return 'Traffic'
    elif re.search(r'lead', parameter):
        return 'LeadAds'
    elif re.search(r'reach', parameter):
        return 'Reach'
    else:
        return '-'