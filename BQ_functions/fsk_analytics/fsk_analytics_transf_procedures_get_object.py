import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_object(parameter: str) -> str:
    parameter = is_none(parameter)

    # Костыль Flatoutlet
    if re.search(r'flatoutlet|nearby', parameter) and re.search(r'cpa|сра', parameter):
        return 'Бренд ФСК'

    # MGCom
    if re.search(r'vskr|voskresensko|voskresensk|воскресенском|воскресенский', parameter):
        return 'Дом на Воскресенском'
    elif re.search(r'druzhba|дружб', parameter):
       return 'Дружба'
    elif re.search(r'zhavoron|жаворонки', parameter):
       return 'Жаворонки Клаб'
    elif re.search(r'i.ma.lovsk|измайловск|монтажная.*8', parameter):
       return '1-й Измайловский'
    elif re.search(r'comm|novogir|moskovsk|коммер', parameter):
       return 'Коммерческая'
    elif re.search(r'martem|мартем', parameter):
       return 'Мартемьяново Клаб'
    elif re.search(r'mld|molodezhn|молод.жный|калуга|kaluga.18', parameter):
       return 'Молодежный'
    elif re.search(r'nstr|nastr|настроение', parameter):
       return 'Настроение'
    elif re.search(r'olp|olimp|олимп', parameter):
       return 'Олимп'
    elif re.search(r'aprel|парк апрель', parameter):
       return 'Парк Апрель'
    elif re.search(r'pokolen|pkl|поколение', parameter):
       return 'Поколение'
    elif re.search(r'rezh|режисс.р', parameter):
       return 'Режиссер'
    elif re.search(r'_rim|rimsk|римский|развилка| rim ', parameter):
       return 'Римский'
    elif re.search(r'rih|rikh|rixard|рихард', parameter):
       return 'Рихард'
    elif re.search(r'saburovo|сабурово|сабурбер', parameter):
       return 'Сабурово Клаб'
    elif re.search(r'sidn.*prime|sydn.*prime|сидней прайм', parameter):
       return 'Сидней Прайм'
    elif re.search(r'sidn|sydn|sydey|сидней', parameter):
       return 'Сидней Сити'
    elif re.search(r'simonovsk|симоновск', parameter):
       return 'Симоновский'
    elif re.search(r'garden|гарден', parameter):
       return 'Скай Гарден'
    elif re.search(r'skolkovsk|skl| sk |сколк', parameter):
       return 'Сколковский'
    elif re.search(r'himkinsk|химкинский', parameter):
       return '1-й Химкинский'
    elif re.search(r'centraln|центральный', parameter):
       return 'Центральный'
    elif re.search(r'sheremet|шеремет', parameter):
       return '1-й Шереметьевский'
    elif re.search(r'lake|лэйк', parameter):
        return 'The Lake'

    # НЕ MGCom
    if re.search(r'zoom', parameter) and re.search(r'hotel|отель', parameter):
        return 'Best Western Zoom Hotel'
    elif re.search(r'м-хаус|мхаус', parameter):
       return 'М-House'
    elif re.search(r'zoom', parameter) and re.search(r'нев', parameter):
       return 'Zoom на Неве'
    elif re.search(r'zoom', parameter) and re.search(r'ч.рн', parameter):
       return 'Zoom Черная речка'
    elif re.search(r'admiral|адмирал', parameter):
       return 'Адмирал'
    elif re.search(r'amber|амбер', parameter):
       return 'Амбер Сити'
    elif re.search(r'archite.t|arhite.t|архитектор', parameter):
       return 'Архитектор'
    elif re.search(r'белая дача', parameter):
       return 'Белая Дача'
    elif re.search(r'владивосток', parameter) and re.search(r'крылова', parameter):
       return 'Владивосток, Крылова 10'
    elif re.search(r'владивосток', parameter) and re.search(r'философия', parameter):
       return 'Владивосток, Философия'
    elif re.search(r'gagar.nsk|гагаринский', parameter):
       return 'Гагаринский'
    elif re.search(r'datsk|датский', parameter):
       return 'Датский квартал'
    elif re.search(r'govorovo|говорово', parameter):
       return 'Движение Говорово'
    elif re.search(r'dvijen|dvizhen|движение|тушино.*2018', parameter) and re.search(r'hotel|отель', parameter):
       return 'Движение Апарт-отель'
    elif re.search(r'dvijen|dvizhen|движение|тушино.*2018', parameter) and not re.search(r'продвижение', parameter):
       return 'Движение'
    elif re.search(r'domodedovo|домодедово', parameter):
       return 'Домодедово Парк'
    elif re.search(r'donsko|донской', parameter):
       return '1-й Донской'
    elif re.search(r'dyh_|dyhan|дыхание', parameter):
       return 'Дыхание'
    elif re.search(r'западное кунцево', parameter):
       return 'Западное Кунцево'
    elif re.search(r'zarech|заречн', parameter):
       return 'Заречный квартал'
    elif re.search(r'зеленодольск.*октябрьский', parameter):
       return 'Зеленодольск, п. Октябрьский'
    elif re.search(r'зодиак', parameter):
       return 'Зодиак'
    elif re.search(r'квартал 29', parameter):
       return 'Квартал 29'
    elif re.search(r'кожухово', parameter):
       return 'Кожухово паркинг'
    elif re.search(r'komendant|комендант', parameter):
       return 'Комендантский'
    elif re.search(r'мосаэро', parameter):
       return 'Мосаэро'
    elif re.search(r'moskvoreck|москворецк', parameter):
       return 'Москворецкий'
    elif re.search(r'moskovsk|московск', parameter) and not re.search(r'nov|new|новый', parameter):
       return 'Московский'
    elif re.search(r'мфс пик', parameter):
       return 'МФС ПИК'
    elif re.search(r'мясницкая', parameter):
       return 'Мясницкая, д.13'
    elif re.search(r'naberezhn|набережн', parameter):
       return 'На набережной. Орехово-Зуево'
    elif re.search(r'kagan|каган', parameter):
       return 'На улице Кагана'
    elif re.search(r'nekrasov|некрасовка', parameter):
       return 'Некрасовка'
    elif re.search(r'новая пролетарка', parameter):
       return 'Новая Пролетарка'
    elif re.search(r'novogireevsk|новогиреевский', parameter):
       return 'Новогиреевский'
    elif re.search(r'i.ma.lovo|новое измайлово', parameter):
       return 'Новое Измайлово'
    elif re.search(r'novoetushino|novoe(-| )tushino|новое тушино', parameter):
       return 'Новое Тушино'
    elif re.search(r'moskovsk|московск', parameter):
       return 'Новый Московский'
    elif re.search(r'ramensk|раменский', parameter):
       return 'Новый Раменский'
    elif re.search(r'andreevsk|андреевский', parameter):
       return 'Первый Андреевский'
    elif re.search(r'leningradsk|lerningradsk|ленинградский|молжаниново|1-len', parameter):
       return 'Первый Ленинградский'
    elif re.search(r'лермонтовский|lerm', parameter):
       return 'Первый Лермонтовский'
    elif re.search(r'юбилейный', parameter):
       return 'Первый Юбилейный'
    elif re.search(r'программы урвн', parameter):
       return 'Программы УРВН'
    elif re.search(r'pushkinsk|пушкинск', parameter):
       return 'Пушкинский'
    elif re.search(r'путилково', parameter):
       return 'Путилково (ДСК)'
    elif re.search(r'rotterdam|роттердам', parameter):
       return 'Роттердам'
    elif re.search(r'саларьево', parameter):
       return 'Саларьево'
    elif re.search(r'саларьевский', parameter):
       return '1-й Саларьевский'
    elif re.search(r'svetlanovsk|светлановск', parameter):
       return 'Светлановский'
    elif re.search(r'skand|скандинавский', parameter):
       return 'Скандинавский'
    elif re.search(r'solncevo|солнцево', parameter):
       return 'Солнцево'
    elif re.search(r'столичный квартал', parameter):
       return 'Столичный квартал'
    elif (re.search(r'flagman|флагман', parameter) and re.search(r'vladivost|владивосток|горшкова', parameter)) or re.search(r'владивосток.*горшкова', parameter):
       return 'Флагман Владивосток'
    elif re.search(r'flagman|флагман|раменское', parameter):
       return 'Флагман'
    elif re.search(r'форест', parameter):
       return 'ФоРест'
    elif re.search(r'centr(_|.2|2)|центр(.2|2)', parameter):
       return 'Центр-2'
    elif re.search(r'bit.a|битца', parameter):
       return 'Южная Битца'
    elif re.search(r'южное кучино', parameter):
       return 'Южное Кучино-2'
    elif re.search(r'uzhn|южный', parameter):
       return '1-й Южный'
    elif re.search(r'asenevsk|asenesk|ясеневский|мамыри', parameter):
       return '1-й Ясеневский'
    elif re.search(r'^up$', parameter):
        return 'UP'

    # ФСК и ДСК Бренды
    if re.search(r'btl|бтл', parameter):
        return 'Движение BTL'
    elif re.search(r'вторич', parameter):
       return 'Вторичная недвижимость'
    elif re.search(r'кладовые', parameter):
       return 'Кладовые'
    elif re.search(r'машиноместа', parameter):
       return 'Машиноместа'
    elif re.search(r'realist|реалист', parameter):
       return 'Реалист'
    elif re.search(r'спецпроект', parameter):
       return 'Спецпроект'
    elif re.search(r'трейд-ин', parameter):
       return 'Трейд-Ин'
    elif re.search(r'business|бизнес', parameter) and not re.search(r'outlet|аутлет', parameter):
       return 'Бизнес ФСК'
    elif re.search(r'fsk(_|-)olv|olv.*fsk|brand.*olv|бренд фск.*olv|бренд olv', parameter):
       return 'Бренд ФСК OLV'
    elif re.search(r'fsk-outlet|аутлет', parameter):
       return 'ФСК Аутлет'
    elif re.search(r'brand|_fsk_|soc_fsk-|fsk lider|fsk.*недвижимость|fsk.*ретаргетинг|бренд фск|fsk.*ipoteka|фск.*лидер|фск', parameter) and not re.search(r'dsk|дск', parameter):
       return 'Бренд ФСК'
    elif re.search(r'застройщика|zastroishchika|zastroishchik-gk-fsk', parameter):
       return 'Бренд ФСК'
    elif (re.search(r'(_| |-)dsk|dsk(_| |-)| дск|дск |дск-1|дск1', parameter) or parameter == 'dsk') and not re.search(r'olv|bitca', parameter):
       return 'Бренд ДСК'
    elif re.search(r'dsk|дск', parameter) and re.search(r'olv', parameter):
        return 'Бренд ДСК OLV'

    return 'NaN'

