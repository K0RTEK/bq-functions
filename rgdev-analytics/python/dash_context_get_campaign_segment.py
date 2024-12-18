import re
import datetime as dt

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()


def classify_campaign(campaign_name, date):

    campaign_name = is_none(campaign_name)
    if re.search(r'brand', campaign_name, re.IGNORECASE):
        return 'Бренд'
    elif re.search(r'retargeting|remarketing|smart_banner', campaign_name, re.IGNORECASE):
        return 'Ретаргетинг'
    elif re.search(r'cpa|autotargeting|convert|class', campaign_name, re.IGNORECASE):
        return 'Общие'
    elif re.search(r'geo', campaign_name, re.IGNORECASE):
        return 'ГЕО'
    elif re.search(r'competitors|konkurenty', campaign_name, re.IGNORECASE):
        return 'Конкуренты'

    return None
