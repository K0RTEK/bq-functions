import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_object_quiz(placement: str, quiz_name: str, contact_phone: str) -> str:
    placement = is_none(placement)
    quiz_name = is_none(quiz_name)
    contact_phone = is_none(contact_phone)

    if placement == 'vk':
        if re.search(r'7999999999|7911111111|700000000|9111111111', contact_phone):
            return 'Тест'
        elif re.search(r'br.*olv', quiz_name):
           return 'Бренд ФСК OLV'
        elif re.search(r'br.*business', quiz_name) and not re.search(r'outlet', quiz_name):
           return 'Бизнес ФСК'
        elif re.search(r'br|fskmain', quiz_name) and not re.search(r'olv|business|outlet', quiz_name):
           return 'Бренд ФСК'
        elif re.search(r'fsk-outlet', quiz_name):
           return 'ФСК Аутлет'
        elif re.search(r'nstr', quiz_name):
           return 'Настроение'
        elif re.search(r'rezh', quiz_name):
           return 'Режиссер'
        elif re.search(r'rim', quiz_name) and not re.search(r'prime', quiz_name):
           return 'Римский'
        elif re.search(r'rih', quiz_name):
           return 'Рихард'
        elif re.search(r'сабурово|saburovo', quiz_name):
           return 'Сабурово Клаб'
        elif re.search(r'zhavoron|жаворон', quiz_name):
           return 'Жаворонки Клаб'
        elif re.search(r'sidn', quiz_name) and not re.search(r'prime', quiz_name):
           return 'Сидней Сити'
        elif re.search(r'prime', quiz_name):
           return 'Сидней Прайм'
        elif re.search(r'gard', quiz_name):
           return 'Скай Гарден'
        elif re.search(r'skol', quiz_name):
           return 'Сколковский'
        elif re.search(r'olimp|olp', quiz_name):
           return 'Олимп'
        elif re.search(r'molode|mld', quiz_name):
           return 'Молодежный'
        elif re.search(r'aprel', quiz_name):
           return 'Парк Апрель'
        elif re.search(r'sheremet|шеремет', quiz_name):
           return '1-й Шереметьевский'
        elif re.search(r'lake', quiz_name):
            return 'The Lake'
        return f'NaN - {quiz_name}'

    elif placement == 'mt':
        if re.search(r'7999999999|7911111111|700000000', contact_phone):
            return 'Тест'
        elif re.search(r'br.*olv', quiz_name):
          return 'Бренд ФСК OLV'
        elif re.search(r'br.*business', quiz_name) and not re.search(r'outlet', quiz_name):
          return 'Бизнес ФСК'
        elif re.search(r'br|fskmain', quiz_name) and not re.search(r'olv|business|outlet', quiz_name):
          return 'Бренд ФСК'
        elif re.search(r'fsk-outlet', quiz_name):
          return 'ФСК Аутлет'
        elif re.search(r'nstr', quiz_name):
          return 'Настроение'
        elif re.search(r'rezh', quiz_name):
          return 'Режиссер'
        elif re.search(r'сабурово|saburovo', quiz_name):
          return 'Сабурово Клаб'
        elif re.search(r'zhavoron|жаворон', quiz_name):
          return 'Жаворонки Клаб'
        elif re.search(r'rim', quiz_name) and not re.search(r'prime', quiz_name):
          return 'Римский'
        elif re.search(r'rih', quiz_name):
          return 'Рихард'
        elif re.search(r'sidn', quiz_name) and not re.search(r'prime', quiz_name):
          return 'Сидней Сити'
        elif re.search(r'prime', quiz_name):
          return 'Сидней Прайм'
        elif re.search(r'gard', quiz_name):
          return 'Скай Гарден'
        elif re.search(r'skol', quiz_name):
          return 'Сколковский'
        elif re.search(r'olimp|olp', quiz_name):
          return 'Олимп'
        elif re.search(r'molode|mld', quiz_name):
          return 'Молодежный'
        elif re.search(r'aprel', quiz_name):
          return 'Парк Апрель'
        elif re.search(r'sheremet|шеремет', quiz_name):
          return '1-й Шереметьевский'
        elif re.search(r'lake', quiz_name):
            return 'The Lake'
        return f'NaN - {quiz_name}'

    elif placement == 'vkr':
        if re.search(r'7999999999|7911111111|700000000|9111111111', contact_phone):
            return 'Тест'
        elif re.search(r'br.*olv', quiz_name):
           return 'Бренд ФСК OLV'
        elif re.search(r'br.*business', quiz_name) and not re.search(r'outlet', quiz_name):
           return 'Бизнес ФСК'
        elif re.search(r'br|fskmain', quiz_name) and not re.search(r'olv|business|outlet', quiz_name):
           return 'Бренд ФСК'
        elif re.search(r'fsk-outlet', quiz_name):
           return 'ФСК Аутлет'
        elif re.search(r'nstr', quiz_name):
           return 'Настроение'
        elif re.search(r'rezh', quiz_name):
           return 'Режиссер'
        elif re.search(r'сабурово|saburovo', quiz_name):
           return 'Сабурово Клаб'
        elif re.search(r'zhavoron|жаворон', quiz_name):
           return 'Жаворонки Клаб'
        elif re.search(r'rim', quiz_name) and not re.search(r'prime', quiz_name):
           return 'Римский'
        elif re.search(r'rih', quiz_name):
           return 'Рихард'
        elif re.search(r'sidn', quiz_name) and not re.search(r'prime', quiz_name):
           return 'Сидней Сити'
        elif re.search(r'prime', quiz_name):
           return 'Сидней Прайм'
        elif re.search(r'gard', quiz_name):
           return 'Скай Гарден'
        elif re.search(r'skol', quiz_name):
           return 'Сколковский'
        elif re.search(r'olimp|olp', quiz_name):
           return 'Олимп'
        elif re.search(r'molode|mld', quiz_name):
           return 'Молодежный'
        elif re.search(r'aprel', quiz_name):
           return 'Парк Апрель'
        elif re.search(r'sheremet|шеремет', quiz_name):
           return '1-й Шереметьевский'
        elif re.search(r'lake', quiz_name):
            return 'The Lake'
        return f'NaN - {quiz_name}'

    elif placement == 'tch':
        if re.search(r'7999999999|7911111111|700000000|9111111111', contact_phone):
            return 'Тест'
        elif re.search(r'br.*olv', quiz_name):
           return 'Бренд ФСК OLV'
        elif re.search(r'br.*business', quiz_name) and not re.search(r'outlet', quiz_name):
           return 'Бизнес ФСК'
        elif re.search(r'br|fskmain', quiz_name) and not re.search(r'olv|business|outlet', quiz_name):
           return 'Бренд ФСК'
        elif re.search(r'fsk-outlet', quiz_name):
           return 'ФСК Аутлет'
        elif re.search(r'nstr', quiz_name):
           return 'Настроение'
        elif re.search(r'rezh', quiz_name):
           return 'Режиссер'
        elif re.search(r'сабурово|saburovo', quiz_name):
           return 'Сабурово Клаб'
        elif re.search(r'zhavoron|жаворон', quiz_name):
           return 'Жаворонки Клаб'
        elif re.search(r'rim', quiz_name) and not re.search(r'prime', quiz_name):
           return 'Римский'
        elif re.search(r'rih', quiz_name):
           return 'Рихард'
        elif re.search(r'sidn', quiz_name) and not re.search(r'prime', quiz_name):
           return 'Сидней Сити'
        elif re.search(r'prime', quiz_name):
           return 'Сидней Прайм'
        elif re.search(r'gard', quiz_name):
           return 'Скай Гарден'
        elif re.search(r'skol', quiz_name):
           return 'Сколковский'
        elif re.search(r'olimp|olp', quiz_name):
           return 'Олимп'
        elif re.search(r'molode|mld', quiz_name):
           return 'Молодежный'
        elif re.search(r'aprel', quiz_name):
           return 'Парк Апрель'
        elif re.search(r'sheremet|шеремет', quiz_name):
           return '1-й Шереметьевский'
        elif re.search(r'lake', quiz_name):
            return 'The Lake'
        return f'NaN - {quiz_name}'

    elif placement == 'tiktok':
        if re.search(r'7999999999|7911111111|700000000|9111111111|77777777777|79000000000', contact_phone):
            return 'Тест'
        elif re.search(r'br.*olv', quiz_name):
           return 'Бренд ФСК OLV'
        elif re.search(r'rezh', quiz_name):
           return 'Режиссер'
        elif re.search(r'rim', quiz_name) and not re.search(r'prime', quiz_name):
           return 'Римский'
        elif re.search(r'rih', quiz_name):
           return 'Рихард'
        elif re.search(r'sidn', quiz_name) and not re.search(r'prime', quiz_name):
           return 'Сидней Сити'
        elif re.search(r'gard', quiz_name):
            return 'Скай Гарден'
        return f'NaN - {quiz_name}'

    elif placement == 'fb':
        if re.search(r'7999999999|7911111111|700000000', contact_phone):
            return 'Тест'
        elif re.search(r'br.*olv', quiz_name):
           return 'Бренд ФСК OLV'
        elif re.search(r'br.*bus', quiz_name):
           return 'Бизнес ФСК'
        elif re.search(r'br|fskmain', quiz_name) and not re.search(r'olv|bus|outlet', quiz_name):
           return 'Бренд ФСК'
        elif re.search(r'fsk-outlet', quiz_name):
           return 'ФСК Аутлет'
        elif re.search(r'nstr', quiz_name):
           return 'Настроение'
        elif re.search(r'rezh', quiz_name):
           return 'Режиссер'
        elif re.search(r'rim', quiz_name) and not re.search(r'prime', quiz_name):
           return 'Римский'
        elif re.search(r'rih', quiz_name):
           return 'Рихард'
        elif re.search(r'sidn', quiz_name) and not re.search(r'prime', quiz_name):
           return 'Сидней Сити'
        elif re.search(r'prime', quiz_name):
           return 'Сидней Прайм'
        elif re.search(r'gard', quiz_name):
           return 'Скай Гарден'
        elif re.search(r'skol', quiz_name):
           return 'Сколковский'
        elif re.search(r'olimp|olp', quiz_name):
           return 'Олимп'
        elif re.search(r'molode|mld', quiz_name):
            return 'Молодежный'
        return f'NaN - {quiz_name}'

    elif placement == 'yandex':
        if re.search(r'7999999999|7911111111|700000000', contact_phone):
            return 'Тест'
        elif re.search(r' br |fsk context', quiz_name) and not re.search(r'olv|bus|outlet', quiz_name):
            return 'Бренд ФСК'
        return f'NaN - {quiz_name}'

    return 'placement-NaN'
