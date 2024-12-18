import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_object(ct_campaign_name, source, medium, campaign, content, term, campaign_name):
    ct_campaign_name = is_none(ct_campaign_name)
    source = is_none(source)
    medium = is_none(medium)
    campaign = is_none(campaign)
    content = is_none(content)
    term = is_none(term)
    campaign_name = is_none(campaign_name)

    if re.search(r'republic', ct_campaign_name):
        return 'Republic'
    elif re.search(r'republic', campaign) or re.search(r'republic', campaign_name):
        return 'Republic'
    else:
        return 'Undefined Object'