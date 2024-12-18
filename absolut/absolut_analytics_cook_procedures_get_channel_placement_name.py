import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_channel_placement_name(channel_name, placement_name, data_group):
    channel_name = is_none(channel_name)
    placement_name = is_none(placement_name)
    data_group = is_none(data_group)
    if data_group == 'client_name':
        return 'Абсолют'

    if channel_name == 'Контекст':
        if data_group == 'channel':
            return 'Контекстная реклама'
        elif data_group == 'campaign_agency':
            return 'MGCom'
        elif data_group == 'placement':
            if placement_name == 'Яндекс Директ':
                return 'Яндекс Директ'
            elif placement_name == 'Google Ads':
                return 'Google Ads'
        elif data_group == 'utm_source':
            if placement_name == 'Яндекс Директ':
                return 'yandex'
            elif placement_name == 'Google Ads':
                return 'google'
        return 'Контекстная реклама'

    if channel_name == 'Базы недвижимости':
        if data_group == 'placement':
            if re.search(r'циан|cian', placement_name, re.IGNORECASE):
                return 'Циан'
            elif re.search(r'авито|avito', placement_name, re.IGNORECASE):
                return 'Авито'
        return 'Базы недвижимости'

    if channel_name == 'Медийная реклама':
        return 'Медийная реклама'

    return None
