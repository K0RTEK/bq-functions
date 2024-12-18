def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def string_normalization(str_field):
    str_field = is_none(str_field)
    if str_field is None or str_field.strip() in ['', '-']:
        return None
    return str_field.strip()
