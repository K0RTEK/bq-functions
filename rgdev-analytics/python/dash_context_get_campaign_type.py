import re
import datetime as dt

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def classify_campaign(campaign_name, date):

    campaign_name = is_none(campaign_name)
    if re.search(r'mkb', campaign_name, re.IGNORECASE):
        return 'МКБ'
    elif re.search(r'_s_.*brand_development', campaign_name, re.IGNORECASE):
        return 'Поиск_бренд застройщика'
    elif re.search(r'_s_.*brand', campaign_name, re.IGNORECASE):
        return 'Поиск_бренд'
    elif re.search(r'_s_.*remarketing', campaign_name, re.IGNORECASE):
        return 'Поиск_ретаргетинг'
    elif re.search(r'_s_.*convert', campaign_name, re.IGNORECASE):
        return 'Поиск_общие'
    elif re.search(r'_s_.*geo', campaign_name, re.IGNORECASE):
        return 'Поиск_Гео'
    elif re.search(r'_mk_', campaign_name, re.IGNORECASE):
        return 'Мастер кампаний'
    elif re.search(r'_n_.*retargeting', campaign_name, re.IGNORECASE):
        return 'РСЯ_Ретаргетинг'
    elif re.search(r'_n_.*smart_banner', campaign_name, re.IGNORECASE):
        return 'Смартбаннеры'
    elif re.search(r'_n_|_epk_', campaign_name, re.IGNORECASE):
        return 'РСЯ'
    elif re.search(r'quiz', campaign_name, re.IGNORECASE):
        return 'Квиз'

    return None