import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_targeting(campaign_name):
    campaign_name_lower = is_none(campaign_name)
    targeting = re.search(r'ta:[^_]+', campaign_name_lower)

    if targeting:
        return targeting.group(0)
    else:
        return 'NaN'