import re
import datetime as dt

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def month_ru(date):
    if date is '':
        return ''
    date = dt.date.fromisoformat(date)
    return {
        1: 'январь',
        2: 'февраль',
        3: 'март',
        4: 'апрель',
        5: 'май',
        6: 'июнь',
        7: 'июль',
        8: 'август',
        9: 'сентябрь',
        10: 'октябрь',
        11: 'ноябрь',
        12: 'декабрь'
    }.get(date.month, 'NaN')