import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_channel(calltracking, traffic_source, source_engine, direct_click_order, utm_source, utm_medium, utm_campaign, utm_content, utm_term):
    calltracking = is_none(calltracking)
    traffic_source = is_none(traffic_source)
    source_engine = is_none(source_engine)
    direct_click_order = is_none(direct_click_order)
    utm_source = is_none(utm_source)
    utm_medium = is_none(utm_medium)
    utm_campaign = is_none(utm_campaign)
    utm_content = is_none(utm_content)
    utm_term = is_none(utm_term)

    if re.search(r'^cpa_', utm_source):
        return "Лидогенерация"
    elif re.search(r'yandex', utm_source) and re.search(r'cpc', utm_medium) and \
       (re.search(r'mg_', utm_campaign) or re.search(r'mg_', utm_content) or re.search(r'mg_', utm_term)):
        return "Яндекс Директ"
    elif source_engine == 'Yandex: Direct' and utm_source is None and re.search(r'mg_', direct_click_order):
        return "Яндекс Директ"
    elif re.search(r'mg|sm', calltracking):
        return "Яндекс Директ"
    elif re.search(r'посетители без рекламной кампании|прямые заходы', calltracking) and re.search(r'yandex', utm_source) and re.search(r'mg_', utm_campaign):
        return "Яндекс Директ"
    elif traffic_source == 'Search engine traffic' and utm_source is None and utm_medium is None:
        return "Поисковые системы"
    elif traffic_source == 'Link traffic' and utm_source is None and utm_medium is None:
        return "Переходы по ссылкам"
    elif re.search(r'yandex', utm_source) and utm_medium.lower() == 'cpc' and not (re.search(r'mg_', utm_campaign) or re.search(r'mg_', utm_content) or re.search(r'mg_', utm_term)):
        return "Чужая контекстная реклама"
    return None