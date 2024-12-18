import re
import datetime as dt

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_geo(channel, campaign, date):
    channel = is_none(channel)
    campaign = is_none(campaign)
    date = is_none(date)

    if channel == 'контекст':
        if re.search(r'_rf|perfomance', campaign):
            return 'РФ'
        else:
            return 'NaN'