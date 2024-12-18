import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_position_type(date, utm_source, utm_medium, utm_campaign, utm_content, utm_term):
    utm_source = is_none(utm_source)
    utm_medium = is_none(utm_medium)
    utm_campaign = is_none(utm_campaign)
    utm_content = is_none(utm_content)
    utm_term = is_none(utm_term)
    return next((match for pattern in [r'\|pt:(\w+)\|', r'%7Cpt:(\w+)%7C'] if (match := re.search(pattern, utm_content))), None)
