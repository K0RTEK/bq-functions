import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_channel(calltracking, traffic_source, source_engine, direct_click_order, utm_source, utm_medium, utm_campaign,
                utm_content, utm_term):
    calltracking = is_none(calltracking)
    traffic_source = is_none(traffic_source)
    source_engine = is_none(source_engine)
    direct_click_order = is_none(direct_click_order)
    utm_source = is_none(utm_source)
    utm_medium = is_none(utm_medium)
    utm_campaign = is_none(utm_campaign)
    utm_content = is_none(utm_content)
    utm_term = is_none(utm_term)
    combined = "_".join(
        [calltracking or "", utm_source or "", utm_medium or "", utm_campaign or "", utm_content or "", utm_term or ""])

    if re.search(r'((atommedia).*(call|cpa|лидоген|звон|fid))', combined, re.IGNORECASE):
        return "Лидогенерация"
    if re.search(r'yandex', utm_source, re.IGNORECASE) and re.search(r'cpc|cpm', utm_medium, re.IGNORECASE):
        return 'Яндекс Директ'
    if re.search(r'google', utm_source, re.IGNORECASE) and re.search(r'cpc', utm_medium, re.IGNORECASE):
        return 'Google Ads'
    if traffic_source == 'Search engine traffic' and utm_source is None and utm_medium is None:
        return 'Поисковые системы'
    if re.search(r'vk_ads|vk_reklama|vk$', utm_source, re.IGNORECASE):
        return 'Реклама в соц.сетях'
    if re.search(r'фид|домклик', calltracking, re.IGNORECASE):
        return 'Базы недвижимости'
    return None
