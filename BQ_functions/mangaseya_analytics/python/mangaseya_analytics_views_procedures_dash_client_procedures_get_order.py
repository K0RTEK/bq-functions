import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_verify_itog(tags, attributes):
    tags = is_none(tags)
    attributes = is_none(attributes)

    if re.search(r'"уцо"|"уцо_мангазея|уцо_mgcom"', tags):
        return True
    else:
        return False