def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def str_num(numer):
    numer = is_none(numer)
    try:
        return float(numer.replace(",", ".").strip())
    except ValueError:
        return None
