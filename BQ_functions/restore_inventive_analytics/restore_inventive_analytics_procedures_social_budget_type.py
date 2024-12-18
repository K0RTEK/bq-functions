import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def budget_type(campaign):
    campaign = is_none(campaign)
    if re.search(r'_m_', campaign):
        return 'основной'
    else:
        return 'NaN'
