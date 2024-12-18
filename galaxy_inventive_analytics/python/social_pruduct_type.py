import re
import datetime as dt

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def social_pruduct_type(campaign, date):
    campaign = is_none(campaign)
    if date <= dt.date(2022, 12, 31):
        return ''
    elif date > dt.date(2022, 12, 31):
        if re.search(r'iphone_', campaign):
            return 'iPhone'
        elif re.search(r'macbook_', campaign):
            return 'macbook'
        elif re.search(r'ipad_', campaign):
            return 'iPad'
        elif re.search(r's22', campaign):
            return 's22'
        elif re.search(r's23', campaign):
            return 's23'
        elif re.search(r'flip4', campaign):
            return 'Flip4'
        elif re.search(r'fold', campaign):
            return 'Fold'
        elif re.search(r'all_|pf_m_dir_dnmc|pf_m_ret_dnmc', campaign):
            return ' '
        else:
            return ''
    else:
        return ''