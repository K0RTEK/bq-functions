import re
import datetime as dt

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_source_type(date, traffic_source, utm_source, utm_medium, source_engine, calltracking):
    utm_source = is_none(utm_source)
    utm_medium = is_none(utm_medium)
    source_engine = is_none(source_engine)
    calltracking = is_none(calltracking)
    if (re.search(r'yd', utm_source) and re.search(r'cpc', utm_medium)) or (source_engine == 'yandex: direct' and utm_source is None) or re.search(r'директ|direct|квиз мих', calltracking) or (re.search(r'посетители без рекламной кампании|прямые заходы', calltracking) and re.search(r'yd', utm_source)):
        return 'Яндекс Директ'
    elif (re.search(r'google', utm_source) and re.search(r'cpc', utm_medium)) or (re.search(r'mg|sm', calltracking) and re.search(r'google|гугл', calltracking)):
        return 'Google Ads'
    elif traffic_source == 'Search engine traffic' and utm_source is None and utm_medium is None:
        return 'Поисковые системы'
    elif traffic_source == 'Link traffic' and utm_source is None and utm_medium is None:
        return 'Переходы по ссылкам'
    elif re.search(r'like estate|likeestate|румбери|callexchange|лидогенерация', calltracking) and not re.search(r'сian.ru Лидогенерация', calltracking):
        return 'CPA'
    elif (re.search(r'vk_ads|vk_reklama', utm_source) or re.search(r'_vk$|^vk$|^vk_', utm_source) or re.search(r'mytarget|_mt$', utm_source) or re.search(r'facebook|fb_ig|inst|_fb$', utm_source) or re.search(r'tiktok', utm_source) or re.search(r'telegram', utm_source)) and utm_medium in ['cpc', 'cpm']:
        return 'Реклама в соц.сетях'
    else:
        return ''