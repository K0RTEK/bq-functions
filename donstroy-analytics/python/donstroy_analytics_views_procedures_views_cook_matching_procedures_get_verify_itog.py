import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_verify_itog(stage):
    stage = is_none(stage)
    if stage is None or stage == 'дисквалифицирован':
        return False
    else:
        return True