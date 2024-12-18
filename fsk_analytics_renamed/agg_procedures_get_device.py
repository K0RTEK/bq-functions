import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_device(date, source, medium, campaign, content, term):
    source = is_none(source)
    medium = is_none(medium)
    campaign = is_none(campaign)
    content = is_none(content)
    term = is_none(term)
    if campaign.startswith('mg_ya_') and source == 'yandex' and medium == 'cpc':
        content_lower = content.lower()
        if 'dt:' in content_lower:
            return re.search(r'dt:([^|]+)', content_lower).group(1)
        return re.search(r'dvc\|([^|]+)', content_lower).group(1)
    return None