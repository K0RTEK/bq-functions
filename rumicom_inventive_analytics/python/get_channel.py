import re
import datetime as dt

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_channel(placement):
    placement = is_none(placement)
    if placement == 'яндексдирект':
        return 'Контекст'
    else:
        return 'NaN'