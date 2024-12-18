import re
import datetime as dt

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def social_format(campaign, date):
    campaign = is_none(campaign)
    if date <= dt.date(2022, 12, 31):
        if re.search(r'_multi|_milti', campaign):
            return 'Мультиформат'
        elif re.search(r'_nat', campaign):
            return 'Формат натив'
        elif re.search(r'_carusel|pf_m_ret_dnmc_action', campaign):
            return 'Карусель'
        elif re.search(r'_rs|_site|pf_m_dir_dnmc', campaign):
            return 'Реклама сайта'
        else:
            return 'NaN'
    else:
        if re.search(r'carusel_|pf_m_ret_dnmc_action', campaign):
            return 'Карусель'
        elif re.search(r'rs_|site_|pf_m_dir_dnmc', campaign):
            return 'Реклама сайта'
        elif re.search(r'multi_', campaign):
            return 'Мультиформат'
        elif re.search(r'nat_', campaign):
            return 'Натив'
        else:
            return 'NaN'