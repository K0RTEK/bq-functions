import re
import datetime as dt

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def social_platform(campaign, date):
    campaign = is_none(campaign)
    if date <= dt.date(2022, 12, 31):
        return 'NaN'
    elif date > dt.date(2022, 12, 31):
        if re.search(r'cross_|pf_m_dir_dnmc|pf_m_ret_dnmc_action', campaign):
            return 'Все устройства'
        elif re.search(r'mob_', campaign):
            return 'Мобилка'
        elif re.search(r'web_', campaign):
            return 'Веб'
        else:
            return 'NaN'