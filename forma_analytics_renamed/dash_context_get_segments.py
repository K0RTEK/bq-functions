import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_segments(date, campaign_name):
    campaign_name = is_none(campaign_name)
    if re.search(r'визитка.*бренд', campaign_name):
        return ['Бренд', 'Бренд', 'Визитка Бренд', 'Поиск']
    elif re.search(r'визитка.*не(|.*)бренд', campaign_name):
        return ['НеБренд', 'НеБренд', 'Визитка НеБренд', 'Поиск']
    else:
        return None