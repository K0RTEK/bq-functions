import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_object_leadgen(placement: str, fb_campaign_name: str, fb_adset_name: str,
                                                form_name: str, phone: str) -> str:
    placement = is_none(placement)
    fb_campaign_name = is_none(fb_campaign_name)
    fb_adset_name = is_none(fb_adset_name)
    form_name = is_none(form_name)
    phone = is_none(phone)

    def test_phone(phone):
        return re.search(r'7911111111|7999999999', phone)

    if placement == 'vk':
        if test_phone(phone):
            return 'Тест'
        elif re.search(r'воскресенский|voskresensk', form_name):
           return 'Дом на Воскресенском'
        elif re.search(r'коммерция', form_name):
           return 'Коммерческая'
        elif re.search(r'молод.жный|molodezhn', form_name):
           return 'Молодежный'
        elif re.search(r'настроение|nastroen', form_name):
           return 'Настроение'
        elif re.search(r'сабурово|saburovo', form_name):
           return 'Сабурово Клаб'
        elif re.search(r'zhavoron|жаворон', form_name):
           return 'Жаворонки Клаб'
        elif re.search(r'сидней сити|sydney city', form_name):
           return 'Сидней Сити'
        elif re.search(r'сидней прайм|sydney prime', form_name):
           return 'Сидней Прайм'
        elif re.search(r'sky.*garden', form_name):
           return 'Скай Гарден'
        elif re.search(r'олимп|olimp', form_name):
           return 'Олимп'
        elif re.search(r'дружба', form_name):
           return 'Дружба'
        elif re.search(r'поколение', form_name):
           return 'Поколение'
        elif re.search(r'режисс.р', form_name):
           return 'Режиссер'
        elif re.search(r'римский|rimsk', form_name):
           return 'Римский'
        elif re.search(r'рихард', form_name):
           return 'Рихард'
        elif re.search(r'сколковский', form_name):
           return 'Сколковский'
        elif re.search(r'бренд olv', form_name):
           return 'Бренд ФСК OLV'
        elif re.search(r'бренд аутлет', form_name):
           return 'ФСК Аутлет'
        elif re.search(r'бренд бизнес', form_name):
           return 'Бизнес ФСК'
        elif re.search(r'бренд фск|fsk 2019|бренд', form_name):
           return 'Бренд ФСК'
        elif re.search(r'datsk', form_name):
           return 'Датский'
        elif re.search(r'gagar.nsk', form_name):
           return 'Гагаринский'
        elif re.search(r'novoe.*tush', form_name):
           return 'Новое Тушино'
        elif re.search(r'skandinavsk', form_name):
           return 'Скандинавский'
        elif re.search(r'dvijen', form_name):
           return 'Движение Тушино'
        elif re.search(r'ramensk', form_name):
           return 'Новый Раменский'
        elif re.search(r'град московский', form_name):
           return 'Град Московский'
        elif re.search(r'novogireevsk', form_name):
           return 'Новогиреевский'
        elif re.search(r'апрель|aprel', form_name):
           return 'Парк Апрель'
        elif re.search(r'sheremet|шеремет', form_name):
           return '1-й Шереметьевский'
        elif re.search(r'lake', form_name):
            return 'The Lake'
        return f'NaN_{form_name}'

    elif placement == 'vkr':
        if test_phone(phone):
            return 'Тест'
        elif re.search(r'воскресенский|voskresensk', form_name):
            return 'Дом на Воскресенском'
        return get_object_leadgen('vk', fb_campaign_name, fb_adset_name, form_name, phone)

    elif placement == 'mt':
        if test_phone(phone):
            return 'Тест'
        elif re.search(r'воскресенский', form_name):
           return 'Дом на Воскресенском'
        elif re.search(r'коммерция', form_name):
           return 'Коммерческая'
        elif re.search(r'молод.жный', form_name):
           return 'Молодежный'
        elif re.search(r'настроение', form_name):
           return 'Настроение'
        elif re.search(r'сабурово|saburovo', form_name):
           return 'Сабурово Клаб'
        elif re.search(r'zhavoron|жаворон', form_name):
           return 'Жаворонки Клаб'
        elif re.search(r'сидней сити|sydney city', form_name):
           return 'Сидней Сити'
        elif re.search(r'сидней прайм|sydney prime', form_name):
           return 'Сидней Прайм'
        elif re.search(r'олимп', form_name):
           return 'Олимп'
        elif re.search(r'поколение', form_name):
           return 'Поколение'
        elif re.search(r'апрель', form_name):
           return 'Парк Апрель'
        elif re.search(r'sheremet|шеремет', form_name):
           return '1-й Шереметьевский'
        elif re.search(r'lake', form_name):
           return 'The Lake'
        elif re.search(r'режисс.р', form_name):
           return 'Режиссер'
        elif re.search(r'римский', form_name):
           return 'Римский'
        elif re.search(r'рихард', form_name):
           return 'Рихард'
        elif re.search(r'дружба', form_name):
           return 'Дружба'
        elif re.search(r'сколковский', form_name):
           return 'Сколковский'
        elif re.search(r'бренд olv', form_name):
           return 'Бренд ФСК OLV'
        elif re.search(r'бренд аутлет', form_name):
           return 'ФСК Аутлет'
        elif re.search(r'бренд бизнес', form_name):
           return 'Бизнес ФСК'
        elif re.search(r'бренд фск', form_name):
            return 'Бренд ФСК'
        return f'NaN_{form_name}'

    elif placement == 'fb':
        if re.search(r'olv-fsk|brand-olv|brand-fsk_olv', fb_campaign_name):
            return 'Бренд ФСК OLV'
        elif re.search(r'_soc_fsk-business_|soc_business-fsk', fb_campaign_name):
           return 'Бизнес ФСК'
        elif re.search(r'_soc_fsk_|brand', fb_campaign_name) and not re.search(r'olv-fsk|brand-olv|brand-fsk_olv',
                                                                                    fb_campaign_name):
           return 'Бренд ФСК'
        elif re.search(r'voskresensk', fb_campaign_name):
           return 'Дом на Воскресенском'
        elif re.search(r'commerc|com_', fb_campaign_name):
           return 'Коммерческая'
        elif re.search(r'molode|_mld_', fb_campaign_name):
           return 'Молодежный'
        elif re.search(r'nastroen|nstr', fb_campaign_name):
           return 'Настроение'
        elif re.search(r'olimp|_olp_', fb_campaign_name):
           return 'Олимп'
        elif re.search(r'pkl|pokolenie', fb_campaign_name):
           return 'Поколение'
        elif re.search(r'rezh', fb_campaign_name):
           return 'Режиссер'
        elif re.search(r'_rim', fb_campaign_name):
           return 'Римский'
        elif re.search(r'rih', fb_campaign_name):
           return 'Рихард'
        elif re.search(r'sydney|sidn', fb_campaign_name) and not re.search(r'-prime', fb_campaign_name):
           return 'Сидней Сити'
        elif re.search(r's.dn.*-prime', fb_campaign_name):
           return 'Сидней Прайм'
        elif re.search(r'skygarden', fb_campaign_name):
           return 'Скай Гарден'
        elif re.search(r'skolkovsk|_skl', fb_campaign_name):
           return 'Сколковский'
        elif re.search(r'bitsa_', fb_campaign_name):
           return 'Южная Битца'
        elif re.search(r'datsk', fb_campaign_name):
           return 'Датский'
        elif re.search(r'nekrasovka', fb_campaign_name):
           return 'Некрасовка'
        elif re.search(r'novogirievsk', fb_campaign_name):
           return 'Новогиреевский'
        elif re.search(r'dyhan', fb_campaign_name):
           return 'Дом Дыхание'
        elif re.search(r'lerm', fb_campaign_name):
           return 'Первый Лермонтовский'
        elif re.search(r'skandinav', fb_campaign_name):
           return 'Скандинавский'
        elif re.search(r'solncevo', fb_campaign_name):
           return 'Солнцево'
        elif re.search(r'centr2', fb_campaign_name):
           return 'Центр-2'
        elif re.search(r'centraln', fb_campaign_name):
           return 'Центральный'
        elif re.search(r'ramensk', fb_campaign_name):
           return 'Новый Раменский'
        elif re.search(r'moskovsk', fb_campaign_name):
           return 'Град Московский'
        elif re.search(r'tushino', fb_campaign_name):
           return 'Новое Тушино'
        elif re.search(r'andr|andereevsk', fb_campaign_name):
           return 'Первый Андреевский'
        elif re.search(r'fsk_auc', fb_campaign_name):
            if re.search(r'olv-fsk|brand-olv|brand-fsk_olv', fb_adset_name):
                return 'Бренд ФСК OLV'
            elif re.search(r'_soc_fsk-business_|soc_business-fsk', fb_adset_name):
               return 'Бизнес ФСК'
            elif re.search(r'_soc_fsk_|brand', fb_adset_name) and not re.search(
                   r'olv-fsk|brand-olv|brand-fsk_olv', fb_adset_name):
               return 'Бренд ФСК'
            elif re.search(r'voskresensk', fb_adset_name):
               return 'Дом на Воскресенском'
            elif re.search(r'commerc|com_', fb_adset_name):
               return 'Коммерческая'
            elif re.search(r'molode|_mld_', fb_adset_name):
               return 'Молодежный'
            elif re.search(r'nastroen|nstr', fb_adset_name):
               return 'Настроение'
            elif re.search(r'olimp|_olp_', fb_adset_name):
               return 'Олимп'
            elif re.search(r'pkl|pokolenie', fb_adset_name):
               return 'Поколение'
            elif re.search(r'rezh', fb_adset_name):
               return 'Режиссер'
            elif re.search(r'_rim', fb_adset_name):
               return 'Римский'
            elif re.search(r'rih', fb_adset_name):
               return 'Рихард'
            elif re.search(r'sydney|sidn', fb_adset_name) and not re.search(r'-prime', fb_adset_name):
               return 'Сидней Сити'
            elif re.search(r's.dn.*-prime', fb_adset_name):
               return 'Сидней Прайм'
            elif re.search(r'skygarden', fb_adset_name):
               return 'Скай Гарден'
            elif re.search(r'skolkovsk|_skl', fb_adset_name):
               return 'Сколковский'
            elif re.search(r'bitsa_', fb_adset_name):
               return 'Южная Битца'
            elif re.search(r'datsk', fb_adset_name):
               return 'Датский'
            elif re.search(r'nekrasovka', fb_adset_name):
               return 'Некрасовка'
            elif re.search(r'novogirievsk', fb_adset_name):
               return 'Новогиреевский'
            elif re.search(r'dyhan', fb_adset_name):
               return 'Дом Дыхание'
            elif re.search(r'lerm', fb_adset_name):
               return 'Первый Лермонтовский'
            elif re.search(r'skandinav', fb_adset_name):
               return 'Скандинавский'
            elif re.search(r'solncevo', fb_adset_name):
               return 'Солнцево'
            elif re.search(r'centr2', fb_adset_name):
               return 'Центр-2'
            elif re.search(r'centraln', fb_adset_name):
               return 'Центральный'
            elif re.search(r'ramensk', fb_adset_name):
               return 'Новый Раменский'
            elif re.search(r'moskovsk', fb_adset_name):
               return 'Град Московский'
            elif re.search(r'tushino', fb_adset_name):
               return 'Новое Тушино'
            elif re.search(r'andr|andereevsk', fb_adset_name):
                return 'Первый Андреевский'
            return 'NaN'
        return 'NaN'

    return 'NaN'
