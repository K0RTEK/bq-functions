import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_object_fact(object: str) -> str:
    object_lower = is_none(object)

    if re.search(r'лэйк|lake', object_lower):
        return 'The Lake'
    elif re.search(r'архитектор', object_lower):
      return 'Архитектор'
    elif re.search(r'вторичн', object_lower):
      return 'Вторичная недвижимость'
    elif re.search(r'гагаринский', object_lower):
      return 'Гагаринский'
    elif re.search(r'датский', object_lower):
      return 'Датский квартал'
    elif re.search(r'движение|движение.*тушино|тушино.*2018', object_lower) and not re.search(r'говорово', object_lower):
      return 'Движение'
    elif re.search(r'движение.*говорово', object_lower):
      return 'Движение Говорово'
    elif re.search(r'воскресенский', object_lower):
      return 'Дом на Воскресенском'
    elif re.search(r'домодедово парк', object_lower):
      return 'Домодедово Парк'
    elif re.search(r'дружб', object_lower):
      return 'Дружба'
    elif re.search(r'дск-1', object_lower):
      return 'ДСК-1'
    elif re.search(r'дыхание', object_lower):
      return 'Дыхание'
    elif re.search(r'калуга (17|18|19|31|32)|тайфун|молод(е|ё)жный', object_lower):
      return 'Молодежный'
    elif re.search(r'настроение', object_lower):
      return 'Настроение'
    elif re.search(r'некрасовка', object_lower):
      return 'Некрасовка'
    elif re.search(r'новогиреевский', object_lower):
      return 'Новогиреевский'
    elif re.search(r'новое измайлово', object_lower):
      return 'Новое Измайлово'
    elif re.search(r'новое тушино', object_lower):
      return 'Новое Тушино'
    elif re.search(r'раменск', object_lower):
      return 'Новый Раменский'
    elif re.search(r'новая пролетарка', object_lower):
      return 'Новая Пролетарка'
    elif re.search(r'олимп', object_lower):
      return 'Олимп'
    elif re.search(r'парк апрель', object_lower):
      return 'Парк Апрель'
    elif re.search(r'шереметьевский', object_lower):
      return 'Первый Шереметьевский'
    elif re.search(r'первый андреевский', object_lower):
      return 'Первый Андреевский'
    elif re.search(r'молжаниново|первый ленинградский', object_lower):
      return 'Первый Ленинградский'
    elif re.search(r'первый лермонтовский', object_lower):
      return 'Первый Лермонтовский'
    elif re.search(r'первый юбилейный', object_lower):
      return 'Первый Юбилейный'
    elif re.search(r'донской', object_lower):
      return 'Первый Донской'
    elif re.search(r'южный', object_lower):
      return 'Первый Южный'
    elif re.search(r'поколение', object_lower):
      return 'Поколение'
    elif re.search(r'режиссер', object_lower):
      return 'Режиссер'
    elif re.search(r'римский', object_lower):
      return 'Римский'
    elif re.search(r'рихард', object_lower):
      return 'Рихард'
    elif re.search(r'роттердам', object_lower):
      return 'Роттердам'
    elif re.search(r'сабур', object_lower):
      return 'Сабурово Клаб'
    elif re.search(r'жаворонки', object_lower):
      return 'Жаворонки Клаб'
    elif re.search(r'сидней', object_lower):
      return 'Сидней Сити'
    elif re.search(r'прайм|prime', object_lower):
      return 'Сидней Прайм'
    elif re.search(r'скай.*гарден', object_lower):
      return 'Скай Гарден'
    elif re.search(r'скандинавский', object_lower):
      return 'Скандинавский'
    elif re.search(r'солнцево', object_lower):
      return 'Солнцево'
    elif re.search(r'одинцово|сколковский', object_lower):
      return 'Сколковский'
    elif re.search(r'фск.*лидер', object_lower):
      return 'ФСК'
    elif re.search(r'центр.2', object_lower):
      return 'Центр-2'
    elif re.search(r'южная битца', object_lower):
        return 'Южная Битца'

    return f'NaN - {object}'
