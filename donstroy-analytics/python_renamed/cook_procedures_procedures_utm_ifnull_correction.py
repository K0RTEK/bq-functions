import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def utm_ifnull_correction(utm):
    utm = is_none(utm)
    return '' if utm in ('None', None) else utm.strip()