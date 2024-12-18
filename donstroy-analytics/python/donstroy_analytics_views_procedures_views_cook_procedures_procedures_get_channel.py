import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()


def get_channel(calltracking, utm_source, utm_medium, utm_campaign, utm_content, utm_term, traffic_source):
    calltracking = is_none(calltracking)
    utm_source = is_none(utm_source)
    utm_medium = is_none(utm_medium)
    utm_campaign = is_none(utm_campaign)
    utm_content = is_none(utm_content)
    utm_term = is_none(utm_term)
    traffic_source = is_none(traffic_source)

    if re.search(r'лидогенераторы', calltracking):
        return "Лидогенерация"
    elif (re.search(r'yandex', utm_source) and re.search(r'cpc|cpm', utm_medium)) or re.search(r'яндекс(.|..)директ', calltracking):
        return 'Яндекс Директ'
    elif (re.search(r'google', utm_source)
          and re.search(r'cpc', utm_medium)
          and (re.search(r'mg_', utm_campaign)
               or re.search(r'mg_', utm_content)
               or re.search(r'mg_', utm_term))) or (re.search(r'mg|sm', calltracking)
                                                    and re.search(r'google|гугл', calltracking)):
        return 'Google Ads'
    elif traffic_source == 'search engine traffic' and utm_source is None and utm_medium is None:
        return 'Поисковые системы'
    elif traffic_source == 'link traffic' and utm_source is None and utm_medium is None:
        return 'Переходы по ссылкам'
    elif (re.search(r'vk_ads|vk_reklama', utm_source)
          or re.search(r'_vk$|^vk$|^vk_', utm_source)
          or re.search(r'mytarget|_mt$', utm_source)
          or re.search(r'facebook|fb_ig|inst|_fb$', utm_source)
          or re.search(r'tiktok', utm_source)
          or re.search(r'telegram', utm_source)) and utm_medium in ('cpc','cpm'):
        return 'Реклама в соц.сетях'
    else:
        return ''