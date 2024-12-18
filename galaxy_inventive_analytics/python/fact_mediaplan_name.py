import re
import datetime as dt

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def fact_mediaplan_name(channel):
    channel = is_none(channel)
    return {
        '': 'NaN',
        'контекст': 'Контекст',
        'соцсети': 'Соцсети',
        'прайс-площадки': 'Прайс-площадки',
        'ретаргетинг': 'Ретаргетинг',
        'флайт s24': 'Флайт S24',
    }.get(channel, 'NaN')