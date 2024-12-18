def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def mediaplan_name(channel):
    channel = is_none(channel)
    # Проверка значений по аналогии с CASE WHEN
    if channel == 'Контекст':
        return 'Контекст'
    elif channel == 'Соцсети':
        return 'Соцсети'
    elif channel == 'Прайс-площадки':
        return 'Прайс-площадки'
    elif channel == 'Ретаргетинг':
        return 'Ретаргетинг'
    else:
        return 'NaN'

