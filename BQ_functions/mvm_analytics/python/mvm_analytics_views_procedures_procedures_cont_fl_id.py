import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()


def cont_fl_id(campaign):
    campaign = is_none(campaign).lower()

    regex_patterns = [
        r'..\...-..\...\..._([0-9]+)',
        r'..\...-..\...\....._([0-9]+)',
        r'..\...\.....-..\...\....._([0-9]+)',
        r'..\...-..\..._([0-9]+)',
        r'..\..._..\..._([0-9]+)',
        r'..\...-.\...\..._([0-9]+)',
        r'..\...-..\...\....*_([0-9]+)',
        r'..\...-..\....*_([0-9]+)',
        r'..\...\.....-..\...\....*_([0-9]+)',
        r'..\...-.\...\....*_([0-9]+)',
        r'..\...\... - ..\...\..._([0-9]+)',
        r'..\... - ..\..._([0-9]+)',
        r'..\...\...-..\...\..._([0-9]+)',
        r'..\...-.\..._([0-9]+)',
        r'..\....-.\..._([0-9]+)',
        r'..\...\...-..\...\..._([0-9]+)',
        r'[0-9]{6,6}_[0-9]{6,6}_([0-9]+)',
        r'[0-9]{4,4}_[0-9]{4,4}_([0-9]+)'
    ]

    for pattern in regex_patterns:
        match = re.search(pattern, campaign)
        if match:
            return match.group(1)

    return 'NaN'
