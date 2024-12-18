import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_campaign_name(date, source, medium, campaign, content, term):
    if is_none(source) == 'yandex' and is_none(medium) == 'cpc':
        if re.search(r'cn:', is_none(campaign)):
            return re.search(r'cn:([^|]+)', is_none(campaign)).group(1)
        elif re.search(r'\|', is_none(campaign)):
            return re.search(r'[^|]+', is_none(campaign)).group(0)
    return is_none(campaign)