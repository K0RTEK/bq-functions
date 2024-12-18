import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_device(date, utm_source, utm_medium, utm_campaign, utm_content, utm_term):
    utm_source = is_none(utm_source)
    utm_medium = is_none(utm_medium)
    utm_campaign = is_none(utm_campaign)
    utm_content = is_none(utm_content)
    utm_term = is_none(utm_term)
    if re.search(r'dt:m|dvc:m', utm_term) or re.search(r'dt:m|dvc:m', utm_content):
        return 'mobile'
    elif re.search(r'dt:t|dvc:t', utm_term) or re.search(r'dt:t|dvc:t', utm_content):
        return 'tablet'
    elif re.search(r'dt:c|desktop', utm_term) or re.search(r'dt:c|desktop', utm_content):
        return 'desktop'
    return None