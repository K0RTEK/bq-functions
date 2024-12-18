import datetime as dt

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def mob_get_cpo(date, os_type):
    os_type = is_none(os_type)
    if date < dt.date(2024, 5, 1):
        if os_type == 'Android':
            return 5714
        elif os_type == 'IOS':
            return 5556
    elif date >= '2024-05-01':
        return 5636
