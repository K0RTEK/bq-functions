import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_client(object_name: str) -> str:
    object_name = is_none(object_name)

    # Проверка для 'ДСК'
    if re.search(r'южная битца|(первый|1).*ленинградский|(первый|1).*лермонтовский|донской|шереметьевский|южный|ясеневский|измайловский|химкинский|саларьевский', object_name):
        return 'ДСК'

    # Проверка для 'ФСК Калуга'
    if re.search(r'олимп|дружба|молод.жный', object_name):
        return 'ФСК Калуга'

    # Проверка для 'ФСК'
    if re.search(r'настроение|новый раменский|скай гарден|sky garden|skygarden|сколковский|спецпроект|роттердам|rotterdam|сидней сити|s.dney city|архитектор|датский квартал|режисс.р|римский|рихард|скандинавский|движение|жк для номера на лендинге|апрель|lake|сабурово|жаворонки|prime|прайм|амбер|amber|мартем', object_lower):
        return 'ФСК'

    # Если объект не подходит ни под одно условие, возвращаем 'NaN - объект'
    return f'NaN - {object_name}'
