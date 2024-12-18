import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_geo(campaign):
    campaign = is_none(campaign)
    if re.search(r'msk', campaign):
        return 'Москва и МО'
    elif re.search(r'spb', campaign):
        return 'Санкт-Петербург и ЛО'
    elif re.search(r'highcr', campaign):
        return 'highcr'
    elif re.search(r'lowcr', campaign):
        return 'lowcr'
    elif re.search(r'rf', campaign):
        return 'РФ'
    else:
        return 'Прочее'
