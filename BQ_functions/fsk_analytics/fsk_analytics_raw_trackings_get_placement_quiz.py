import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_placement_quiz(quiz_name, utm_source):
    quiz_name = is_none(quiz_name)
    utm_source = is_none(utm_source)

    # Проверка по utm_source
    if re.search(r'mytarget|mt', utm_source):
        return 'MyTarget'
    elif re.search(r'vkontakte|vk', utm_source) and not re.search(r'vk.*reklama', utm_source):
        return 'Vkontakte'
    elif re.search(r'vk.*reklama|vkads|vkreklama', utm_source):
        return 'VK Reklama'
    elif re.search(r'tiktok', utm_source):
        return 'Tik-tok'
    elif re.search(r'yandex', utm_source):
        return 'Яндекс.Директ'
    elif re.search(r'google', utm_source):
        return 'Google Ads'
    elif re.search(r'fb|facebook', utm_source):
        return 'Facebook'

    # Если по utm_source не найдено, проверка по quiz_name
    if re.search(r'fb.*mt|mt|мт', quiz_name):
        return 'MyTarget'
    elif re.search(r'fb.*vk|vk|вк', quiz_name) and not re.search(r'vkr|reklama', quiz_name):
        return 'Vkontakte'
    elif re.search(r'vkr|vk.*reklama', quiz_name):
        return 'VK Reklama'
    elif re.search(r'tenchat', quiz_name):
        return 'Tenchat'
    elif re.search(r'tiktok|tik-tok', quiz_name):
        return 'Tik-tok'
    elif re.search(r'яндекс|yandex', quiz_name):
        return 'Яндекс.Директ'
    elif re.search(r'google', quiz_name):
        return 'Google Ads'
    elif re.search(r'fb|facebook', quiz_name) or quiz_name in [
        'fsk nstr', 'fsk rezh', 'fsk rih', 'fsk rim', 'fsk br olv',
        'fsk br', 'fsk br bus new', 'fsk skol', 'fsk br business', 'fsk br olv'
    ]:
        return 'Facebook'

    # Если ничего не подходит
    return 'NaN'

