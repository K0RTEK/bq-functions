import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_traffic_type(campaign):
    campaign = is_none(campaign)
    if re.search(r'_p_', campaign):
        return 'Поиск'
    elif re.search(r'_s_', campaign):
        return 'Сеть'
    else:
        return 'Прочее'
