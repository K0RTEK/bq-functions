import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_additions(id_type, parameter):
    parameter = is_none(parameter)
    id_type = is_none(id_type)
    if id_type in ['ad_id','adid'] and re.search(r'adid:([0-9]+)', parameter):
        return re.search(r'adid:([0-9]+)', parameter).group(1)
    elif id_type in ['ad_id','adid'] and re.search(r'[0-9]+', parameter) and not re.search(r'[^0-9]', parameter):
        return re.search(r'[0-9]+', parameter).group(0)
    else:
        return ''