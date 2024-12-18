import re


def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()


def get_channel(source_medium):
    source_medium = is_none(source_medium)

    if re.search(r'mytarget', source_medium):
        return 'Соцсети'
    elif re.search(r'vk ', source_medium):
        return 'Соцсети'
    elif re.search(r'vkr', source_medium):
        return 'Соцсети'
    elif re.search(r'yandex / cpc', source_medium):
        return 'Контекст'
    elif re.search(r'google / cpc', source_medium):
        return 'Контекст'
    elif re.search(r'soloway', source_medium):
        return 'Ретаргетинг'
    else:
        return 'channel - NaN'


def search_net(source_medium, campaign_name, ad_name, campaign_id):
    if get_channel(source_medium) == "Контекст":
        if re.search(r'[^_]search[_$]', campaign_name) or re.search(r'^[^_]search[_$]', ad_name):
            return 'Поиск'
        elif re.search(r'[^_]network[_$]', campaign_name) or re.search(r'^[^_]network[_$]', ad_name):
            return 'Сеть'
        return 'NaN'
    return "None"
