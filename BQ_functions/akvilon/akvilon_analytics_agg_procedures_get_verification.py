import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_verification(tags):
    tags = is_none(tags)
    return bool(re.search(r"(^|(, )|,)целевой($| ,|,)", tags.strip()))
