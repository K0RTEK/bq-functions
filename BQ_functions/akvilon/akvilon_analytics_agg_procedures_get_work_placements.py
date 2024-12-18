import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_work_placements(date, utm_source, utm_medium, utm_campaign, utm_content, utm_term, ct_campaign_name):
    utm_source = is_none(utm_source)
    utm_medium = is_none(utm_medium)
    utm_campaign = is_none(utm_campaign)
    utm_content = is_none(utm_content)
    utm_term = is_none(utm_term)
    ct_campaign_name = is_none(ct_campaign_name)
    if re.search(r'контекстная реклама', ct_campaign_name.strip()) and re.search(r'яндекс директ', ct_campaign_name.strip()):
        return 'Яндекс Директ'
    elif utm_source == 'yandex' and utm_medium == 'cpc':
        return 'Яндекс Директ'
    return None
