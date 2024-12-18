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
        return 'Донстрой'

    if channel_name == 'контекст':
        if data_group == 'channel':
            return 'Контекстная реклама'
        elif data_group == 'campaign_agency':
            return 'MGCom'
        elif data_group == 'utm_medium':
            return 'cpc'
        elif data_group == 'placement':
            if placement_name == 'яндекс директ':
                return 'Яндекс Директ'
            elif placement_name == 'google ads':
                return 'Google Ads'
        elif data_group == 'utm_source':
            if placement_name == 'яндекс директ':
                return 'yandex'
            elif placement_name == 'google ads':
                return 'google'
        return 'Контекст'

    if channel_name == 'лидогенерация':
        if data_group == 'channel':
            return 'Лидогенерация'
        elif data_group == 'campaign_agency':
            return 'MGCom'
        elif data_group == 'utm_medium':
            return 'cpa'
        return 'Лидогенерация'

    if channel_name == 'базы недвижимости':
        if data_group == 'channel':
            return 'Базы недвижимости'
        elif data_group == 'campaign_agency':
            return 'MGCom'
        elif data_group == 'placement':
            if placement_name == 'циан':
                return 'Циан'
            elif placement_name == 'авито':
                return 'Авито'
            elif placement_name == 'яндекс недвижимость':
                return 'Яндекс Недвижимость'
        return 'Базы недвижимости'

    if channel_name == 'соцсети':
        if data_group == 'channel':
            return 'Реклама в соц.сетях'
        elif data_group == 'campaign_agency':
            return 'MGCom'
        elif data_group == 'utm_medium':
            return 'cpc'
        elif data_group == 'placement':
            if placement_name == 'вконтакте':
                return 'Вконтакте'
            elif placement_name == 'вкр':
                return 'ВКР'
            elif placement_name == 'mytarget':
                return 'Mytarget'
        elif data_group == 'utm_source':
            if placement_name == 'вконтакте':
                return 'vkontakte'
            elif placement_name == 'вкр':
                return 'vkr'
            elif placement_name == 'mytarget':
                return 'mt'
        return 'Соцсети'

    if channel_name == 'медийная реклама':
        if data_group == 'channel':
            return 'Медийная реклама'
        elif data_group == 'campaign_agency':
            return 'MGCom'
        return 'Медийная реклама'

    if channel_name == 'программатик':
        if data_group == 'channel':
            return 'Программатик'
        elif data_group == 'campaign_agency':
            return 'MGCom'
        elif data_group == 'placement':
            if placement_name == 'soloway':
                return 'Soloway'
            elif placement_name == 'hybrid':
                return 'Hybrid'
        elif data_group == 'utm_source':
            if placement_name == 'soloway':
                return 'soloway'
            elif placement_name == 'hybrid':
                return 'hybrid'
        elif data_group == 'utm_medium':
            if placement_name == 'soloway':
                return 'cpc'
            elif placement_name == 'hybrid':
                return 'cpc'
        return 'Программатик'