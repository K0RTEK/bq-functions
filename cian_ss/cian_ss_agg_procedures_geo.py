import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def geo(campaign_name, ad_name, campaign_id):
    campaign_name = is_none(campaign_name)
    ad_name = is_none(ad_name)
    campaign_id = is_none(campaign_id)
    if re.search(r'^msk|_msk_|_msk$', campaign_name) or re.search(r'^msk|_msk_|_msk$', ad_name):
        return 'Москва'
    elif re.search(r'^mskmo|_mskmo_|_mskmo$', campaign_name) or re.search(r'^mskmo|_mskmo_|_mskmo$', ad_name):
        return 'Москва'
    # Other regions follow the same logic
    else:
        return "geo - NaN"