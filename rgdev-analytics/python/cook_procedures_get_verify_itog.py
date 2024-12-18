import re
import datetime as dt

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_verify_itog(tags):
    tags = is_none(tags)

    if re.search(r'целевой mgcom', tags):
        return True
    else:
        return False