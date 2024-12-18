import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()
    
def get_format(date, ct_source, ct_medium, crm_advertising_source, utm_source, utm_medium, utm_campaign, utm_content, utm_term):
    utm_source = is_none(utm_source)
    utm_medium = is_none(utm_medium)
    utm_campaign = is_none(utm_campaign)
    utm_content = is_none(utm_content)
    crm_advertising_source = is_none(crm_advertising_source)
    utm_term = is_none(utm_term)
    ct_medium = is_none(ct_medium)
    ct_source = is_none(ct_source)

    if re.search(r'tgb', utm_term, re.IGNORECASE) or re.search(r'tgb', utm_source, re.IGNORECASE):
        return ' '
    elif re.search(r'banner', utm_term, re.IGNORECASE) or re.search(r'banner', utm_source, re.IGNORECASE):
        return ' '
    elif re.search(r'spec', utm_term, re.IGNORECASE) or re.search(r'spec', utm_source, re.IGNORECASE):
        return ' '
    elif re.search(r'pin', utm_term, re.IGNORECASE):
        return 'PIN'
    elif re.search(r'poi', utm_term, re.IGNORECASE):
        return 'POI'
    elif re.search(r'billboard', utm_term, re.IGNORECASE):
        return ' '
    elif re.search(r'snippet', utm_term, re.IGNORECASE):
        return ' '
    elif re.search(r'push', utm_term, re.IGNORECASE) or re.search(r'push', utm_medium, re.IGNORECASE):
        return ' '
    elif re.search(r'kontekstno', utm_term, re.IGNORECASE):
        return ' '
    elif re.search(r'statika', utm_term, re.IGNORECASE):
        return ' '
    elif re.search(r'brendiro', utm_term, re.IGNORECASE):
        return ' '
    else:
        return 'NaN'