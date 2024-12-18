import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_banner_id(utm_content):
    utm_content = is_none(utm_content)
    if 'adid:' in utm_content:
        return re.search(r'adid:([0-9]+)', utm_content).group(1)
    elif '"adid":' in utm_content:
        return re.search(r'"adid":([0-9]+)', utm_content).group(1)
    elif re.search(r'^[0-9]+$', utm_content):
        return re.search(r'[0-9]+', utm_content).group(0)
    else:
        return None