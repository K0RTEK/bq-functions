def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def string_normalization(str_field):
    str_field = is_none(str_field)
    if str_field.strip() in ['', '-', None]:
        return None
    else:
        return str_field.strip()