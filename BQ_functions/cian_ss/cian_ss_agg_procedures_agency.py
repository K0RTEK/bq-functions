import re
import datetime as dt

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def agency(date, campaign_name, ad_name, campaign_id):
    campaign_name = is_none(campaign_name)
    ad_name = is_none(ad_name)
    campaign_id = is_none(campaign_id)
    if date < dt.datetime(2024, 4, 15):
        return None
    elif re.search(r'(^|_)mgcom(_|$)', campaign_name):
        return 'mgcom'
    elif re.search(r'(^|_)rw(_|$)', ad_name):
        return 'realweb'
    else:
        return "agency - NaN"