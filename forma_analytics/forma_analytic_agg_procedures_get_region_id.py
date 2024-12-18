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
    if source == 'yandex' and medium == 'cpc':
        match = re.search(r'reg\|([0-9]+)', content)
        if match:
            return match.group(1)
    return None