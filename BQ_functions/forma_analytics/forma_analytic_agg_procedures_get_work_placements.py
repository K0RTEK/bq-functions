import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_work_placements(date, source, medium, campaign, content, term, ct_campaign_name):
    source = is_none(source)
    medium = is_none(medium)
    campaign = is_none(campaign)
    content = is_none(content)
    term = is_none(term)
    ct_campaign_name = is_none(ct_campaign_name)
    if re.search(r'контекстная реклама', ct_campaign_name) and re.search(r'яндекс.директ', ct_campaign_name):
        return 'Яндекс Директ'
    elif source == 'yandex' and medium == 'cpc':
        return 'Яндекс Директ'
    return None