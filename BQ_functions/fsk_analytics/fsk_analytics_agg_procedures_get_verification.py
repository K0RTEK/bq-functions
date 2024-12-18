import datetime as dt

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_verification(date, verify_itog, verify_itog_new):
    verify_itog = is_none(verify_itog)
    verify_itog_new = is_none(verify_itog_new)
    if date < dt.datetime(2022, 10, 1) and verify_itog == 'ЦЕЛЕВОЙ':
        return True
    elif date >= dt.datetime(2022, 10, 1) and (verify_itog_new == 'ЦЕЛЕВОЙ' or verify_itog_new == 'УСЛОВНО ЦЕЛЕВОЙ'):
        return True
    return False