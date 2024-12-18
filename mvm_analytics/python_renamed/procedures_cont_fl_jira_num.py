import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def cont_fl_jira_num(campaign):
    campaign = is_none(campaign)
    return next(
        (re.search(pattern, campaign).group(1) for pattern in [
            r'_([0-9]+)_.*\...-..\...\...',
            r'_([0-9]+)_.*\...-.\...\...',
            r'_([0-9]+)_.*-.*'
        ] if re.search(pattern, campaign) is not None),
        'NaN'
    )