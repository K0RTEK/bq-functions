import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_object(parameter):
    parameter = is_none(parameter)
    if re.search(r'realist', parameter):
        return 'Реалист'
    elif re.search(r'business|бизнес', parameter) and not re.search(r'outlet', parameter):
        return 'Бизнес ФСК'
    elif re.search(r'fsk(_|-)olv|olv(-|_)fsk|brand.*olv|бренд фск.*olv|бренд olv', parameter):
        return 'Бренд ФСК OLV'
    elif re.search(r'fsk-outlet|аутлет', parameter):
        return 'ФСК Аутлет'
    elif re.search(r'brand|_soc_fsk_|soc_fsk-|fsk lider|бренд фск', parameter) and re.search(
            r'^mg|fsk.*недвижимость|fsk.*ретаргетинг', parameter):
        return 'Бренд ФСК'
    elif re.search(r'vskr|voskresensko|воскресенском|воскресенский', parameter):
        return 'Дом на Воскресенском'
    elif re.search(r'druzhba|дружба', parameter):
        return 'Дружба'
    elif re.search(r'zhavoron|жаворонки', parameter):
        return 'Жаворонки Клаб'
    elif re.search(r'comm|novogir|moskovsk|коммер', parameter):
        return 'Коммерческая'
    elif re.search(r'mld|molodezhn|молодежный', parameter):
        return 'Молодежный'
    elif re.search(r'nstr|nastr|настроение', parameter):
        return 'Настроение'
    elif re.search(r'olp|olimp|олимп', parameter):
        return 'Олимп'
    elif re.search(r'aprel|парк апрель', parameter):
        return 'Парк Апрель'
    elif re.search(r'pokolen|pkl|поколение', parameter):
        return 'Поколение'
    elif re.search(r'rezh|ежисс', parameter):
        return 'Режиссер'
    elif re.search(r'_rim|rimsk|римский', parameter):
        return 'Римский'
    elif re.search(r'rih|rikh|рихард', parameter):
        return 'Рихард'
    elif re.search(r'saburovo-club|сабурово', parameter):
        return 'Сабурово Клаб'
    elif re.search(r'sidn.*prime|sydn.*prime|сидней прайм', parameter):
        return 'Сидней Прайм'
    elif re.search(r'sidn|sydn|сидней', parameter):
        return 'Сидней Сити'
    elif re.search(r'garden|гарден', parameter):
        return 'Скай Гарден'
    elif re.search(r'skolkovsk|skl|сколковский', parameter):
        return 'Сколковский'
    elif re.search(r'центральный', parameter):
        return 'Центральный'
    elif re.search(r'sheremet|шереметьевский', parameter):
        return 'Первый Шереметьевский'
    elif re.search(r'lake', parameter):
        return 'The Lake'
    elif re.search(r'ясеневский', parameter):
        return '1-й Ясеневский'
    elif re.search(r'измайловский|измаиловский', parameter):
        return '1-й Измайловский'
    elif re.search(r'жк для номера на лендинге|спецпроект', parameter):
        return 'Спецпроект'
    elif re.search(r'dsk|дск', parameter) and re.search(r'olv', parameter):
        return 'Бренд ДСК OLV'
    elif (re.search(r'(_| |-)dsk|dsk(_| |-)| дск|дск ', parameter) or parameter == 'dsk') and not re.search(
            r'olv|bitca', parameter):
        return 'Бренд ДСК'
    elif re.search(r'dvijen|dvizhen|движение', parameter) and re.search(r'btl', parameter):
        return 'Движение BTL'
    elif re.search(r'archite.t|arhite.t|архитектор', parameter):
        return 'Архитектор'
    elif re.search(r'gagar.nsk|гагаринский', parameter):
        return 'Гагаринский'
    elif re.search(r'datsk|датский', parameter):
        return 'Датский квартал'
    elif re.search(r'dvijen|dvizhen|движение', parameter) and not re.search(r'btl|говорово|govorovo',
                                                                                  parameter):
        return 'Движение'
    elif re.search(r'govorovo|говорово', parameter):
        return 'Движение Говорово'
    elif re.search(r'domodedovo|домодедово', parameter):
        return 'Домодедово Парк'
    elif re.search(r'donsko|донской', parameter):
        return 'Первый Донской'
    elif re.search(r'dyh_|dyhan|дыхание', parameter):
        return 'Дыхание'
    elif re.search(r'moskvoreck|москворецк', parameter):
        return 'Москворецкий'
    elif re.search(r'nekrasov|некрасовка', parameter):
        return 'Некрасовка'
    elif re.search(r'novogireevsk|новогиреевский', parameter):
        return 'Новогиреевский'
    elif re.search(r'novoetushino|novoe(-| )tushino|новое тушино', parameter):
        return 'Новое Тушино'
    elif re.search(r'ramensk|раменский', parameter):
        return 'Новый Раменский'
    elif re.search(r'andreevsk|андреевский', parameter):
        return 'Первый Андреевский'
    elif re.search(r'le(n|rn)ingradsk|ленинградский', parameter):
        return 'Первый Ленинградский'
    elif re.search(r'lermontovsk|лермонтовский|1-lerm', parameter):
        return 'Первый Лермонтовский'
    elif re.search(r'юбилейный', parameter):
        return 'Первый Юбилейный'
    elif re.search(r'rotterdam|роттердам', parameter):
        return 'Роттердам'
    elif re.search(r'skand|скандинавский', parameter):
        return 'Скандинавский'
    elif re.search(r'solncevo|солнцево', parameter):
        return 'Солнцево'
    elif re.search(r'flagman|флагман', parameter):
        return 'Флагман'
    elif re.search(r'centr(_|.2|2)|центр(.2|2)', parameter):
        return 'Центр-2'
    elif re.search(r'bit.a|битца', parameter):
        return 'Южная Битца'
    elif re.search(r'uzhniy|южный', parameter):
        return 'Первый Южный'
    return 'Неизвестный'
