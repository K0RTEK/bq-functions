import re
import datetime as dt

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def social_age(campaign, date):
    campaign = is_none(campaign)
    if dt.date.fromisoformat(date) <= dt.date(2022, 12, 31):
        return 'NaN'
    else:
        if re.search(r'18_|pf_m_dir_dnmc|pf_m_ret_dnmc_action', campaign):
            return '18'
        elif re.search(r'18-55_', campaign):
            return '18-55'
        elif re.search(r'18-50_', campaign):
            return '18-50'
        elif re.search(r'23-55_', campaign):
            return '23-55'
        else:
            return 'NaN'