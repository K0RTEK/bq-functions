import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def pruduct_type(campaign):
    campaign = is_none(campaign)
    if re.search(r'iphone', campaign):
        return 'iPhone'
    elif re.search(r'imac', campaign):
        return 'imac'
    elif re.search(r'mac|macbook_', campaign):
        return 'MacBook'
    elif re.search(r'ipad_', campaign):
        return 'iPad'
    elif re.search(r'all_|pf_m_dir_dnmc|pf_m_ret_dnmc', campaign):
        return 'все товары'
    elif re.search(r'apple-watch_', campaign):
        return 'Apple Watch'
    elif re.search(r'noapple', campaign):
        return 'не Apple'
    else:
        return 'NaN'
