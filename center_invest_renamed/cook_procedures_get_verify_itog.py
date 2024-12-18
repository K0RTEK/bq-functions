import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_verify_itog(tags):
    tags = is_none(tags)
    if re.search(r'целевой', tags) and not re.search(r'нецелевой', tags):
        return True
    return False