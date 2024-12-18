import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_ad_id(date, source, medium, campaign, content, term):
    source = is_none(source)
    medium = is_none(medium)
    campaign = is_none(campaign)
    content = is_none(content)
    term = is_none(term)
    if source == 'yandex' and medium == 'cpc':
        return re.search(r'aid:([0-9]+)', content).group(1)
    elif source == 'mt' and medium == 'cpc' and not re.search(r'[^0-9]+', content):
        return re.search(r'[0-9]+', content).group(0)
    elif source == 'mt' and medium == 'cpc':
        return re.search(r'aid.([0-9]+)', content).group(1)
    elif source in ('vk', 'vkontakte') and medium == 'cpc' and not re.search(r'[^0-9]+', content):
        return re.search(r'[0-9]+', content).group(0)
    elif source in ('vk', 'vkontakte') and medium == 'cpc':
        return re.search(r'aid.([0-9]+)', content).group(1)
    elif source == 'vkr' and medium == 'cpc' and not re.search(r'[^0-9]+', content):
        return re.search(r'[0-9]+', content).group(0)
    elif source == 'vkr' and medium == 'cpc':
        return re.search(r'aid.([0-9]+)', re.sub('-', '', content)).group(1)
    else:
        return 'NaN'