import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_geo_id(date, utm_source, utm_medium, utm_campaign, utm_content, utm_term):
    utm_source = is_none(utm_source)
    utm_medium = is_none(utm_medium)
    utm_campaign = is_none(utm_campaign)
    utm_content = is_none(utm_content)
    utm_term = is_none(utm_term)

    if utm_source == 'yandex' and utm_medium == 'cpc':
        match = re.search(r'geoid:([0-9]+)', utm_content)
        if match:
            return match.group(1)
    return 'NaN'