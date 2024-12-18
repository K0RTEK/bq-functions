import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_channel(calltracking, traffic_source, source_engine, direct_click_order, utm_source, utm_medium, utm_campaign, utm_content, utm_term):
    utm_source = is_none(utm_source)
    utm_medium = is_none(utm_medium)
    utm_campaign = is_none(utm_campaign)
    utm_content = is_none(utm_content)
    utm_term = is_none(utm_term)
    calltracking = is_none(calltracking)
    traffic_source = is_none(traffic_source)
    direct_click_order = is_none(direct_click_order)
    source_engine = is_none(source_engine)

    if re.search(r'yandex', utm_source) and re.search(r'cpc', utm_medium) and re.search(r'mg_', utm_campaign):
        return 'Яндекс Директ'
    elif re.search(r'google', utm_source) and re.search(r'mg_', utm_campaign):
        return 'Google Ads'
    elif traffic_source == 'Search engine traffic':
        return 'Поисковые системы'
    elif traffic_source == 'Link traffic':
        return 'Переходы по ссылкам'
    elif re.search(r'like estate|румбери', calltracking):
        return 'CPA'
    return 'Unknown'