import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def soc_traf_type(campaign):
    campaign = is_none(campaign)
    if not re.search(r'mg_', campaign):
        return ' '
    elif re.search(r'_flight_', campaign):
        return 'Flight'
    elif re.search(r'_dir_', campaign):
        return ' '
    elif re.search(r'_dnmc_', campaign):
        return ' '
    elif re.search(r'_sttc_', campaign):
        return ' '
    else:
        return 'NaN - ' + campaign