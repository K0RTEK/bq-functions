def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_channel(placement):
    placement = is_none(placement)
    # Проверка значений по аналогии с CASE WHEN
    if placement in ['Яндекс Директ', 'Google Ads']:
        return 'Контекст'
    elif placement in ['Facebook', 'МТ', 'Вконтакте', 'ВКР']:
        return 'Соцсети'
    elif placement == 'Прайс-площадки':
        return 'Прайс-площадки'
    elif placement in ['Соловей', 'Медиаснайпер']:
        return 'Ретаргетинг'
    elif placement in ['Яндекс РМП', 'ВКР Mobile']:
        return 'Mobile'
    else:
        return 'NaN'

