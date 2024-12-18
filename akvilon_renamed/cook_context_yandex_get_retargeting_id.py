import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_retargeting_id(date, utm_source, utm_medium, utm_campaign, utm_content, utm_term):
    return re.search(r're:(\d+)\|', utm_content) or re.search(r're:(\d+)\|', utm_term) or \
           "unknown"