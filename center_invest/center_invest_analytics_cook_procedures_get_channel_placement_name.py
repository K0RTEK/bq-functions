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
        return 'Центр-Инвест'
    elif channel_name == 'Контекст' and data_group == 'placement':
        return 'Яндекс Директ'
    elif channel_name == 'Лидогенерация' and data_group == 'channel':
        return 'Лидогенерация'
    elif channel_name == 'Соцсети' and data_group == 'placement':
        if placement_name == 'Вконтакте':
            return 'Вконтакте'
    return 'Unknown'