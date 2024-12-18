import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def social_format(campaign):
    campaign = is_none(campaign)
    if re.search(r'carusel_|pf_m_ret_dnmc_action', campaign):
        return 'Карусель'
    elif re.search(r'rs_|site_|pf_m_dir_dnmc', campaign):
        return 'Реклама сайта'
    elif re.search(r'multi_', campaign):
        return 'Мультиформат'
    elif re.search(r'nat_', campaign):
        return 'Натив'
    elif re.search(r'video', campaign):
        return 'Видео'
    elif re.search(r'dro', campaign):
        return 'ДРО'
    else:
        return 'NaN'
