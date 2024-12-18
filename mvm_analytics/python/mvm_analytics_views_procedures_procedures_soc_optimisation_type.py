import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def soc_optimisation_type(campaign):
    campaign = is_none(campaign)
    if not re.search(r'mg_', campaign):
        return ' '
    elif re.search(r'_cpa', campaign):
        return '  '
    else:
        return 'Other'