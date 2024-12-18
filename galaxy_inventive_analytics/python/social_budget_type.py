import re
import datetime as dt

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def social_budget_type(campaign, date):
    campaign = is_none(campaign)
    if dt.date.fromisoformat(date) <= dt.date(2022,12,31):
        if re.search(r'_m_', campaign):
            return 'основной'
        else:
            return 'NaN'
    else:
        if re.search(r'_m_', campaign):
            return 'основной'
        elif re.search(r'_f_', campaign):
            return 'флайт'
        else:
            return 'NaN'