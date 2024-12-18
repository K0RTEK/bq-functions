import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_format(campaign_name):
    campaign_name = is_none(campaign_name)

    if re.search(r'_leadform', campaign_name):
        return 'lead ads'
    elif re.search(r'_multi', campaign_name):
        return 'мультиформат'
    elif re.search(r'_carousel', campaign_name):
        return 'карусель'
    else:
        return 'NaN'