import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def cont_fl_ecounit(campaign):
    campaign = is_none(campaign)
    if re.search(r'_e-p_', campaign):
        return ' '
    elif re.search(r'_kt_', campaign):
        return ' '
    elif re.search(r'_mb_', campaign):
        return '  '
    elif re.search(r'_h-o_', campaign):
        return '   '
    elif re.search(r'_c-s_|_c_s_', campaign):
        return '   '
    elif re.search(r'_h-c_', campaign):
        return '  '
    else:
        return 'NaN'