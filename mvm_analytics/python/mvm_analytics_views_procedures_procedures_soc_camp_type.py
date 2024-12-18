import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def soc_camp_type(campaign):
    campaign = is_none(campaign)
    if not re.search(r'mg_', campaign):
        return ' '
    elif re.search(r'_flight_', campaign):
        return 'Flight'
    elif re.search(r'_pf_', campaign):
        return 'Performance'
    elif re.search(r'_md_', campaign):
        return 'Media'
    else:
        return 'NaN - ' + campaign