import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def creo(campaign_name, ad_name, campaign_id):
    campaign_name = is_none(campaign_name)
    ad_name = is_none(ad_name)
    campaign_id = is_none(campaign_id)

    if re.search(r'cr-[a-zA-Z0-9_.+-]+$', campaign_name):
        return re.split(r'_', re.search(r'(cr-[a-zA-Z0-9_.+-]+)$', campaign_name).group(0))[0]
    elif re.search(r'cr-[a-zA-Z0-9_.+-]+$', ad_name):
        return re.split(r'_', re.search(r'(cr-[a-zA-Z0-9_.+-]+)$', ad_name).group(0))[0]
    elif re.search(r'cr:[a-zA-Z0-9_.+-]+$', campaign_name):
        return re.split(r'_', re.search(r'(cr:[a-zA-Z0-9_.+-]+)$', campaign_name).group(0))[0]
    elif re.search(r'cr:[a-zA-Z0-9_.+-]+$', ad_name):
        return re.split(r'_', re.search(r'(cr:[a-zA-Z0-9_.+-]+)$', ad_name).group(0))[0]
    elif re.search(r'_feed-', campaign_name):
        return 'Фид'
    else:
        return "creo - NaN"