import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_object_price(object: str) -> str:
    object = is_none(object)

    if re.search(r'кладовые', object):
        return 'Кладовые'
    elif re.search(r'машиноместа', object):
       return 'Машиноместа'
    elif re.search(r'новогиреевский', object):
       return 'Новогиреевский'
    elif re.search(r'коммерция', object):
       return 'Коммерция'
    elif re.search(r'м-хаус', object):
       return 'М-Хаус'
    elif re.search(r'новое тушино', object):
       return 'Новое Тушино'
    elif re.search(r'вторичная', object):
       return 'Вторичная недвижимость'
    elif re.search(r'флагман', object):
       return 'Флагман'
    elif re.search(r'новое измайлово', object):
       return 'Новое Измайлово'
    elif re.search(r'дом на воскресенском', object):
       return 'Дом на Воскресенском'
    elif re.search(r'воскресенск, центральный', object):
       return 'Воскресенск, Центральный'
    elif re.search(r'фск', object):
       return 'ФСК'
    elif re.search(r'lake|лэйк', object):
       return 'The Lake'
    elif re.search(r'архитектор', object):
       return 'Архитектор'
    elif re.search(r'апрель парк|парк апрель', object):
       return 'Парк Апрель'
    elif re.search(r'гагаринский', object):
       return 'Гагаринский (Жуковский)'
    elif re.search(r'датский квартал', object):
       return 'Датский квартал'
    elif re.search(r'движение|dvizhen', object) and not re.search(r'говорово|govorovo', object):
       return 'Движение'
    elif re.search(r'говорово|govorovo', object):
       return 'Движение Говорово'
    elif re.search(r'дружба', object):
       return 'Дружба'
    elif re.search(r'дыхание', object):
       return 'Дыхание'
    elif re.search(r'молод.жный', object):
       return 'Молодежный'
    elif re.search(r'настроение', object):
       return 'Настроение'
    elif re.search(r'некрасовка', object):
       return 'Некрасовка'
    elif re.search(r'раменский', object):
       return 'Новый Раменский'
    elif re.search(r'огни.сочи', object):
       return 'Огни Сочи'
    elif re.search(r'олимп', object):
       return 'Олимп'
    elif re.search(r'aprel|апрель', object):
       return 'Парк Апрель'
    elif re.search(r'(первый|1).*ленинградский', object):
       return 'Первый Ленинградский'
    elif re.search(r'(первый|1).*лермонтовский', object):
       return 'Первый Лермонтовский'
    elif re.search(r'поколение', object):
       return 'Поколение'
    elif re.search(r'режисс.р', object):
       return 'Режиссер'
    elif re.search(r'римский', object):
       return 'Римский'
    elif re.search(r'рихард', object):
       return 'Рихард'
    elif re.search(r'rotterdam|роттердам', object):
       return 'Роттердам'
    elif re.search(r'sydney city|сидней', object) and not re.search(r'прайм|prime', object):
       return 'Сидней Сити'
    elif re.search(r'sky garden|skygarden|скайгарден|скай гарден', object):
       return 'Скай Гарден'
    elif re.search(r'скандинавский', object):
       return 'Скандинавский'
    elif re.search(r'сколковский', object):
       return 'Сколковский'
    elif re.search(r'центр.*2', object):
       return 'Центр-2'
    elif re.search(r'южная битца', object):
       return 'Южная Битца'
    elif re.search(r'сабурово', object):
       return 'Сабурово Клаб'
    elif re.search(r'донской', object):
       return 'Первый Донской'
    elif re.search(r'шереметьевский', object):
       return 'Первый Шереметьевский'
    elif re.search(r'южный', object):
       return 'Первый Южный'
    elif re.search(r'жаворонки', object):
       return 'Жаворонки Клаб'
    elif re.search(r'прайм|prime', object):
       return 'Сидней Прайм'
    elif re.search(r'тушино-2018', object):
       return 'Новое Тушино'
    elif re.search(r'молжаниново', object):
       return 'Первый Ленинградский'
    elif re.search(r'калуга, дружбы ул', object):
       return 'Дружба'
    elif re.search(r'калуга, воскресенский', object):
       return 'Воскресенский'
    elif re.search(r'калуга 17', object):
       return 'Молодежный'
    elif re.search(r'жк для номера на лендинге|спецпроект', object):
       return 'Спецпроект'
    elif re.search(r'ясеневский', object):
       return '1-й Ясеневский'
    elif re.search(r'измайловский|измаиловский', object):
       return '1-й Измайловский'
    elif re.search(r'химкинск', object):
       return 'Первый Химкинский'
    elif re.search(r'саларьев', object):
       return 'Первый Саларьевский'
    elif re.search(r'амбер|amber', object):
       return 'Амбер Сити'
    elif re.search(r'мартем|martem', object):
        return 'Мартемьяново Клаб'

    return f'NaN - {object}'
