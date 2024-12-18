import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_banner_id(date, utm_source, utm_medium, utm_campaign, utm_content, utm_term):
    utm_source = is_none(utm_source)
    utm_medium = is_none(utm_medium)
    utm_campaign = is_none(utm_campaign)
    utm_content = is_none(utm_content)
    utm_term = is_none(utm_term)
    if utm_source is None:
        return re.search(r'\(M-(\d+)\)$', utm_content).group(1) if re.search(r'\(M-(\d+)\)$', utm_content) else None
    return next((match for pattern in [
        r'\|b:(\d+)\|', r'\|aid\|(\d+)', r'\|aid:(\d+)', r'%7cb:(\d+)%7c', r'%7caid%7c(\d+)%7c']
        if (match := re.search(pattern, utm_content))), None)