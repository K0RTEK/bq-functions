import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_object_campaign(channel: str, campaign: str) -> str:
    channel = is_none(channel)
    campaign = is_none(campaign)

    if channel == 'Реклама в соц.сетях':
        if re.search(r'dvijen|dvizhen|движение', campaign) and re.search(r'btl', campaign):
            return 'Движение BTL'
        elif re.search(r'archite.t|arhite.t|архитектор', campaign):
           return 'Архитектор'
        elif re.search(r'gagar.nsk|гагаринский', campaign):
           return 'Гагаринский'
        elif re.search(r'datsk|датский', campaign):
           return 'Датский квартал'
        elif re.search(r'dvijen|dvizhen|движение', campaign) and not re.search(r'btl|говорово|govorovo',
                                                                                    campaign):
           return 'Движение'
        elif re.search(r'govorovo|говорово', campaign):
           return 'Движение Говорово'
        elif re.search(r'domodedovo|домодедово', campaign):
           return 'Домодедово Парк'
        elif re.search(r'dyh_|dyhan|дыхание', campaign):
           return 'Дыхание'
        elif re.search(r'moskvoreck|москворецк', campaign):
           return 'Москворецкий'
        elif re.search(r'nekrasov|некрасовка', campaign):
           return 'Некрасовка'
        elif re.search(r'novogireevsk|новогиреевский', campaign):
           return 'Новогиреевский'
        elif re.search(r'novoetushino|novoe(-| )tushino|новое тушино', campaign):
           return 'Новое Тушино'
        elif re.search(r'ramensk|раменский', campaign):
           return 'Новый Раменский'
        elif re.search(r'andreevsk|андреевский', campaign):
           return 'Первый Андреевский'
        elif re.search(r'le(n|rn)ingradsk|ленинградский', campaign):
           return 'Первый Ленинградский'
        elif re.search(r'lermontovsk|лермонтовский|1-lerm', campaign):
           return 'Первый Лермонтовский'
        elif re.search(r'donsko|донской', campaign):
           return '1-й Донской'
        elif re.search(r'uzhniy|южный', campaign):
           return '1-й Южный'
        elif re.search(r'юбилейный', campaign):
           return 'Первый Юбилейный'
        elif re.search(r'rotterdam|роттердам', campaign):
           return 'Роттердам'
        elif re.search(r'skand|скандинавский', campaign):
           return 'Скандинавский'
        elif re.search(r'solncevo', campaign):
           return 'Солнцево'
        elif re.search(r'flagman|флагман', campaign):
           return 'Флагман'
        elif re.search(r'centr(_|.2|2)|центр(.2|2)', campaign):
           return 'Центр-2'
        elif re.search(r'bit.a|битца', campaign):
           return 'Южная Битца'
        elif re.search(r'(_| |-)dsk|dsk(_| |-)| дск|дск ', campaign) and not re.search(r'olv|bitca',
                                                                                            campaign):
           return 'Бренд ДСК'
        elif re.search(r'dsk|дск', campaign) and re.search(r'olv', campaign):
           return 'Бренд ДСК OLV'
        elif re.search(r'коммер|comm', campaign):
           return 'Коммерческая'
        elif re.search(r'voskresensk|воскресенском', campaign) and not re.search(r'centr|центр',
                                                                                      campaign):
           return 'Дом на Воскресенском'
        elif re.search(r'molodezhn|молод.жный', campaign):
           return 'Молодежный'
        elif re.search(r'nastroen|(-| |_)nstr|nstr(-| |_)|настроение', campaign):
           return 'Настроение'
        elif re.search(r'olimp|олимп', campaign):
           return 'Олимп'
        elif re.search(r'druzhba|дружба', campaign):
           return 'Дружба'
        elif re.search(r'lake', campaign):
           return 'The Lake'
        elif re.search(r'aprel|парк апрель', campaign):
           return 'Парк Апрель'
        elif re.search(r'zhavoronk|жаворонки', campaign):
           return 'Жаворонки Клаб'
        elif re.search(r'sheremet|шеремет', campaign):
           return '1-й Шереметьевский'
        elif re.search(r'pokolen|поколение', campaign):
           return 'Поколение'
        elif re.search(r'rezh|режис', campaign):
           return 'Режиссер'
        elif re.search(r'_rim|римский|rim_|rimsk', campaign):
           return 'Римский'
        elif re.search(r'rih|рихард', campaign):
           return 'Рихард'
        elif re.search(r'saburovo|сабурово', campaign):
           return 'Сабурово Клаб'
        elif re.search(r's.dn|сидней|sydey', campaign) and not re.search(r'-prime', campaign):
           return 'Сидней Сити'
        elif re.search(r's.dn.*-prime', campaign):
           return 'Сидней Прайм'
        elif re.search(r'skygarden|sky garden', campaign):
           return 'Скай Гарден'
        elif re.search(r'skl|skol|сколковский', campaign):
           return 'Сколковский'
        elif re.search(r'centraln.*voskr|центральный.*воскресенск', campaign):
           return 'Центральный Воскресенск'
        elif re.search(r'centraln.*noginsk|центральный.*ногинск', campaign):
           return 'Центральный Ногинск'
        elif re.search(r'realist|реалист', campaign):
           return 'Реалист'
        elif re.search(r'fsk|фск|brand|tec-00012', campaign) and not re.search(
               r'business|olv|dsk|brand-b|дск|outlet|аутлет', campaign):
           return 'Бренд ФСК'
        elif re.search(r'fsk|фск|brand|бренд', campaign) and re.search(r'olv', campaign):
           return 'Бренд ФСК OLV'
        elif re.search(r'fsk.*business|brand-b|бизнес', campaign) and not re.search(r'outlet', campaign):
           return 'Бизнес ФСК'
        elif re.search(r'fsk-outlet|аутлет', campaign):
            return 'ФСК Аутлет'
        return f'NaN - {campaign}'

    elif channel == 'Контекстная реклама':
        if re.search(r'dvijen|dvizhen|движение|бтл-дв|btl-dv', campaign) and re.search(r'btl|бтл',
                                                                                               campaign):
            return 'Движение BTL'
        if re.search(r'admiral|адмирал', campaign):
            return 'Адмирал'
        elif re.search(r'archite.t|arhite.t|архитектор', campaign):
           return 'Архитектор'
        elif re.search(r'gagar.nsk|гагаринский', campaign):
           return 'Гагаринский'
        elif re.search(r'datsk|датский', campaign):
           return 'Датский квартал'
        elif re.search(r'dvijen|dvizhen|движение', campaign) and not re.search(r'btl|говорово|govorovo',
                                                                                    campaign):
           return 'Движение'
        elif re.search(r'govorovo|говорово', campaign):
           return 'Движение Говорово'
        elif re.search(r'domodedovo|домодедово', campaign):
           return 'Домодедово Парк'
        elif re.search(r'dyh_|d(y|i)han|дыхание', campaign):
           return 'Дыхание'
        elif re.search(r'moskvoreck|москворецк', campaign):
           return 'Москворецкий'
        elif re.search(r'на-набережной', campaign):
           return 'На набережной'
        elif re.search(r'nekrasov|некрасовка', campaign):
           return 'Некрасовка'
        elif re.search(r'novogireevsk|новогиреевский|balash', campaign):
           return 'Новогиреевский'
        elif re.search(r'novoetushino|novoe(-| )tushino|новое тушино|tyshino', campaign):
           return 'Новое Тушино'
        elif re.search(r'ramensk|раменский', campaign):
           return 'Новый Раменский'
        elif re.search(r'andreev|андреевский', campaign):
           return 'Первый Андреевский'
        elif re.search(r'le(n|rn)ing(r|t)adsk|ленинградский', campaign):
           return 'Первый Ленинградский'
        elif re.search(r'ler(m|mm)ontovsk|лермонтовский|1-lerm', campaign):
           return 'Первый Лермонтовский'
        elif re.search(r'donsko|донской', campaign):
           return '1-й Донской'
        elif re.search(r'uzhniy|южный', campaign):
           return '1-й Южный'
        elif re.search(r'юбилейный|bile.n', campaign):
           return 'Первый Юбилейный'
        elif re.search(r'rotterdam|роттердам', campaign):
           return 'Роттердам'
        elif re.search(r'skand|скандинавский', campaign):
           return 'Скандинавский'
        elif re.search(r'flagman|флагман', campaign):
           return 'Флагман'
        elif re.search(r'centr(_|.2|2)|центр(.2|2)', campaign):
           return 'Центр-2'
        elif re.search(r'bit.a|битца', campaign):
           return 'Южная Битца'
        elif re.search(r'(_| |-)dsk|dsk(_| |-)| дск|дск ', campaign) and not re.search(r'olv|bitca|вдск',
                                                                                            campaign):
           return 'Бренд ДСК'
        elif re.search(r'dsk|дск', campaign) and re.search(r'olv', campaign):
           return 'Бренд ДСК OLV'
        elif re.search(r'коммер|comm', campaign):
           return 'Коммерческая'
        elif re.search(r'voskresensk|воскресенском', campaign) and not re.search(r'centr|центр',
                                                                                      campaign):
           return 'Дом на Воскресенском'
        elif re.search(r'дружба|druzhba', campaign):
           return 'Дружба'
        elif re.search(r'molodezhn|молод.жный', campaign):
           return 'Молодежный'
        elif re.search(r'nastroen|nstr_|настроение', campaign):
           return 'Настроение'
        elif re.search(r'olimp|олимп', campaign):
           return 'Олимп'
        elif re.search(r'lake', campaign):
           return 'The Lake'
        elif re.search(r'aprel|парк апрель', campaign):
           return 'Парк Апрель'
        elif re.search(r'zhavoron|жаворонки', campaign):
           return 'Жаворонки Клаб'
        elif re.search(r'1.shereme|1shereme|шереметьевский', campaign):
           return '1-й Шереметьевский'
        elif re.search(r'pokolen|pkl|поколение', campaign):
           return 'Поколение'
        elif re.search(r'rezh|режис', campaign):
           return 'Режиссер'
        elif re.search(r'rim_|rimsk|римский|развилка', campaign):
           return 'Римский'
        elif re.search(r'rih_|rihard|rikhard|рихард', campaign):
           return 'Рихард'
        elif re.search(r's.dn|сидней|sydey', campaign) and not re.search(r'-prime', campaign):
           return 'Сидней Сити'
        elif re.search(r's.dn.*-prime', campaign):
           return 'Сидней Прайм'
        elif re.search(r'сабурово|saburovo', campaign):
           return 'Сабурово Клаб'
        elif re.search(r'skygarden|sky garden|скай( г|г)арден', campaign):
           return 'Скай Гарден'
        elif re.search(r'skl_|_skl|skol|сколк', campaign):
           return 'Сколковский'
        elif re.search(r'centraln.*voskr|центральный.*воскресенск', campaign):
           return 'Центральный Воскресенск'
        elif re.search(r'centraln.*noginsk|центральный.*ногинск', campaign):
           return 'Центральный Ногинск'
        elif re.search(r'реалист|realist', campaign):
           return 'Реалист'
        elif re.search(r'fsk|фск|brand|brend|бренд|outlet|аутлет', campaign) and re.search(
               r'mg_ya_|mg \| контекст', campaign) and not re.search(r'business|olv|dsk|brand-b|дск',
                                                                             campaign):
           return 'Бренд ФСК'
        elif re.search(r'fsk|фск|brand|brend|бренд', campaign) and re.search(r'olv', campaign):
           return 'Бренд ФСК OLV'
        elif re.search(r'fsk.*business|бизнес|business-class', campaign) and not re.search(r'outlet',
                                                                                                campaign):
           return 'Бизнес ФСК'
        elif re.search(r'test', campaign) and not re.search(r'outlet', campaign):
            return 'Тест'
        return f'NaN - {campaign}'

    return 'NaN'
