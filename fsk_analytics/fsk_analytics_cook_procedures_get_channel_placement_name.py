def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_channel_placement_name(channel_name, placement_name, data_group):
    channel_name = is_none(channel_name)
    placement_name = is_none(placement_name)
    data_group = is_none(data_group)

    if channel_name == 'Контекст':
        if data_group == 'channel':
            return 'Контекстная реклама'
        elif data_group == 'campaign_agency':
            return 'MGCom'
        elif data_group == 'utm_medium':
            return 'cpc'
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
                return 'cian.ru База'
            elif placement_name == 'Авито':
                return 'Авито (avito) База'
            elif placement_name == 'Яндекс Недвижимость':
                return 'Яндекс.Недвижимость База'
            elif placement_name == 'Новострой-М':
                return 'Novostroy-m.ru База'
        return 'Базы недвижимости'
    elif channel_name == 'Соцсети':
        if data_group == 'channel':
            return 'Реклама в соц.сетях'
        elif data_group == 'campaign_agency':
            return 'MGCom'
        elif data_group == 'placement':
            if placement_name == 'Facebook':
                return 'Facebook'
            elif placement_name == 'Tik-tok':
                return 'Tik-tok'
            elif placement_name == 'Telegram':
                return 'Telegram'
            elif placement_name == 'Mytarget':
                return 'MyTarget'
            elif placement_name == 'ВКР':
                return 'ВК Реклама'
            elif placement_name == 'Вконтакте':
                return 'Vkontakte'
        elif data_group == 'utm_source':
            if placement_name == 'Facebook':
                return 'fb'
            elif placement_name == 'Tik-tok':
                return 'tik_tok'
            elif placement_name == 'Telegram':
                return 'tg'
            elif placement_name == 'Mytarget':
                return 'mt'
            elif placement_name == 'ВКР':
                return 'vkr'
            elif placement_name == 'Вконтакте':
                return 'vk'
        return 'Реклама в соц.сетях'
    elif channel_name == 'Программатик':
        if data_group == 'channel':
            return 'Программатик'
        elif data_group == 'campaign_agency':
            return 'MGCom'
        elif data_group == 'placement':
            if placement_name == 'Upravel':
                return 'Upravel'
            elif placement_name == 'DV360':
                return 'DV360 программатик'
            elif placement_name == 'Criteo':
                return 'criteo.com Программатик'
            elif placement_name == 'Soloway':
                return 'Soloway Программатик'
        return 'Программатик'
    return None