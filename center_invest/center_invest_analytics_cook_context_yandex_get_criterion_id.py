import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_criterion_id(date, utm_source, utm_medium, utm_campaign, utm_content, utm_term):
    utm_source = is_none(utm_source)
    utm_medium = is_none(utm_medium)
    utm_campaign = is_none(utm_campaign)
    utm_content = is_none(utm_content)
    utm_term = is_none(utm_term)

    patterns = [
        r'\|kw_id:(\d+)\|', r'\|kwd-([^|]+)\|', r'kwd-(.*?)%', r':kwd-(.*?)\|',
        r'%7ckw_id:(.*?)%']
    return next((match for pattern in patterns if (match := re.search(pattern, utm_content))), None)
