import re
import datetime as dt

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
        return 'Клиент'

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
        else:
            return 'Контекст'

    if channel_name == 'Лидогенерация':
        if data_group == 'channel':
            return 'Лидогенерация'
        elif data_group == 'campaign_agency':
            return 'MGCom'
        elif data_group == 'utm_medium':
            return 'cpa'
        else:
            return 'Лидогенерация'

    if channel_name == 'Базы недвижимости':
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
                return 'Яндекс Недвижимость'
        else:
            return 'Базы недвижимости'

    if channel_name == 'Соцсети':
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
            elif placement_name == 'Mytarget':
                return 'Mytarget'
        elif data_group == 'utm_source':
            if placement_name == 'Вконтакте':
                return 'vkontakte'
            elif placement_name == 'ВКР':
                return 'vkr'
            elif placement_name == 'Mytarget':
                return 'mt'
        else:
            return 'Соцсети'

    if channel_name == 'Медийная реклама':
        if data_group == 'channel':
            return 'Медийная реклама'
        elif data_group == 'campaign_agency':
            return 'MGCom'
        else:
            return 'Медийная реклама'

    if channel_name == 'Программатик':
        if data_group == 'channel':
            return 'Программатик'
        elif data_group == 'campaign_agency':
            return 'MGCom'
        elif data_group == 'placement':
            if placement_name == 'Soloway':
                return 'Soloway'
            elif placement_name == 'Hybrid':
                return 'Hybrid'
        elif data_group == 'utm_source':
            if placement_name == 'Soloway':
                return 'soloway'
            elif placement_name == 'Hybrid':
                return 'hybrid'
        elif data_group == 'utm_medium':
            if placement_name == 'Soloway' or placement_name == 'Hybrid':
                return 'cpc'
        else:
            return 'Программатик'

    return None
