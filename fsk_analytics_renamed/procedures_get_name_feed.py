import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_name_feed(name):
    name = is_none(name)
    if re.search(r'lake', name):
        return 'The Lake'
    elif re.search(r'zoom.*неве', name):
       return 'Zoom на Неве'
    elif re.search(r'zoom.*черная', name):
       return 'Zoom Черная речка'
    elif re.search(r'архитектор', name):
       return 'Архитектор'
    elif re.search(r'балашиха', name):
       return 'Балашиха'
    elif re.search(r'гагаринский', name):
       return 'Гагаринский'
    elif re.search(r'датский', name):
       return 'Датский квартал'
    elif re.search(r'движение|движение.*тушино|тушино.*2018', name) and not re.search(r'говорово', name):
       return 'Движение'
    elif re.search(r'движение.*говорово', name):
       return 'Движение Говорово'
    elif re.search(r'дом на воскресенском', name):
       return 'Дом на Воскресенском'
    elif re.search(r'домодедово парк', name):
       return 'Домодедово Парк'
    elif re.search(r'дружб', name):
       return 'Дружба'
    elif re.search(r'дск-1', name):
       return 'ДСК-1'
    elif re.search(r'дыхание', name):
       return 'Дыхание'
    elif re.search(r'заречный квартал', name):
       return 'Заречный квартал'
    elif re.search(r'калуга (17|18|19|31|32)|тайфун|молод(е|ё)жный', name):
       return 'Молодежный'
    elif re.search(r'московский', name):
       return 'Московский'
    elif re.search(r'на набережной', name):
       return 'На набережной. Орехово-Зуево'
    elif re.search(r'настроение', name):
       return 'Настроение'
    elif re.search(r'некрасовка', name):
       return 'Некрасовка'
    elif re.search(r'новогиреевский', name):
       return 'Новогиреевский'
    elif re.search(r'новое измайлово', name):
       return 'Новое Измайлово'
    elif re.search(r'новое тушино', name):
       return 'Новое Тушино'
    elif re.search(r'раменск', name):
       return 'Новый Раменский'
    elif re.search(r'олимп', name):
       return 'Олимп'
    elif re.search(r'парк апрель', name):
       return 'Парк Апрель'
    elif re.search(r'первый андреевский', name):
       return 'Первый Андреевский'
    elif re.search(r'пушкинский', name):
       return 'Пушкинский'
    elif re.search(r'1.*ленинградский', name):
       return 'Первый Ленинградский'
    elif re.search(r'1.*лермонтовский', name):
       return 'Первый Лермонтовский'
    elif re.search(r'первый юбилейный', name):
       return 'Первый Юбилейный'
    elif re.search(r'поколение', name):
       return 'Поколение'
    elif re.search(r'режиссер', name):
       return 'Режиссер'
    elif re.search(r'римский', name):
       return 'Римский'
    elif re.search(r'рихард', name):
       return 'Рихард'
    elif re.search(r'rotterdam', name):
       return 'Роттердам'
    elif re.search(r'sydney.*city', name):
       return 'Сидней Сити'
    elif re.search(r'sydney.*prime', name):
       return 'Сидней Прайм'
    elif re.search(r'sky.*garden', name):
       return 'Скай Гарден'
    elif re.search(r'скандинавский', name):
       return 'Скандинавский'
    elif re.search(r'одинцово|сколковский', name):
       return 'Сколковский'
    elif re.search(r'солнцево', name):
       return 'Солнцево'
    elif re.search(r'фск.*лидер', name):
       return 'ФСК'
    elif re.search(r'центр.2', name):
       return 'Центр-2'
    elif re.search(r'южная битца', name):
        return 'Южная Битца'
    return f'NaN - {name}'