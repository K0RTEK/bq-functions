import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_campaign_id(date, source, medium, campaign, content, term):
    date = is_none(date)
    source = is_none(source)
    medium = is_none(medium)
    campaign = is_none(campaign)
    content = is_none(content)
    term = is_none(term)

    if source == 'yandex' and medium == 'cpc' and re.search(r'cid:', content):
        return re.search(r'cid:([0-9]+)', content).group(1)
    elif source == 'yandex' and medium == 'cpc' and re.search(r'cid:', campaign):
        return re.search(r'cid:([0-9]+)', campaign).group(1)
    elif source == 'yandex' and medium == 'cpc' and re.search(r'\|[0-9]{5,}', campaign):
        return re.search(r'\|([0-9]{5,})', campaign).group(1)
    elif source == 'mt' and medium == 'cpc':
        return re.search(r'cid\.([0-9]+)', content).group(1)
    elif source in ('vk', 'vkontakte') and medium == 'cpc':
        return re.search(r'cid\.([0-9]+)', content).group(1)
    else:
        return 'NaN'