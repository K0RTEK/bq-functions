import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_object_class(object: str) -> str:
    object = is_none(object)
    if re.search(r'новогиреевский', object):
        return 'Комфорт'
    elif re.search(r'м-хаус', object):
       return 'Эконом'
    elif re.search(r'новое тушино', object):
       return 'Комфорт'
    elif re.search(r'флагман', object):
       return 'Бизнес'
    elif re.search(r'новое измайлово', object):
       return 'Эконом'
    elif re.search(r'дом на воскресенском', object):
       return 'Бизнес'
    elif re.search(r'воскресенск, центральный', object):
       return 'Комфорт'
    elif re.search(r'lake', object):
       return 'Бизнес'
    elif re.search(r'архитектор', object):
       return 'Бизнес'
    elif re.search(r'апрель парк|парк апрель', object):
       return 'Комфорт'
    elif re.search(r'гагаринский', object):
       return 'Комфорт'
    elif re.search(r'датский квартал', object):
       return 'Комфорт'
    elif re.search(r'движение|dvizhen', object) and not re.search(r'говорово|govorovo', object):
       return 'Комфорт'
    elif re.search(r'говорово|govorovo', object):
       return 'Комфорт'
    elif re.search(r'дружба', object):
       return 'Комфорт'
    elif re.search(r'дыхание', object):
       return 'Бизнес'
    elif re.search(r'молод.жный', object):
       return 'Комфорт'
    elif re.search(r'настроение', object):
       return 'Комфорт'
    elif re.search(r'некрасовка', object):
       return 'Комфорт'
    elif re.search(r'раменский', object):
       return 'Бизнес'
    elif re.search(r'огни.сочи', object):
       return 'Бизнес'
    elif re.search(r'олимп', object):
       return 'Комфорт'
    elif re.search(r'aprel|апрель', object):
       return 'Комфорт'
    elif re.search(r'(первый|1).*ленинградский', object):
       return 'Комфорт'
    elif re.search(r'(первый|1).*лермонтовский', object):
       return 'Комфорт'
    elif re.search(r'поколение', object):
       return 'Комфорт'
    elif re.search(r'режисс.р', object):
       return 'Бизнес'
    elif re.search(r'римский', object):
       return 'Комфорт'
    elif re.search(r'рихард', object):
       return 'Бизнес'
    elif re.search(r'rotterdam|роттердам', object):
       return 'Бизнес'
    elif re.search(r'sydney city|сидней сити', object):
       return 'Бизнес'
    elif re.search(r'sky garden|skygarden|скайгарден|скай гарден', object):
       return 'Бизнес'
    elif re.search(r'скандинавский', object):
       return 'Комфорт'
    elif re.search(r'сколковский', object):
       return 'Комфорт'
    elif re.search(r'центр.*2', object):
       return 'Комфорт'
    elif re.search(r'южная битца', object):
       return 'Комфорт'
    elif re.search(r'сабурово', object):
       return 'Бизнес'
    elif re.search(r'донской', object):
       return 'Комфорт'
    elif re.search(r'шереметьевский', object):
       return 'Комфорт'
    elif re.search(r'южный', object):
       return 'Комфорт'
    elif re.search(r'жаворонки', object):
       return 'Комфорт'
    elif re.search(r'прайм|prime', object):
       return 'Бизнес'
    elif re.search(r'новое тушино', object):
       return 'Комфорт'
    elif re.search(r'на воскресенском', object):
       return 'Комфорт'
    elif re.search(r'(первый|1).*ясеневский', object):
       return 'Комфорт'
    elif re.search(r'(первый|1).*изма(и|й)ловский', object):
        return 'Комфорт'

    return 'NaN'
