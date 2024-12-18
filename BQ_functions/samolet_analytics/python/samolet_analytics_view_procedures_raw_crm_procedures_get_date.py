import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_segment(parameter):
    parameter = is_none(parameter)
    months = {
        'янв': 1,
        'фев': 2,
        'мар': 3,
        'апр': 4,
        'мая': 5,
        'июн': 6,
        'июл': 7,
        'авг': 8,
        'сен': 9,
        'окт': 10,
        'ноя': 11,
        'дек': 12
    }
    for month, value in months.items():
        if month in parameter:
            day = int(re.search(r'\d+', parameter).group())
            return f'{2024}-{value}-{day}'
    return ''