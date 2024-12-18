import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_cpa(string_param):
    string_param = is_none(string_param)
    patterns = {
        'Atommedia': r'atommedia',
        'AurumRealty': r'aurumrealty',
        'Call of Leads': r'call(.|)of(.|)leads',
        # Add more patterns as per the original logic
    }

    for name, pattern in patterns.items():
        if re.search(pattern, string_param, re.IGNORECASE):
            return name
    return None
