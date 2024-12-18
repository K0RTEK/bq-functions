def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_placement_quiz(quiz_name: str, utm_source: str, name_length: str) -> str:
    utm_source = is_none(utm_source)
    quiz_name = is_none(quiz_name)
    name_length = is_none(name_length)

    if 'mytarget' in utm_source or 'mt' in utm_source:
        return 'mt' if name_length == 'shortname' else 'MyTarget'
    elif 'vkontakte' in utm_source or ('vk' in utm_source and 'vk.*reklama' not in utm_source):
        return 'vk' if name_length == 'shortname' else 'Vkontakte'
    elif 'vk.*reklama' in utm_source or 'vkads' in utm_source or 'vkreklama' in utm_source:
        return 'vkr' if name_length == 'shortname' else 'VK Reklama'
    elif 'tiktok' in utm_source:
        return 'tiktok' if name_length == 'shortname' else 'Tik-tok'
    elif 'yandex' in utm_source:
        return 'yandex' if name_length == 'shortname' else 'Яндекс.Директ'
    elif 'google' in utm_source:
        return 'google' if name_length == 'shortname' else 'Google Ads'
    elif 'fb' in utm_source or 'facebook' in utm_source:
        return 'fb' if name_length == 'shortname' else 'Facebook'
    else:
        if 'fb.*mt' in quiz_name or 'mt' in quiz_name or 'мт' in quiz_name:
            return 'mt' if name_length == 'shortname' else 'MyTarget'
        elif 'fb.*vk' in quiz_name or 'vk' in quiz_name or 'вк' in quiz_name and 'vkr' not in quiz_name and 'reklama' not in quiz_name:
            return 'vk' if name_length == 'shortname' else 'Vkontakte'
        elif 'vkr' in quiz_name or 'vk.*reklama' in quiz_name:
            return 'vkr' if name_length == 'shortname' else 'VK Reklama'
        elif 'tenchat' in quiz_name:
            return 'tch' if name_length == 'shortname' else 'Tenchat'
        elif 'tiktok' in quiz_name or 'tik-tok' in quiz_name:
            return 'tiktok' if name_length == 'shortname' else 'Tik-tok'
        elif 'яндекс' in quiz_name or 'yandex' in quiz_name:
            return 'yandex' if name_length == 'shortname' else 'Яндекс.Директ'
        elif 'google' in quiz_name:
            return 'google' if name_length == 'shortname' else 'Google Ads'
        elif 'fb' in quiz_name or 'facebook' in quiz_name or quiz_name in [
            'FSK NSTR', 'FSK REZH', 'FSK RIH', 'FSK RIM', 'FSK BR OLV',
            'FSK BR', 'FSK BR BUS New', 'FSK SKOL', 'FSK BR BUSINESS', 'FSK BR OLV'
        ]:
            return 'fb' if name_length == 'shortname' else 'Facebook'
        else:
            return 'NaN'
