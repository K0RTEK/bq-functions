import re
import datetime as dt

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_campaign_name_id(data_group, campaign):
    campaign = is_none(campaign)

    if data_group == 'campaign_name':
        if not re.search(r'[a-zа-я]', campaign):
            return None
        elif re.search(r'cn%[0-9]+', campaign):
            return re.search(r'cn%.*3a(.*)', campaign).group(1)
        else:
            campaign = re.sub(r'[0-9.]{6,}', '', campaign)
            campaign = re.sub(r'\|.*', '', campaign)
            return campaign

    elif data_group == 'campaign_id':
        if re.search(r'cid:{campaign_id}', campaign):
            return None
        elif re.search(r'cid:', campaign):
            return re.search(r'cid:([0-9]+)', campaign).group(1)
        elif re.search(r'cid%', campaign):
            return re.search(r'([0-9]+)_cn', campaign).group(1)
        elif re.search(r'[0-9]{6,}', campaign):
            return re.search(r'[0-9]{6,}', campaign).group(0)
        elif not re.search(r'(cid|сid)(:|%)', campaign):
            return None