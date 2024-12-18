import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_placement(parameter):
    parameter = is_none(parameter)
    if re.search(r'yandex|яндекс', parameter) and not re.search(r'realty|недвижимость', parameter):
        return 'Яндекс Директ'
    elif re.search(r'avito|авито', parameter):
        return 'Авито'
    elif re.search(r'cian|циан', parameter):
        return 'Циан'
    elif re.search(r'realty.*yandex|яндекс.*недвижимость', parameter):
        return 'Яндекс Недвижимость'
    elif re.search(r'jcat', parameter):
        return 'JCAT'
    elif re.search(r'svetvokne', parameter):
        return 'Svetvokne'
    elif re.search(r'm2|м2', parameter):
        return 'М2'
    elif re.search(r'domclick|домклик', parameter):
        return 'Домклик'
    elif re.search(r'novostroy-m', parameter):
        return 'Новострой-М'
    elif re.search(r'avaho|авахо', parameter):
        return 'Авахо'
    elif re.search(r'move', parameter):
        return 'Move.ru'
    elif re.search(r'мирквартир', parameter):
        return 'МирКвартир'
    elif re.search(r'vkr|vk reklama|vk ads|vkads', parameter):
        return 'ВКР'
    elif re.search(r'	vk | vk$| vk | вк | вк$|fb.*vk|вконтакте| вк ', parameter):
        return 'Вконтакте'
    elif re.search(r' mt$|fb.*mt| мт$| мт |mt|mytarget|target.mail| mail ', parameter):
        return 'MyTarget'
    elif re.search(r'facebook| fb | fb$|insta|fb.inst', parameter):
        return 'Facebook'
    elif re.search(r'telegram', parameter):
        return 'Telegram'
    elif re.search(r'tenchat', parameter):
        return 'TenChat'
    elif re.search(r'tiktok|tik-tok', parameter):
        return 'Tik-tok'
    else:
        return 'Не определено'