import datetime as dt

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def comissions(placement_or_channel, date):
    placement_or_channel = is_none(placement_or_channel)
    
    if placement_or_channel == 'google ads':
        if date < dt.date(2021, 3, 1):
            return 0.1
        elif date >= dt.date(2021, 3, 1):
            return 0.09
        return 0
    elif placement_or_channel == 'яндекс директ':
        if date < dt.date(2022, 8, 1):
            return 0.07
        elif date >= dt.date(2022, 8, 1):
            return 0
        return 0
    elif placement_or_channel == 'facebook':
        if date < dt.date(2021, 3, 1):
            return 0.1
        elif date >= dt.date(2021, 3, 1):
            return 0.09
        return 0
    elif placement_or_channel == 'tik-tok':
        return 0.01
    elif placement_or_channel in ('vkontakte', 'vk reklama', 'mytarget'):
        return 0
    elif placement_or_channel in ('лидогенерация', 'программатик', 'блоггеры'):
        return 0.01
    return 0