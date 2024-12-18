import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_device(source_medium, utm_campaign, utm_content, utm_term):
    source_medium = is_none(source_medium)
    utm_campaign = is_none(utm_campaign)
    utm_content = is_none(utm_content)
    utm_term = is_none(utm_term)
    if re.search(r'yandex / cpc', source_medium):
        return re.search(r'dev:([a-z]+)', utm_content).group(1)
    else:
        return 'NaN'