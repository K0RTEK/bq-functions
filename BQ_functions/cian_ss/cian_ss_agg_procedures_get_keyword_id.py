import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_keyword_id(source_medium, utm_campaign, utm_content, utm_term):
    source_medium = is_none(source_medium)
    utm_campaign = is_none(utm_campaign)
    utm_content = is_none(utm_content)
    utm_term = is_none(utm_term)
    if re.search(r'yandex / cpc', source_medium):
        match = re.search(r'kw:([0-9-]+)', utm_content)
        return match.group(1) if match else 'NaN'
    return 'NaN'