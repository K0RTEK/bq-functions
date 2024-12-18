def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def utm_ifnull_correction(utm):
    utm = is_none(utm)
    if utm == 'None' or utm is None:
        return ''
    return utm.lower().strip()