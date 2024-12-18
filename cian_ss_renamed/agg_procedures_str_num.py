def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def str_num(numer):
    numer = is_none(numer)
    cleaned_numer = numer.strip()
    if cleaned_numer in ['', '0', ',0', ',00', '0,00', '0,0', '.0', '.00', '0.00', '0.0']:
        return None
    return float(cleaned_numer.replace(',', '.'))