import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_ad_id(source_medium, utm_campaign, utm_content, utm_term):
    source_medium = is_none(source_medium)
    utm_campaign = is_none(utm_campaign)
    utm_content = is_none(utm_content)
    utm_term = is_none(utm_term)
    if re.search(r'mytarget', source_medium):
        return re.search(r'[0-9]{6,}', utm_term).group(0)
    elif re.search(r'vk ', source_medium):
        return re.search(r'[0-9]{6,}', utm_term).group(0)
    elif re.search(r'vkr', source_medium):
        return re.search(r'[0-9]{6,}', utm_term).group(0)
    elif re.search(r'yandex / cpc', source_medium):
        return re.search(r'ad:([0-9]+)', utm_content).group(1)
    else:
        return 'NaN'