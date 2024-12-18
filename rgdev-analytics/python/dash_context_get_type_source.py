import re
import datetime as dt

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_type_source(campaign_name, date):
    campaign_name = is_none(campaign_name)

    if re.search(r'_s_', campaign_name, re.IGNORECASE):
        return 'Поиск'
    elif re.search(r'_n_|_epk_', campaign_name, re.IGNORECASE):
        return 'Сеть'
    elif re.search(r'_mk_', campaign_name, re.IGNORECASE):
        return 'Мастер_кампаний'
    elif re.search(r'_tk_', campaign_name, re.IGNORECASE):
        return 'ТК'
    elif re.search(r'_tg_', campaign_name, re.IGNORECASE):
        return 'ТГ'
    elif re.search(r'_s_|_n_', campaign_name, re.IGNORECASE):
        return 'Поиск/Сеть'

    return None