import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_quiz_type(campaign_name):
    return next(
        (value for value, condition in (
            ("Квиз Pages", re.search(r'quiz\.pages', is_none(campaign_name))),
            ("Квиз", re.search(r'quiz', is_none(campaign_name)))
        ) if condition is not None),
        ""
    )