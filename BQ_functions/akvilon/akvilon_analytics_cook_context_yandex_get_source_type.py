import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_source_type(date, utm_source, utm_medium, utm_campaign, utm_content, utm_term):
    utm_source = is_none(utm_source)
    utm_medium = is_none(utm_medium)
    utm_campaign = is_none(utm_campaign)
    utm_content = is_none(utm_content)
    utm_term = is_none(utm_term)
    if re.search(r'src\|context|st\|context', utm_term) or \
       re.search(r'src\|context|st\|context', utm_content):
        return 'ad_network'
    elif re.search(r'src\|search|st\|search', utm_term) or \
         re.search(r'src\|search|st\|search', utm_content):
        return 'search'