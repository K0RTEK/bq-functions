import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_campaign_id(date, utm_source, utm_medium, utm_campaign, utm_content, utm_term):
    utm_source = is_none(utm_source)
    utm_medium = is_none(utm_medium)
    utm_campaign = is_none(utm_campaign)
    utm_content = is_none(utm_content)
    utm_term = is_none(utm_term)
    if utm_source is None:
        return re.search(r'\(N-(\d+)\)$', utm_campaign).group(1) if re.search(r'\(N-(\d+)\)$', utm_campaign) else None
    patterns = [
        r'cid:(\d+)\|', r'\|cid\|(\d+)', r'\%7Ccid:(\d+)\%7c', r'cid:(\d+)\%7c',
        r'cid%7c(\d+)\%7c', r'\|cid:(\d+)', r'^(\d+)\|']
    return next((match for pattern in patterns if (match := re.search(pattern, utm_content))), None)
