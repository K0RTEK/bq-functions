import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def b2segment(campaign_name, ad_name, campaign_id):
    campaign_name = is_none(campaign_name)
    ad_name = is_none(ad_name)
    campaign_id = is_none(campaign_id)
    if re.search(r'^b2c|_b2c_|_b2c$', campaign_name) or re.search(r'^b2c|_b2c_|_b2c$', ad_name):
        return 'b2c'
    elif re.search(r'^b2b|_b2b_|_b2b$', campaign_name) or re.search(r'^b2b|_b2b_|_b2b$', ad_name):
        return 'b2b'
    else:
        return "b2segment - NaN"