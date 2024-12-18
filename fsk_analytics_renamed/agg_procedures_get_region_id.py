import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_region_id(date, source, medium, campaign, content, term):
    source = is_none(source)
    medium = is_none(medium)
    campaign = is_none(campaign)
    content = is_none(content)
    term = is_none(term)
    if campaign.startswith('mg_ya_') and source == 'yandex' and medium == 'cpc':
        region_id = re.search(r'geo:([^|]+)', content)
        if region_id:
            return region_id.group(1)
        return re.search(r'reg\|([^|]+)', content).group(1)
    return None