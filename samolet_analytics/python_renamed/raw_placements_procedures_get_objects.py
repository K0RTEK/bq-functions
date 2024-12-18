import re


def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()


def get_objects(parameter, res_type):
    parameter = is_none(parameter)
    res_type = is_none(res_type)
    if re.search(r'жк0', parameter) and re.search(r'msk|mmo', parameter):
        if res_type == 'object':
            return 'ПРИГОРОД'
        elif res_type == 'crm_direction':
            return 'Москва'
        else:
            return 'Москва'

    elif re.search(r'cl-nmsk_|кластер - новая москва', parameter):
        if res_type == 'object':
            return 'Кластер - Новая Москва'
        elif res_type == 'crm_direction':
            return 'Москва'
        else:
            return 'Москва'

    elif re.search(r'cl-yug_|кластер - юг', parameter):
        if res_type == 'object':
            return 'Кластер - Юг'
        elif res_type == 'crm_direction':
            return 'Москва'
        else:
            return 'Москва'

    elif re.search(r'cl-sever_|кластер - север', parameter):
        if res_type == 'object':
            return 'Кластер - Север'
        elif res_type == 'crm_direction':
            return 'Москва'
        else:
            return 'Москва'

    elif re.search(r'cl-zapad_|кластер - запад', parameter):
        if res_type == 'object':
            return 'Кластер - Запад'
        elif res_type == 'crm_direction':
            return 'Москва'
        else:
            return 'Москва'

    elif re.search(r'cl-vostok_|кластер - восток', parameter):
        if res_type == 'object':
            return 'Кластер - Восток'
        elif res_type == 'crm_direction':
            return 'Москва'
        else:
            return 'Москва'

    elif re.search(r'cl-bus_|кластер - бизнес-класс', parameter):
        if res_type == 'object':
            return 'Кластер - Бизнес-класс'
        elif res_type == 'crm_direction':
            return 'Москва'
        else:
            return 'Москва'

    elif re.search(r'behappy|формула счастья', parameter):
        if res_type == 'object':
            return 'Формула счастья'
        elif res_type == 'crm_direction':
            return 'Флайт'
        else:
            return 'Москва'

    elif re.search(r'alhimovo|алхимово', parameter):
        if res_type == 'object':
            return 'АЛХИМОВО'
        return 'Москва'

    elif re.search(r'aviatorov|квартал авиаторов', parameter):
        if res_type == 'object':
            return 'Квартал Авиаторов'
        return 'Москва'

    elif re.search(r'bogdanovsk|богдановский лес', parameter):
        if res_type == 'object':
            return 'Богдановский Лес'
        return 'Москва'

    elif re.search(r'cvet poliany|tsvetochnye-poljany|цветочные поляны', parameter):
        if res_type == 'object':
            return 'Цветочные Поляны'
        return 'Москва'

    elif re.search(r'dolina.yauz|долина яузы', parameter):
        if res_type == 'object':
            return 'Долина Яузы'
        return 'Москва'

    elif re.search(r'domashni|квартал домашний', parameter):
        if res_type == 'object':
            return 'Квартал Домашний'
        return 'Москва'

    elif re.search(r'egorovo|егорово парк', parameter):
        if res_type == 'object':
            return 'Егорово Парк'
        return 'Москва'

    elif re.search(r'eko.bunino|эко бунино', parameter):
        if res_type == 'object':
            return 'Эко Бунино'
        return 'Москва'

    elif re.search(r'gercena|kvartal-gertzena|квартал герцена', parameter):
        if res_type == 'object':
            return 'Квартал Герцена'
        return 'Москва'

    elif re.search(r'gorki.park|горки парк', parameter):
        if res_type == 'object':
            return 'Горки Парк'
        return 'Москва'

    elif re.search(r'ivakino|ивакино', parameter):
        if res_type == 'object':
            return 'ИВАКИНО'
        return 'Москва'

    elif re.search(r'kvartal.maryino|квартал марьино', parameter):
        if res_type == 'object':
            return 'Квартал Марьино'
        return 'Москва'

    elif re.search(r'kvartal.na.vode|квартал на воде', parameter):
        if res_type == 'object':
            return 'Квартал на воде'
        return 'Москва'

    elif re.search(r'kvartal.zapadn|квартал западный', parameter):
        if res_type == 'object':
            return 'Квартал Западный'
        return 'Москва'

    elif re.search(r'lubercy|люберцы', parameter):
        if res_type == 'object':
            return 'ЛЮБЕРЦЫ'
        return 'Москва'

    elif re.search(r'molzhaninovo|молжаниново', parameter):
        if res_type == 'object':
            return 'МОЛЖАНИНОВО'
        return 'Москва'

    elif re.search(r'mytischi|мытищи парк', parameter):
        if res_type == 'object':
            return 'Мытищи Парк'
        return 'Москва'

    elif re.search(r'vnukovo|новое внуково', parameter):
        if res_type == 'object':
            return 'НОВОЕ ВНУКОВО'
        return 'Москва'

    elif re.search(r'nova|nova select', parameter) and not re.search(r'novaya', parameter):
        if res_type == 'object':
            return 'Nova Select'
        return 'Москва'

    elif re.search(r'novodanilovskaya|новоданиловская', parameter):
        if res_type == 'object':
            return 'НОВОДАНИЛОВСКАЯ'
        return 'Москва'

    elif re.search(r'novograd.pavlino|новоград павлино', parameter):
        if res_type == 'object':
            return 'Новоград Павлино'
        return 'Москва'

    elif re.search(r'oktyabrskaya.98|октябрьская.98', parameter):
        if res_type == 'object':
            return 'Октябрьская 98'
        return 'Москва'

    elif re.search(r'ostafievo|остафьево', parameter):
        if res_type == 'object':
            return 'ОСТАФЬЕВО'
        return 'Москва'

    elif re.search(r'podolskie.kvartaly|подольские кварталы', parameter):
        if res_type == 'object':
            return 'Подольские Кварталы'
        return 'Москва'

    elif re.search(r'pribrezhnyj.park|прибрежный парк', parameter):
        if res_type == 'object':
            return 'Прибрежный Парк'
        return 'Москва'

    elif re.search(r'prigorod|пригород', parameter):
        if res_type == 'object':
            return 'ПРИГОРОД'
        return 'Москва'

    elif re.search(r'putilkovo|путилково', parameter):
        if res_type == 'object':
            return 'ПУТИЛКОВО'
        return 'Москва'

    elif re.search(r'pyatnitskie.luga|пятницкие луга', parameter):
        if res_type == 'object':
            return 'Пятницкие Луга'
        return 'Москва'

    elif re.search(r'pyatnitskoe.58|pyatnickoe.58|пятницкое.58', parameter):
        if res_type == 'object':
            return 'Пятницкое 58'
        return 'Москва'

    elif re.search(r'rublevskiy|рублевский квартал', parameter):
        if res_type == 'object':
            return 'Рублевский квартал'
        return 'Москва'

    elif re.search(r'rumyancevo|rumyantsevo|квартал румянцево', parameter):
        if res_type == 'object':
            return 'Квартал Румянцево'
        return 'Москва'

    elif re.search(r'sputnik|спутник', parameter) and not re.search(r'samoletum', parameter):
        if res_type == 'object':
            return 'СПУТНИК'
        return 'Москва'

    elif re.search(r'stremyann...2|стремянный.2', parameter):
        if res_type == 'object':
            return 'Стремянный 2'
        return 'Москва'

    elif re.search(r'strogino|квартал строгино', parameter):
        if res_type == 'object':
            return 'Квартал Строгино'
        return 'Москва'

    elif re.search(r'tomilino|томилино', parameter):
        if res_type == 'object':
            return 'ТОМИЛИНО'
        return 'Москва'

    elif re.search(r'troparevo|тропарево парк', parameter):
        if res_type == 'object':
            return 'Тропарево Парк'
        return 'Москва'

    elif re.search(r'veresk|вереск', parameter):
        if res_type == 'object':
            return 'Вереск'
        return 'Москва'

    elif re.search(r'vidnoe|новое видное', parameter):
        if res_type == 'object':
            return 'Новое Видное'
        return 'Москва'

    elif re.search(r'zarechye|заречье парк', parameter):
        if res_type == 'object':
            return 'Заречье Парк'
        return 'Москва'

    elif re.search(r'vere.ska.a.41|верейская', parameter):
        if res_type == 'object':
            return 'ВЕРЕЙСКАЯ'
        return 'Москва'

    elif re.search(r'nekrasovka|некрасовка', parameter):
        if res_type == 'object':
            return 'Некрасовка'
        return 'Москва'

    elif re.search(r'мята', parameter):
        if res_type == 'object':
            return 'Мята'
        return 'Москва'

    elif re.search(r'кленовые аллеи', parameter):
        if res_type == 'object':
            return 'Кленовые Аллеи'
        return 'Москва'

    elif re.search(r'жк0', parameter) and re.search(r'spb', parameter):
        if res_type == 'object':
            return 'ЖИВИ В Рыбацком'
        return 'Спб'

    elif re.search(r'жк0', parameter) and re.search(r'tmn', parameter):
        if res_type == 'object':
            return 'Чаркова, 72'
        return 'Тюмень'

    elif re.search(r'жк0', parameter) and re.search(r'vldv', parameter):
        if res_type == 'object':
            return 'Сабанеева 125'
        return 'Владивосток'

    elif re.search(r'astrid|астрид', parameter):
        if res_type == 'object':
            return 'АСТРИД (Колпино)'
        return 'Спб'

    elif re.search(r'spb brand|ipt.spb|mbl.sbp|spb.samolet|samolet.spb.*dinrem|спб общий', parameter):
        if res_type == 'object':
            return 'СПБ общий'
        return 'Спб'

    elif re.search(r'kolpino|красный кирпичник|новое колпино', parameter):
        if res_type == 'object':
            return 'Красный Кирпичник (Новое Колпино)'
        return 'Спб'

    elif re.search(r'kurort.kvartal|kurortkvartal|курортный квартал|песочный', parameter):
        if res_type == 'object':
            return 'Курортный Квартал (Песочный)'
        return 'Спб'

    elif re.search(r'lagolovo|лаголово', parameter):
        if res_type == 'object':
            return 'Квартал Лаголово'
        return 'Спб'

    elif re.search(r'lavriki|лаврики', parameter):
        if res_type == 'object':
            return 'Новые Лаврики'
        return 'Спб'

    elif re.search(r'nevskaya.dolina|невская долина', parameter):
        if res_type == 'object':
            return 'Невская Долина'
        return 'Спб'

    elif re.search(r'rybacko|живи(.|..)в рыбацком', parameter):
        if res_type == 'object':
            return 'ЖИВИ В Рыбацком'
        return 'Спб'

    elif re.search(r'sunday|санд.й|сосновая поляна', parameter):
        if res_type == 'object':
            return 'САНДЕЙ'
        return 'Спб'

    elif re.search(r'toriki|квартал торики', parameter):
        if res_type == 'object':
            return 'Квартал Торики'
        return 'Спб'

    elif re.search(r'yuzhnaya.neva|южная нева', parameter):
        if res_type == 'object':
            return 'Южная Нева'
        return 'Спб'

    elif re.search(r'charkova|чаркова.*72', parameter):
        if res_type == 'object':
            return 'Чаркова, 72'
        return 'Тюмень'

    elif re.search(r'sabaneeva|сабанеева.*125', parameter):
        if res_type == 'object':
            return 'Сабанеева 125'
        return 'Владивосток'

    elif re.search(r'малая охта', parameter):
        if res_type == 'object':
            return 'МАЛАЯ ОХТА'
        return 'Спб'

    elif re.search(r'ne(i|j)but|нейбута', parameter):
        if res_type == 'object':
            return 'Квартал Нейбута'
        return 'Владивосток'

    elif re.search(r'celeport|clprt_samolet|clprt|целепорт', parameter):
        if res_type == 'object':
            return 'Целепорт'
        return 'Целепорт'

    elif re.search(r'samolet.rto|rto.samolet|_rto_|и живи-ка', parameter):
        if res_type == 'object':
            return 'И живи-ка'
        return 'И живи-ка'

    elif re.search(r'istra|истра дом', parameter):
        if res_type == 'object':
            return 'Истра Дом'
        return 'ИЖС'

    elif re.search(r'dmitrov.dom|дмитров', parameter):
        if res_type == 'object':
            return 'Дмитров Дом'
        return 'ИЖС'

    elif re.search(r'life.samolet|life', parameter) and not re.search(r'samoletum', parameter):
        if res_type == 'object':
            return 'LIFE'
        return 'Флайт'

    elif re.search(r'samolet.smm|смм', parameter):
        if res_type == 'object':
            return 'СММ'
        return 'СММ'

    elif re.search(r'samoletum-school-sputnik|школа', parameter):
        if res_type == 'object':
            return 'Школа'
        return 'Самолетум'

    elif re.search(r'samoletum-school-curriculum|доп. образование', parameter):
        if res_type == 'object':
            return 'Доп. образование'
        return 'Самолетум'

    elif re.search(r'samoletum-school-dod|дод', parameter):
        if res_type == 'object':
            return 'ДОД'
        return 'Самолетум'

    elif re.search(r'samoletum|samoletum|самолетум', parameter):
        if res_type == 'object':
            return 'Самолетум'
        return 'Самолетум'

    # Общебренд
    elif re.search(r'senler', parameter):
        if res_type == 'object':
            return 'Senler'
        return 'Москва'

    elif re.search(r'_flash|flash sale|flashsale', parameter):
        if res_type == 'object':
            return 'Flash sale - общебренд'
        return 'Москва'

    elif re.search(r'mbl_msk|_mbl_|квартиры с мебелью', parameter):
        if res_type == 'object':
            return 'Квартиры с мебелью'
        return 'Москва'

    elif re.search(r'ipt_msk|ipt-|ипотека', parameter):
        if res_type == 'object':
            return 'Ипотека'
        return 'Москва'

    elif re.search(r'lead-vk-engineer|lead-ovik-engineer|main-engineer|hr вакансии', parameter):
        if res_type == 'object':
            return 'HR вакансии'
        return 'Вакансии'

    elif re.search(
            r'samolet.*_ret|rem_samolet_ret|lead-p_minpay.vid_samolet_ct_ndv_lead_mmo_23_55_2|общебренд ретаргетинг|общий ремаркетинг',
            parameter):
        if res_type == 'object':
            return 'Общебренд ретаргетинг'
        return 'Москва'

    elif re.search(
            r'samolet.*d.nre|samolet.lal|mg_vka_soc_samolet_msk_traf|mg_samolet_msk_lead_lead-30d-1875-mmo_banner_02-24|mg_samolet_msk_lead_sub-1875-mmo_banner_02-24|mg_samolet_msk_lead_sub-2565-mmo_banner_02-24|общебренд динрем|samolet_msk_traf_dinrem',
            parameter):
        if res_type == 'object':
            return 'Общебренд динрем'
        return 'Москва'

    elif re.search(r'_installment|рассрочка', parameter):
        if res_type == 'object':
            return 'Рассрочка'
        return 'Москва'

    elif re.search(r'petsflats', parameter):
        if res_type == 'object':
            return 'Petsflats'
        return 'Москва'

    elif re.search(r'_detmetr|детский метр', parameter):
        if res_type == 'object':
            return 'Детский метр'
        return 'Москва'

    elif re.search(r'brand.msk|samolet_msk|ipt_msk|mbl_msk|zhk_samolet_ct_vk|samoletgroup', parameter):
        if res_type == 'object':
            return 'SAMOLETGROUP'
        return 'Москва'

    return '-'
