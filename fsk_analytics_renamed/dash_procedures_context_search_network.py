import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def search_network(campaign_global):
    campaign_global = is_none(campaign_global)
    if re.search(r'_srch|поиск', campaign_global):
        return 'Search'
    elif re.search(r'epk-direct', campaign_global):
       return 'ЕПК (единая кампания)'
    elif re.search(r'mc.direct', campaign_global):
       return 'Мастер кампаний'
    elif re.search(r'tc.direct', campaign_global):
        return 'Товарные кампании'
    return 'Network'