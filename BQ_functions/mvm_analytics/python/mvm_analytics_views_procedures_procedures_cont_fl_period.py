import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def cont_fl_period(campaign):
    campaign = is_none(campaign)
    regex_list = [
        r'(..\...-..\...\...)',
        r'(..\...\.....-..\...\.....)',
        r'(..\...-..\...)',
        r'(..\...-.\...\...)'
    ]
    for regex in regex_list:
        match = re.search(regex, campaign)
        if match:
            return match.group(0)
    return 'NaN'