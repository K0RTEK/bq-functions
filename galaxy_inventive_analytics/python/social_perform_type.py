import re
import datetime as dt

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def social_perform_type(campaign, date):
    campaign = is_none(campaign)
    if date <= dt.date(2022, 12, 31):
        return 'NaN'
    elif date > dt.date(2022, 12, 31):
        if re.search(r'pf_', campaign):
            return 'Перформ'
        elif re.search(r'md_', campaign):
            return 'Медийка'
        else:
            return 'NaN'
    else:
        return 'NaN'