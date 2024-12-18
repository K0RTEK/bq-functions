import re
import datetime as dt

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_channel(placement):
    return {
        'Яндекс Директ': 'Контекст',
        'Google Ads': 'Контекст',
        'Facebook': 'Соцсети',
        'МТ': 'Соцсети',
        'Вконтакте': 'Соцсети',
        'ВКР': 'Соцсети',
        'Прайс-площадки': 'Прайс-площадки',
        'Соловей': 'Ретаргетинг',
        'Медиаснайпер': 'Ретаргетинг'
    }.get(is_none(placement), 'NaN')