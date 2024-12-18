import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def social_logic(campaign):
    campaign = is_none(campaign)
    if re.search(r'ret_', campaign):
        return 'ретаргет'
    elif re.search(r'dir_', campaign):
        return 'прямая'
    else:
        return 'NaN'
