import re
import datetime as dt

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_campaign_name_id(data_group, campaign):
    data_group = is_none(data_group)
    campaign = is_none(campaign)
    if data_group == 'campaign_name':
        if not re.search(r'cn|сn', campaign) and re.search(r'cid|сid', campaign):
            return None
        else:
            return re.sub(r'\|.*', '', re.sub(r'[0-9.]{6,}_', '', re.sub(r'.*(cn(:|%))', '', campaign)))
    elif data_group == 'campaign_id':
        return re.sub(r'\|.*', '', re.sub(r'[a-zа-я._]+', '', re.sub(r'.*(cid(:|%))', '', campaign)))