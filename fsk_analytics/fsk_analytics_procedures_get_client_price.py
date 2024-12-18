import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_client_price(object):
    object = is_none(object)
    if re.search(r'южная битца|(первый|1).*ленинградский|(первый|1).*лермонтовский|донской|шереметьевский|южный|ясеневский|измайловский', object):
        return 'ДСК'
    if re.search(r'олимп|дружба|молод.жный', object):
        return 'ФСК Калуга'
    if re.search(r'настроение|новый раменский|скай гарден|sky garden|skygarden|сколковский|спецпроект|роттердам|rotterdam|сидней сити|s.dney city|архитектор|датский квартал|режисс.р|римский|рихард|скандинавский|движение|жк для номера на лендинге|апрель|lake|сабурово|жаворонки|prime|прайм', object):
        return 'ФСК'
    return f'NaN - {object}'