import re
import datetime as dt

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_call_type(date, attributes, tags, verify_itog, verify_itog_new):
    attributes = is_none(attributes)
    tags = is_none(tags)
    verify_itog = is_none(verify_itog)
    verify_itog_new = is_none(verify_itog_new)

    return ''.join([
        'quality,' if re.search('quality', attributes) else '',
        'target' if re.search('гео', tags) and re.search('цена', tags) and re.search('ца', tags) else '',
        ',vco' if (date < dt.date(2022, 10, 1) and verify_itog == 'ЦЕЛЕВОЙ') or (date >= dt.date(2022, 10, 1) and verify_itog_new in ['ЦЕЛЕВОЙ', 'УСЛОВНО ЦЕЛЕВОЙ']) else ''
    ])