import re
import datetime as dt

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()