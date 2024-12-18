import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def cont_fl_budget_type(campaign):
    campaign = is_none(campaign)
    if re.search(r'_kd_', campaign):
        return ' '
    elif re.search(r'_fed_', campaign):
        return ' '
    else:
        return 'NaN - ' + campaign