import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def campaign_types(campaign_name: str) -> str:
    campaign_name = is_none(campaign_name)

    if re.search(r'magazin', campaign_name):
        return 'Magazin'
    elif re.search(r'chat-landing', campaign_name):
        return 'Chat-landing'
    elif re.search(r'chats|wa-tg|wa|tg', campaign_name):
        return 'Chats'
    elif re.search(r'clips|klips', campaign_name):
        return 'Clips'
    elif re.search(r'mp', campaign_name) and not re.search(r'[a-z-]+mp|mp[a-z-]+', campaign_name):
        return 'Market-platform'
    elif re.search(r'le.ds|leadads|lead-ads', campaign_name):
        return 'Leadads'
    elif re.search(r'traf|dinrem', campaign_name):
        return 'Traffic'
    elif re.search(r'reach', campaign_name):
        return 'Reach'
    elif re.search(r'quiz', campaign_name):
        return 'Quiz'
    elif campaign_name == 'NaN':
        return 'Не опознается'
    else:
        return 'NaN'
