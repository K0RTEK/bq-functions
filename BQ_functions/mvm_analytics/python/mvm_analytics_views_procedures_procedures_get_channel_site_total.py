import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_channel_site_total(source, medium):
    source = is_none(source)
    medium = is_none(medium)
    if source == 'yandex' and medium in ('organic', 'referral'):
        return 'Organic Yandex'
    elif source == 'google' and medium == 'organic':
        return 'Organic Google'
    elif medium == 'cpa':
        return 'CPA'
    elif source == 'direct' and medium == 'none':
        return 'DIRECT'
    elif medium == 'email':
        return 'EMAIL'
    elif source == 'yandex' and medium == 'cpc':
        return 'PAID'
    elif source in ('2gis', 'yandex_maps'):
        return 'PAID'
    elif re.search(r'regmarket|blizko|pulscen|price', source) and medium == 'cpc':
        return 'PAID'
    elif source in ('mt', 'vk', 'vkontakte', 'vkr') and re.search(r'cpc|cpm', medium):
        return 'PAID'
    elif source == 'soloway' and re.search(r'rs', medium):
        return 'PAID'
    elif source in ('Hybrid', 'hybrid') and medium in ('cpc', 'cpm'):
        return 'PAID'
    else:
        return 'OTHER'