import re
import datetime as dt

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def social_logic(campaign, date):
    campaign = is_none(campaign)
    if date <= dt.date(2022, 12, 31):
        if re.search(r'_dir', campaign):
            return 'Прямая логика'
        elif re.search(r'_kw|keys', campaign):
            return 'Ключи'
        elif re.search(r'_int', campaign):
            return 'Интересы'
        elif re.search(r'_ret_dnmc', campaign):
            return 'Дин.рем'
        elif re.search(r'_ret_', campaign) and not re.search(r'dnmc', campaign):
            return 'Ретаргетинг'
        else:
            return 'NaN'
    elif date > dt.date(2022, 12, 31):
        if re.search(r'ret_', campaign):
            return 'ретаргет'
        elif re.search(r'dir_', campaign):
            return 'прямая'
        else:
            return 'NaN'