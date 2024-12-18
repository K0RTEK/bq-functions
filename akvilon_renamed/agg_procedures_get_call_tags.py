import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_call_tags(call_tags):
    call_tags = is_none(call_tags)
    return ','.join(re.findall(r'"names":\[(.+?)\]', call_tags))
