import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_object_cabinet(placement, parameter):
    placement = is_none(placement)
    parameter = is_none(parameter)

    if placement == 'vkontakte':
        if re.search(r'realist', parameter):
            return 'Реалист'
        elif re.search(r'brand|_soc_fsk_|soc_fsk-', parameter) and re.search(r'mg_ya_|mg \| контекст',
                                                                                   parameter) and not re.search(
                r'fsk_olv|brand-olv|olv-fsk|outlet', parameter):
            return 'Бренд ФСК'
        elif re.search(r'business', parameter) and not re.search(r'outlet', parameter):
            return 'Бизнес ФСК'
        elif re.search(r'fsk(_|-)olv|brand-olv|olv(-|_)fsk', parameter):
            return 'Бренд ФСК OLV'
        elif re.search(r'fsk-outlet', parameter):
            return 'ФСК Аутлет'
        elif re.search(r'comm|novogir|moskovsk', parameter):
            return 'Коммерческая'
        elif re.search(r'mld|molodezhn', parameter):
            return 'Молодежный'
        elif re.search(r'nstr|nastr', parameter):
            return 'Настроение'
        elif re.search(r'olp|olimp', parameter):
            return 'Олимп'
        elif re.search(r'aprel', parameter):
            return 'Парк Апрель'
        elif re.search(r'zhavoron', parameter):
            return 'Жаворонки Клаб'
        elif re.search(r'sheremet', parameter):
            return '1-й Шереметьевский'
        elif re.search(r'donsko', parameter):
            return '1-й Донской'
        elif re.search(r'rezh', parameter):
            return 'Режиссер'
        elif re.search(r'rih', parameter):
            return 'Рихард'
        elif re.search(r'_rim', parameter):
            return 'Римский'
        elif re.search(r'vskr|voskresensk', parameter):
            return 'Дом на Воскресенском'
        elif re.search(r'saburovo-club', parameter):
            return 'Сабурово Клаб'
        elif re.search(r'sidn|sydn', parameter) and not re.search(r'-prime', parameter):
            return 'Сидней Сити'
        elif re.search(r'sidn.*-prime|sydn.*-prime', parameter):
            return 'Сидней Прайм'
        elif re.search(r'pokolen|pkl', parameter):
            return 'Поколение'
        elif re.search(r'skygarden', parameter):
            return 'Скай Гарден'
        elif re.search(r'skolkovsk|skl', parameter):
            return 'Сколковский'
        elif re.search(r'druzhba', parameter):
            return 'Дружба'
        elif re.search(r'lake', parameter):
            return 'The Lake'
        return f'NaN - {parameter}'

    elif placement in ('vkr', 'vk reklama'):
        if re.search(r'realist', parameter):
            return 'Реалист'
        elif re.search(r'brand|_soc_fsk_|soc_fsk-', parameter) and not re.search(
                r'fsk_olv|brand-olv|olv-fsk|outlet', parameter):
            return 'Бренд ФСК'
        elif re.search(r'business', parameter) and not re.search(r'outlet', parameter):
            return 'Бизнес ФСК'
        elif re.search(r'fsk(_|-)olv|brand-olv|olv(-|_)fsk', parameter):
            return 'Бренд ФСК OLV'
        elif re.search(r'fsk-outlet', parameter):
            return 'ФСК Аутлет'
        elif re.search(r'comm|novogir|moskovsk', parameter):
            return 'Коммерческая'
        elif re.search(r'mld|molodezhn', parameter):
            return 'Молодежный'
        elif re.search(r'nstr|nastr', parameter):
            return 'Настроение'
        elif re.search(r'olp|olimp', parameter):
            return 'Олимп'
        elif re.search(r'aprel', parameter):
            return 'Парк Апрель'
        elif re.search(r'zhavoron', parameter):
            return 'Жаворонки Клаб'
        elif re.search(r'sheremet', parameter):
            return '1-й Шереметьевский'
        elif re.search(r'donsko', parameter):
            return '1-й Донской'
        elif re.search(r'rezh', parameter):
            return 'Режиссер'
        elif re.search(r'rih', parameter):
            return 'Рихард'
        elif re.search(r'_rim', parameter):
            return 'Римский'
        elif re.search(r'vskr|voskresensk', parameter):
            return 'Дом на Воскресенском'
        elif re.search(r'saburovo-club', parameter):
            return 'Сабурово Клаб'
        elif re.search(r'sidn|sydn', parameter) and not re.search(r'-prime', parameter):
            return 'Сидней Сити'
        elif re.search(r'sidn.*-prime|sydn.*-prime', parameter):
            return 'Сидней Прайм'
        elif re.search(r'pokolen|pkl', parameter):
            return 'Поколение'
        elif re.search(r'skygarden', parameter):
            return 'Скай Гарден'
        elif re.search(r'skolkovsk|skl', parameter):
            return 'Сколковский'
        elif re.search(r'druzhba', parameter):
            return 'Дружба'
        elif re.search(r'lake', parameter):
            return 'The Lake'
        return f'NaN - {parameter}'

    elif placement == 'mytarget':
        if re.search(r'realist', parameter):
            return 'Реалист'
        elif re.search(r'_fsk-business_') and not re.search(r'outlet', parameter):
            return 'Бизнес ФСК'
        elif re.search(r'_fsk_|brand_|_fsk-') and not re.search(r'brand_olv|brand-olv|olv-fsk|outlet', parameter):
            return 'Бренд ФСК'
        elif re.search(r'fsk(_|-)olv|brand(_|-)olv|olv(-|_)fsk', parameter):
            return 'Бренд ФСК OLV'
        elif re.search(r'fsk-outlet', parameter):
            return 'ФСК Аутлет'
        elif re.search(r'comm', parameter):
            return 'Коммерческая'
        elif re.search(r'mld|molodezhn', parameter):
            return 'Молодежный'
        elif re.search(r'nastroen|nstr', parameter):
            return 'Настроение'
        elif re.search(r'olimp', parameter):
            return 'Олимп'
        elif re.search(r'aprel', parameter):
            return 'Парк Апрель'
        elif re.search(r'zhavoron', parameter):
            return 'Жаворонки Клаб'
        elif re.search(r'sheremet', parameter):
            return '1-й Шереметьевский'
        elif re.search(r'donsko', parameter):
            return '1-й Донской'
        elif re.search(r'pokolen', parameter):
            return 'Поколение'
        elif re.search(r'rezh', parameter):
            return 'Режиссер'
        elif re.search(r'rih', parameter):
            return 'Рихард'
        elif re.search(r'_rim', parameter):
            return 'Римский'
        elif re.search(r'saburovo-club', parameter):
            return 'Сабурово Клаб'
        elif re.search(r'sidn|sydn', parameter) and not re.search(r'-prime', parameter):
            return 'Сидней Сити'
        elif re.search(r'sidn.*-prime|sydn.*-prime', parameter):
            return 'Сидней Прайм'
        elif re.search(r'skl|skolkovsk', parameter):
            return 'Сколковский'
        elif re.search(r'voskresensk', parameter):
            return 'Дом на Воскресенском'
        elif re.search(r'skygarden', parameter):
            return 'Скай Гарден'
        elif re.search(r'druzhba', parameter):
            return 'Дружба'
        elif re.search(r'lake', parameter):
            return 'The Lake'
        return f'NaN - {parameter}'

    elif placement == 'tiktok':
        if re.search(r'realist', parameter):
            return 'Реалист'
        elif re.search(r'olv(-|_)fsk|brand-olv|fsk(_|-)olv', parameter):
            return 'Бренд ФСК OLV'
        elif re.search(r'_soc_fsk-business_', parameter):
            return 'Бизнес ФСК'
        elif re.search(r'_soc_fsk_|brand', parameter) and not re.search(r'olv-fsk|brand-olv|brand-fsk_olv',
                                                                              parameter):
            return 'Бренд ФСК'
        elif re.search(r'voskresensk', parameter):
            return 'Дом на Воскресенском'
        elif re.search(
                r'commerc|com_|fsk_auc|_bitsa_|datsk|nekrasovka|novogirievsk|dyhan|lerm|skandinav|solncevo|centr2|centr|ramensk|moskovsk|tushino',
                parameter):
            return 'Коммерческая'
        elif re.search(r'molode', parameter):
            return 'Молодежный'
        elif re.search(r'nastroen|nstr', parameter):
            return 'Настроение'
        elif re.search(r'olimp', parameter):
            return 'Олимп'
        elif re.search(r'pkl|pokolenie', parameter):
            return 'Поколение'
        elif re.search(r'rezh', parameter):
            return 'Режиссер'
        elif re.search(r'_rim', parameter):
            return 'Римский'
        elif re.search(r'rih', parameter):
            return 'Рихард'
        elif re.search(r'sidn|sydn', parameter) and not re.search(r'-prime', parameter):
            return 'Сидней Сити'
        elif re.search(r'sidn.*-prime|sydn.*-prime', parameter):
            return 'Сидней Прайм'
        elif re.search(r'skygarden', parameter):
            return 'Скай Гарден'
        elif re.search(r'skolkovsk|_skl', parameter):
            return 'Сколковский'
        elif re.search(r'druzhba', parameter):
            return 'Дружба'
        elif re.search(r'lake', parameter):
            return 'The Lake'
        return f'NaN - {parameter}'

    elif placement == 'facebook':
        if re.search(r'realist', parameter):
            return 'Реалист'
        elif re.search(r'olv(-|_)fsk|brand-olv|fsk(_|-)olv', parameter):
            return 'Бренд ФСК OLV'
        elif re.search(r'_soc_fsk-business_|soc_business-fsk', parameter):
            return 'Бизнес ФСК'
        elif re.search(r'_soc_fsk_|brand', parameter) and not re.search(r'olv-fsk|brand-olv|brand-fsk_olv',
                                                                              parameter):
            return 'Бренд ФСК'
        elif re.search(r'voskresensk', parameter):
            return 'Дом на Воскресенском'
        elif re.search(
                r'commerc|com_|fsk_auc|_bitsa_|datsk|nekrasovka|novogirievsk|dyhan|lerm|skandinav|solncevo|centr2|centr|ramensk|moskovsk|tushino',
                parameter):
            return 'Коммерческая'
        elif re.search(r'molode', parameter):
            return 'Молодежный'
        elif re.search(r'nastroen|nstr', parameter):
            return 'Настроение'
        elif re.search(r'olimp', parameter):
            return 'Олимп'
        elif re.search(r'pkl|pokolenie', parameter):
            return 'Поколение'
        elif re.search(r'rezh', parameter):
            return 'Режиссер'
        elif re.search(r'_rim', parameter):
            return 'Римский'
        elif re.search(r'rih', parameter):
            return 'Рихард'
        elif re.search(r'sidn|sydn', parameter) and not re.search(r'prime', parameter):
            return 'Сидней Сити'
        elif re.search(r'sidn.*-prime|sydn.*-prime', parameter):
            return 'Сидней Прайм'
        elif re.search(r'skygarden', parameter):
            return 'Скай Гарден'
        elif re.search(r'skolkovsk|_skl', parameter):
            return 'Сколковский'
        elif re.search(r'druzhba', parameter):
            return 'Дружба'
        elif re.search(r'lake', parameter):
            return 'The Lake'
        return f'NaN - {parameter}'

    elif placement == 'yandex':
        if re.search(r'fsk-the-lake', parameter):
            return 'The Lake'
        elif re.search(r'fsk-olimp-obninsk', parameter):
            return 'Олимп'
        elif re.search(r'fsk-rezhisser', parameter):
            return 'Режиссер'
        elif re.search(r'fsk-voskresensky', parameter):
            return 'Дом на Воскресенском'
        elif re.search(r'fsk-druzhba', parameter):
            return 'Дружба'
        elif re.search(r'fsk-pokolenie', parameter):
            return 'Поколение'
        elif re.search(r'fsk-rihard', parameter):
            return 'Рихард'
        elif re.search(r'fsk-molodezhniy', parameter):
            return 'Молодежный'
        elif re.search(r'fsk-skolkovsky', parameter):
            return 'Сколковский'
        elif re.search(r'ipro-fsk-nastroenie', parameter):
            return 'Настроение'
        elif re.search(r'fsk-park-aprel', parameter):
            return 'Парк Апрель'
        elif re.search(r'fsk-zhavoronki-club', parameter):
            return 'Жаворонки Клаб'
        elif re.search(r'dsk-1sheremet', parameter):
            return '1-й Шереметьевский'
        elif re.search(r'fsk-rimskiy', parameter):
            return 'Римский'
        elif re.search(r'fsk-sydney-city', parameter) and not re.search(r's.dn.*-prime', parameter):
            return 'Сидней Сити'
        elif re.search(r'fsk-sydney-city.*s.dn.*-prime', parameter):
            return 'Сидней Прайм'
        elif re.search(r'fsk-saburovo-club-mo', parameter):
            return 'Сабурово Клаб'
        elif re.search(r'fsk-sky-garden', parameter):
            return 'Скай Гарден'
        elif re.search(r'fsk-brand', parameter):
            if re.search(r'realist', parameter):
                return 'Реалист'
            elif re.search(r'olv', parameter):
                return 'Бренд ФСК OLV'
            elif re.search(r'business', parameter) and not re.search(r'outlet', parameter):
                return 'Бизнес ФСК'
            return 'Бренд ФСК'
        return f'NaN - {parameter}'

    elif placement == 'google':
        if re.search(r'ВОСКРЕСЕНСКИЙ', parameter):
            return 'Дом на Воскресенском'
        elif re.search(r'НОВОГИРЕЕВСКИЙ', parameter):
            return 'Новогиреевский'
        elif re.search(r'ДРУЖБА', parameter):
            return 'Дружба'
        elif re.search(r'ПОКОЛЕНИЕ', parameter):
            return 'Поколение'
        elif re.search(r'РИМСКИЙ', parameter):
            return 'Римский'
        elif re.search(r'РЕЖИССЁР', parameter):
            return 'Режиссер'
        elif re.search(r'МОЛОДЁЖНЫЙ', parameter):
            return 'Молодежный'
        elif re.search(r'СКОЛКОВСКИЙ', parameter):
            return 'Сколковский'
        elif re.search(r'БРЕНД ФСК', parameter):
            if re.search(r'realist', parameter):
                return 'Реалист'
            elif re.search(r'olv', parameter):
                return 'Бренд ФСК OLV'
            elif re.search(r'business', parameter) and not re.search(r'outlet', parameter):
                return 'Бизнес ФСК'
            return 'Бренд ФСК'
        elif re.search(r'СИДНЕЙ СИТИ', parameter):
          return 'Сидней Сити'
        elif re.search(r'ОЛИМП', parameter):
          return 'Олимп'
        elif re.search(r'НАСТРОЕНИЕ', parameter):
          return 'Настроение'
        elif re.search(r'РИХАРД', parameter):
          return 'Рихард'
        elif re.search(r'СКАЙ ГАРДЕН', parameter):
            return 'Скай Гарден'
        return f'NaN - {parameter}'

    elif placement == 'dv360':
        if re.search(r'nastroen', parameter):
            return 'Настроение'
        elif re.search(r'rikhard|rihard', parameter):
           return 'Рихард'
        elif re.search(r'skolkovsk', parameter):
           return 'Сколковский'
        elif re.search(r'brand|fsk lider', parameter) and not re.search(r'business', parameter):
           return 'Бренд ФСК'
        elif re.search(r'business', parameter):
           return 'Бизнес ФСК'
        elif re.search(r'rezhis', parameter):
           return 'Режиссер'
        elif re.search(r'rimsk', parameter):
           return 'Римский'
        elif re.search(r'garden', parameter):
           return 'Скай Гарден'
        elif re.search(r'sydn|sidn', parameter):
            return 'Сидней Сити'
        return f'NaN - {parameter}'

    elif placement == 'criteo':
        if parameter == 'FSK Sydney-city RU':
            return 'Сидней Сити'
        elif parameter == 'FSK Skolkovskiy':
           return 'Сколковский'
        elif parameter == 'FSK Rimskiy':
           return 'Римский'
        elif parameter == 'FSK RU Rezhisser':
           return 'Режиссер'
        elif parameter == 'Fsk RU Rihard':
            return 'Рихард'
        return f'NaN - {parameter}'

    elif placement == 'upravel':
        if re.search(r'fsk // aidata // недвижимость|fsk // недвижимость|fsk // ретаргетинг',
                     parameter) and not re.search(r'коммерческая недвижимость', parameter):
            return 'Бренд ФСК'
        elif re.search(r'fsk // бизнес|fsk business', parameter):
           return 'Бизнес ФСК'
        elif re.search(r'fsk rezhiser', parameter):
           return 'Режиссер'
        elif re.search(r'коммерческая недвижимость', parameter):
           return 'Коммерческая'
        elif re.search(r'sky garden|skygarden', parameter):
           return 'Скай Гарден'
        elif re.search(r'sydney|сидней', parameter) and not re.search(r'prime|прайм', parameter):
           return 'Сидней Сити'
        elif re.search(r'sydney|сидней', parameter) and re.search(r'prime|прайм', parameter):
           return 'Сидней Прайм'
        elif parameter == 'FSK // January // 2021 // video':
            return 'Неопределяемый ЖК'
        return f'NaN - {parameter}'

    elif placement == 'custom':
        if re.search(r'бизнес|fsk-business', parameter):
            return 'Бизнес ФСК'
        elif re.search(r'garden|гарден', parameter):
           return 'Скай Гарден'
        elif re.search(r'sydney|сидней', parameter):
           return 'Сидней Сити'
        elif re.search(r'nastroenie', parameter):
           return 'Настроение'
        elif re.search(r'rezhiser', parameter):
           return 'Режиссер'
        elif re.search(r'rihard', parameter):
           return 'Рихард'
        elif re.search(r'rimskiy', parameter):
           return 'Римский'
        elif re.search(r'skolkovskiy', parameter):
            return 'Сколковский'
        return f'NaN - {parameter}'

    elif placement == 'soloway':
        if re.search(r'римский', parameter):
            return 'Римский'
        elif re.search(r'сидней', parameter):
           return 'Сидней Сити'
        elif re.search(r'режиссер', parameter):
           return 'Режиссер'
        elif re.search(r'гарден', parameter):
           return 'Скай Гарден'
        elif re.search(r'настроение', parameter):
           return 'Настроение'
        elif re.search(r'рихард', parameter):
            return 'Рихард'
        return f'NaN - {parameter}'

    elif placement == 'mobile_vkr':
        if re.search(r'outlet', parameter):
            return 'ФСК Аутлет'
        elif re.search(r'rezhis', parameter):
           return 'Режиссер'
        elif re.search(r'rimsk', parameter):
           return 'Римский'
        elif re.search(r'rihard', parameter):
           return 'Рихард'
        elif re.search(r'sydn', parameter):
           return 'Сидней Сити'
        elif re.search(r'garden', parameter):
            return 'Скай Гарден'
        return f'NaN - {parameter}'

    return 'placement-NaN'
