import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_tags(tags):
    tags = is_none(tags)
    if re.search(r'names', tags):
        return re.sub(r'\{|\}|\[|\]', '', re.search(r'"names":(.*)', tags).group(1))
    return tags