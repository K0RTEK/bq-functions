import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_lead_type(date, campaign_calltracking, utm_source, utm_medium, utm_campaign, campaign_cabinet):
    utm_source = is_none(utm_source)
    utm_medium = is_none(utm_medium)
    utm_campaign = is_none(utm_campaign)
    campaign_cabinet = is_none(campaign_cabinet)
    campaign_calltracking = is_none(campaign_calltracking)

    if utm_source in ['google', 'yandex'] and utm_medium == 'cpc':
        if re.search(r'quiz', utm_campaign) or re.search(r'quiz', campaign_cabinet) or re.search(r'яндекс директ.*quiz', campaign_calltracking):
            return 'Quiz'
        return 'Traffic'
    if re.search(r'quiz', utm_campaign) or re.search(r'quiz', campaign_cabinet) or re.search(r'quiz', campaign_calltracking):
        return 'Quiz'
    if re.search(r'lead', utm_campaign) or re.search(r'lead', campaign_calltracking):
        return 'Leadads'
    return 'Traffic'