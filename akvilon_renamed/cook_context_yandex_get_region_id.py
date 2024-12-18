import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_region_id(date, utm_source, utm_medium, utm_campaign, utm_content, utm_term):
    utm_source = is_none(utm_source)
    utm_medium = is_none(utm_medium)
    utm_campaign = is_none(utm_campaign)
    utm_content = is_none(utm_content)
    utm_term = is_none(utm_term)
    return re.search(r'\|reg:(\d+)[|$_]', utm_content) or re.search(r'\|reg:(\d+)[|$_]', utm_term) or \
           re.search(r'\|geo.(\d+)\|', utm_content) or re.search(r'\|geo.(\d+)\|', utm_term) or \
           "unknown"