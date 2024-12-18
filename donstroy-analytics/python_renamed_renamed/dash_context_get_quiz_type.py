import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def determine_source(campaign_name):
    campaign_name = is_none(campaign_name)
    if re.search(r'quiz\.pages', campaign_name):
        return 'Квиз Pages'
    elif re.search(r'quiz', campaign_name):
        return 'Квиз'
    else:
        return ''