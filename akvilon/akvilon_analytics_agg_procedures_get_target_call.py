import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_target_call(call_tags):
    call_tags = is_none(call_tags)
    return bool(re.search(r'("|,| |$)mg_целевой("|,| |$)', call_tags.strip()))
