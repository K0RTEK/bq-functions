import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_placement(source_medium):
    source_medium = is_none(source_medium)
    if re.search(r'mytarget', source_medium):
        return 'MyTarget'
    elif re.search(r'vk ', source_medium):
        return 'Vkontakte'
    elif re.search(r'vkr', source_medium):
        return 'VK Reklama'
    elif re.search(r'yandex / cpc', source_medium):
        return 'Яндекс.Директ'
    elif re.search(r'google / cpc', source_medium):
        return 'Google ads'
    elif re.search(r'soloway', source_medium):
        return 'Soloway'
    elif re.search(r'direct / mgcom_cpm', source_medium):
        return 'Яндекс.Директ'
    return 'placement - NaN'