import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_verify_itog(tags):
    tags = is_none(tags)
    if re.search(r'целевой', tags, re.IGNORECASE) and not re.search(r'нецелевой|не целевой', tags, re.IGNORECASE):
        return True
    return False
