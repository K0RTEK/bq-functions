import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def perform_type(campaign):
    campaign = is_none(campaign)
    if re.search(r'pf_', campaign):
        return 'Перформ'
    elif re.search(r'md_', campaign):
        return 'Медийка'
    else:
        return 'NaN'
