import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_agency(date, smth):
    smth = is_none(smth)
    if re.search(r'^mg', smth.strip()):
        return variables_mg_var_agency_mgcom()
    else:
        return 'Not MG'