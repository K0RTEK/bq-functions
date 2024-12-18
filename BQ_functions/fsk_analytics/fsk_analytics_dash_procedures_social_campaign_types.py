import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def campaign_types(campaign_global):
    campaign_global = is_none(campaign_global)
    if re.search(r'magazin', campaign_global):
        return 'Magazin'
    elif re.search(r'chat-landing', campaign_global):
       return 'Chat-landing'
    elif re.search(r'chats|wa-tg|wa|tg', campaign_global):
       return 'Chats'
    elif re.search(r'clips|klips', campaign_global):
       return 'Clips'
    elif re.search(r'mp', campaign_global) and not re.search(r'[a-z-]+mp|mp[a-z-]+', campaign_global):
       return 'Market-platform'
    elif re.search(r'le.ds|leadads|lead-ads', campaign_global):
       return 'Leadads'
    elif re.search(r'traf|dinrem', campaign_global):
       return 'Traffic'
    elif re.search(r'reach', campaign_global):
       return 'Reach'
    elif re.search(r'quiz', campaign_global):
        return 'Quiz'
    return None