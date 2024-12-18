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
        return 'Аквилон'

    elif channel_name == 'Контекст':
        if data_group == 'channel':
            return 'Контекстная реклама'
        elif data_group == 'campaign_agency':
            return 'MGCom'
        elif data_group == 'utm_medium':
            return 'cpc'
        elif data_group == 'placement':
            if placement_name == 'Яндекс Директ':
                return 'Яндекс.Директ'
            elif placement_name == 'Google Ads':
                return 'Google Ads'
        elif data_group == 'utm_source':
            if placement_name == 'Яндекс Директ':
                return 'yandex'
            elif placement_name == 'Google Ads':
                return 'google'
        return 'Контекст'

    elif channel_name == 'Лидогенерация':
        if data_group == 'channel':
            return 'Лидогенерация'
        elif data_group == 'campaign_agency':
            return 'MGCom'
        elif data_group == 'utm_medium':
            return 'cpa'
        return 'Лидогенерация'

    elif channel_name == 'Базы недвижимости':
        if data_group == 'channel':
            return 'Базы недвижимости'
        elif data_group == 'campaign_agency':
            return 'MGCom'
        elif data_group == 'placement':
            placement_mapping = {
                'Циан': 'Cian',
                'Авито': 'Авито',
                'Яндекс Недвижимость': 'Яндекс.Недвижимость',
                'Домклик': 'Домклик'
            }
            return placement_mapping.get(placement_name, 'Базы недвижимости')
        return 'Базы недвижимости'

    elif channel_name == 'Соцсети':
        if data_group == 'channel':
            return 'Соц сети'
        elif data_group == 'campaign_agency':
            return 'MGCom'
        elif data_group == 'utm_medium':
            return 'cpc'
        elif data_group == 'placement':
            placement_mapping = {
                'ВКР': 'ВК Реклама',
                'Mytarget': 'MyTarget'
            }
            return placement_mapping.get(placement_name, 'Соц сети')
        elif data_group == 'utm_source':
            source_mapping = {
                'ВКР': 'vkr',
                'Mytarget': 'mt'
            }
            return source_mapping.get(placement_name, 'Соц сети')
        return 'Соц сети'

    elif channel_name == 'Медийная реклама':
        if data_group == 'channel':
            return 'Медийная реклама'
        elif data_group == 'campaign_agency':
            return 'MGCom'
        return 'Медийная реклама'

    elif channel_name == 'Программатик':
        if data_group == 'channel':
            return 'Programmatic/OLV'
        elif data_group == 'campaign_agency':
            return 'MGCom'
        elif data_group == 'placement':
            placement_mapping = {
                'Upravel': 'Upravel',
                'Яндекс': 'Яндекс'
            }
            return placement_mapping.get(placement_name, 'Programmatic/OLV')
        return 'Programmatic/OLV'

    elif channel_name == 'Промо Страницы':
        if data_group == 'channel':
            return 'Промо Страницы'
        elif data_group == 'campaign_agency':
            return 'MGCom'
        elif data_group == 'placement':
            return 'Промо Страницы' if placement_name == 'Промо Страницы' else 'Промо Страницы'
        return 'Промо Страницы'

    return None