import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def targeting(campaign_name, ad_name, campaign_id):
    campaign_name = is_none(campaign_name)
    ad_name = is_none(ad_name)
    campaign_id = is_none(campaign_id)
    for field in [campaign_name, ad_name]:
        if re.search(r'ta-[a-zA-Z0-9_.+-]+$', field):
            return re.split(r'_', re.search(r'(ta-[a-zA-Z0-9_.+-]+)$', field).group(1))[0]
        elif re.search(r'ta:[a-zA-Z0-9_.+-]+$', field):
            return re.split(r'_', re.search(r'(ta:[a-zA-Z0-9_.+-]+)$', field).group(1))[0]
    return "targeting - NaN"