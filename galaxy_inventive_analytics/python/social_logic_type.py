import re
import datetime as dt

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def social_logic_type(campaign, date):
    campaign = is_none(campaign)
    if date <= dt.date(2022,12,31):
        return 'NaN'
    else:
        if re.search(r'kw_', campaign):
            return 'ключи'
        elif re.search(r'int_', campaign):
            return 'интересы'
        elif re.search(r'auto', campaign):
            return 'автоинтересы'
        elif re.search(r'dnmc_', campaign):
            return 'динрем'
        elif re.search(r'sttc_|stts_', campaign):
            return 'стат.ремаркетинг'
        else:
            return 'NaN'