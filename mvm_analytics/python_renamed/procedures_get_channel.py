import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_channel(source, medium):
    source = is_none(source)
    medium = is_none(medium)
    if medium == 'organic':
        return 'ORGANIC'
    elif source == 'yandex' and medium == 'referral':
        return 'ORGANIC'
    elif medium == 'cpa':
        return 'CPA'
    elif medium == '(none)':
        return 'DIRECT'
    elif medium.lower() == 'email':
        return 'EMAIL'
    elif source == 'yandex' and medium == 'cpc':
        return 'PAID'
    elif source in ('2gis', 'yandex_maps'):
        return 'GEO'
    elif re.search(r'regmarket|blizko|pulscen|price', source) and medium == 'cpc':
        return 'PAID'
    elif source in ('mt', 'vk', 'vkontakte', 'vkr') and re.search(r'cpc|cpm', medium):
        return 'PAID'
    elif source in ('soloway') and medium == 'rs':
        return 'PAID'
    elif source in ('Hybrid', 'hybrid') and medium in ('cpc', 'cpm'):
        return 'PAID'
    else:
        return 'OTHER'