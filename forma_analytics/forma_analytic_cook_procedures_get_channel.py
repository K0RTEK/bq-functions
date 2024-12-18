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
    if "лидогенераторы" in calltracking.lower():
        return "Лидогенерация"
    elif re.search(r'яндекс(.|..)директ', calltracking) and not re.search(r'rtb|performance|telegram|яндекс видео_olv', calltracking):
        return "Яндекс Директ"
    elif re.search(r'google', utm_source) and re.search(r'cpc', utm_medium) and (re.search(r'mg_', utm_campaign) or re.search(r'mg_', utm_content) or re.search(r'mg_', utm_term)):
        return "Google Ads"
    elif traffic_source == 'Search engine traffic' and utm_source is None and utm_medium is None:
        return "Поисковые системы"
    elif traffic_source == 'Link traffic' and utm_source is None and utm_medium is None:
        return "Переходы по ссылкам"
    elif re.search(r'yandex', utm_source):
        return "Чужая контекстная реклама"
    elif (re.search(r'vk_ads|vk_reklama|vk$', utm_source) or re.search(r'mytarget|facebook|tiktok|telegram', utm_source)) and utm_medium in ['cpc', 'cpm']:
        return "Реклама в соц.сетях"
    return None