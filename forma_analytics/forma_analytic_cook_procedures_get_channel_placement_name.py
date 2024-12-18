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
        return 'Forma'
    elif channel_name == 'Контекст':
        if data_group == 'channel':
            return 'Контекстная реклама'
        elif data_group == 'placement':
            return 'Яндекс Директ'
        elif data_group == 'campaign_agency':
            return 'MGCom'
        elif data_group == 'utm_source':
            return 'yandex'
        elif data_group == 'utm_medium':
            return 'cpc'
        return 'Яндекс Директ'
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
            if placement_name == 'Циан':
                return 'Циан'
            elif placement_name == 'Авито':
                return 'Авито'
            elif placement_name == 'Яндекс Недвижимость':
                return 'Яндекс.Недвижимость'
            elif placement_name == 'Jcat':
                return 'JCat'
            elif placement_name == 'Домклик':
                return 'Домклик'
        return 'Базы недвижимости'
    elif channel_name == 'Соцсети':
        if data_group == 'channel':
            return 'Реклама в соц.сетях'
        elif data_group == 'campaign_agency':
            return 'MGCom'
        elif data_group == 'utm_medium':
            return 'cpc'
        elif data_group == 'placement':
            if placement_name == 'Вконтакте':
                return 'Вконтакте'
            elif placement_name == 'ВКР':
                return 'ВКР'
        elif data_group == 'utm_source':
            if placement_name == 'Вконтакте':
                return 'vkontakte'
            elif placement_name == 'ВКР':
                return 'vkr'
        return 'Соцсети'
    elif channel_name == 'Программатик':
        if data_group == 'channel':
            return 'Программатик'
        elif data_group == 'campaign_agency':
            return 'MGCom'
        elif data_group == 'placement':
            if placement_name == 'Soloway':
                return 'Soloway'
            elif placement_name == 'Hybrid':
                return 'Hybrid'
        return 'Программатик'
    return None