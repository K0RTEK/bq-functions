import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_creative(campaign_name, ad_name):
    campaign_name = is_none(campaign_name)
    ad_name = is_none(ad_name)
    if re.search(r'cr:[^_]+', ad_name):
        return re.search(r'cr:[^_]+', ad_name).group(0)
    elif re.search(r'cr:[^_]+', campaign_name):
        return re.search(r'cr:[^_]+', campaign_name).group(0)
    else:
        return 'NaN'