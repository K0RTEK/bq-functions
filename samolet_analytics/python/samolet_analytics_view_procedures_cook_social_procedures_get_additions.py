import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_additions(date, parameter):
    parameter = is_none(parameter)
    if re.search(r'mg_|clprt|_rto_', parameter):
        return '-'
    elif re.search(r'samolet_msk_traf_dinrem|cl-bus_msk_traf_dinrem', parameter):
        return '-'
    else:
        return ' '