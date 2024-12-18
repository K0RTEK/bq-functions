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