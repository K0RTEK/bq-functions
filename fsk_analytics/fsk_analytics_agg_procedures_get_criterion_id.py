import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_criterion_id(date, source, medium, campaign, content, term):
    source = is_none(source)
    medium = is_none(medium)
    campaign = is_none(campaign)
    content = is_none(content)
    term = is_none(term)

    if campaign.startswith('mg_ya_') and source == 'yandex' and medium == 'cpc':
        content_lower = content.lower()
        if 'kw_id:' in content_lower:
            return re.search(r'kw_id:([0-9]+)', content_lower).group(1)
        elif 'gid|' in content_lower:
            return re.search(r'gid\|([0-9]+)', content_lower).group(1)
        elif 'b:' in content_lower:
            return re.search(r'b:([0-9]+)', content_lower).group(1)
        elif 'aid|' in content_lower:
            return re.search(r'aid\|([0-9]+)', content_lower).group(1)
    return None