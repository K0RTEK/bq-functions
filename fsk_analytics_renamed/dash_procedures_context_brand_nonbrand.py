import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def brand_nonbrand(campaign_global):
    campaign_global = is_none(campaign_global)
    if re.search(r'brand|контекст бренд', campaign_global) and not re.search(r'_net_|сеть', campaign_global):
        return 'Brand'
    return 'Non-Brand'