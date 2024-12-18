import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_campaign_object(date, *parameters):
    parameters = [is_none(x) for x in parameters]
    if any(x in parameters for x in ['63803', '96021540', 'mangazeya-na-rechnom-mg', 'rechnoi']):
        return ' '
    elif any(re.search(r'на\.речном|na\.rechnom', x) for x in parameters):
        return ' '
    else:
        return None