import datetime as dt

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_verify_itog(date, tags):
    date_threshold = dt.date(2024, 6, 1)
    tags = is_none(tags)

    if date < date_threshold and 'целевой_б24' in tags and 'уже не актуально' not in tags:
        return True
    elif date >= date_threshold and 'целевой_б24' in tags:
        return True
    else:
        return False
