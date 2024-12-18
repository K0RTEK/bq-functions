import re
import datetime as dt

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def context_campaign_type(campaign):
    campaign = is_none(campaign)
    if re.search(r'brand', campaign):
        return 'Брендовая'
    elif re.search(r'mkb', campaign):
        return 'МКБ'
    elif re.search(r'vendor', campaign):
        return 'Вендорная'
    elif re.search(r'model', campaign):
        return 'Модельная'
    elif re.search(r'dsa', campaign):
        return 'ДСА'
    elif re.search(r'retargeting', campaign):
        return 'Ретаргетинг'
    elif re.search(r'smartbanner', campaign):
        return 'Смартбаннеры'
    elif re.search(r'tov_campaign_test1', campaign):
        return 'Товарная кампания (пн-чт)'
    elif re.search(r'tov_campaign_test2', campaign):
        return 'Товарная кампания (пт-вс)'
    elif re.search(r'tov', campaign):
        return 'Товарная'
    elif re.search(r'perfomance', campaign):
        return 'ЕПК'
    elif re.search(r'general', campaign):
        return 'General рк'
    elif re.search(r'elektrosamokaty_xiaomi', campaign):
        return 'РК по самокатам'
    elif re.search(r'pylesosy_xiaomi', campaign):
        return 'РК по пылесосам'
    else:
        return 'NaN'