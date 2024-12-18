import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def forma_analytic_agg_procedures_get_device(date, source, medium, campaign, content, term):
    source = is_none(source)
    medium = is_none(medium)
    campaign = is_none(campaign)
    content = is_none(content)
    term = is_none(term)
    if source == 'yandex' and medium == 'cpc':
        match = re.search(r'dvc:([^|]+)', content)
        if match:
            return match.group(1)
    return None