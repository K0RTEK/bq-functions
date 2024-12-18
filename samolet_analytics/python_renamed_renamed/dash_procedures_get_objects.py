import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

import re

def get_objects(date, parameter, res_type):
    parameter = is_none(parameter)
    res_type = is_none(res_type)

    if re.search(r'mg_vka_soc_samolet_msk_lead_lead-b|mg_vka_soc_samolet_msk_lead_ret-b|mg_vka_soc_samolet_msk_traf_click-b', parameter):
        if res_type == 'object':
            return 'Кэшбэк'
        return 'Москва'

    if re.search(r'commercial.auc', parameter):
        if res_type == 'object':
            return 'Аукцион'
        return 'Москва'

    if re.search(r'l2c_', parameter):
        if res_type == 'object':
            return 'Lead2Call'
        return 'Москва'

    if re.search(r'жк0', parameter) and (re.search(r'msk|mmo', parameter) or not re.search(r'istra|spb|tmn|vldv', parameter)):
        if res_type == 'object':
            return 'ПРИГОРОД'
        return 'Москва'

    if re.search(r'behappy|формула счастья', parameter):
        if res_type == 'object':
            return 'Формула счастья'
        if res_type == 'crm_direction':
            return 'Флайт'
        return 'Москва'

    if re.search(r'alhimovo|алхимово', parameter):
        if res_type == 'object':
            return 'АЛХИМОВО'
        return 'Москва'

    if re.search(r'aviatorov|квартал авиаторов', parameter):
        if res_type == 'object':
            return 'Квартал Авиаторов'
        return 'Москва'

    if re.search(r'bogdanovsk|богдановский лес', parameter):
        if res_type == 'object':
            return 'Богдановский Лес'
        return 'Москва'

    if re.search(r'cvet poliany|tsvetochnye-poljany|цветочные поляны', parameter):
        if res_type == 'object':
            return 'Цветочные Поляны'
        return 'Москва'

    if re.search(r'dolina.yauz|долина яузы', parameter):
        if res_type == 'object':
            return 'Долина Яузы'
        return 'Москва'

    if re.search(r'domashni|квартал домашний', parameter):
        if res_type == 'object':
            return 'Квартал Домашний'
        return 'Москва'

    if re.search(r'egorovo|егорово парк', parameter):
        if res_type == 'object':
            return 'Егорово Парк'
        return 'Москва'

    if re.search(r'eko.bunino|эко бунино', parameter):
        if res_type == 'object':
            return 'Эко Бунино'
        return 'Москва'

    if re.search(r'gercena|kvartal-gertzena|квартал герцена', parameter):
        if res_type == 'object':
            return 'Квартал Герцена'
        return 'Москва'

    if re.search(r'gorki.park|горки парк', parameter):
        if res_type == 'object':
            return 'Горки Парк'
        return 'Москва'

    if re.search(r'ivakino|ивакино', parameter):
        if res_type == 'object':
            return 'ИВАКИНО'
        return 'Москва'

    if re.search(r'kvartal.maryino|квартал марьино', parameter):
        if res_type == 'object':
            return 'Квартал Марьино'
        return 'Москва'

    if re.search(r'kvartal.na.vode|квартал на воде', parameter):
        if res_type == 'object':
            return 'Квартал на воде'
        return 'Москва'

    if re.search(r'kvartal.zapadn|квартал западный', parameter):
        if res_type == 'object':
            return 'Квартал Западный'
        return 'Москва'

    if re.search(r'lubercy|люберцы', parameter):
        if res_type == 'object':
            return 'ЛЮБЕРЦЫ'
        return 'Москва'

    if re.search(r'molzhaninovo|молжаниново', parameter):
        if res_type == 'object':
            return 'МОЛЖАНИНОВО'
        return 'Москва'

    if re.search(r'mytischi|мытищи парк', parameter):
        if res_type == 'object':
            return 'Мытищи Парк'
        return 'Москва'

    if re.search(r'vnukovo|новое внуково', parameter):
        if res_type == 'object':
            return 'НОВОЕ ВНУКОВО'
        return 'Москва'

    if re.search(r'nova|nova select', parameter) and not re.search(r'novaya', parameter):
        if res_type == 'object':
            return 'Nova Select'
        return 'Москва'

    if re.search(r'novodanilovskaya|новоданиловская', parameter):
        if res_type == 'object':
            return 'НОВОДАНИЛОВСКАЯ'
        return 'Москва'

    if re.search(r'novograd.pavlino|новоград павлино', parameter):
        if res_type == 'object':
            return 'Новоград Павлино'
        return 'Москва'

    if re.search(r'o.tyabrskaya.98|октябрьская.98', parameter):
        if res_type == 'object':
            return 'Октябрьская 98'
        return 'Москва'

    if re.search(r'ostafievo|остафьево', parameter):
        if res_type == 'object':
            return 'ОСТАФЬЕВО'
        return 'Москва'

    if re.search(r'podolskie.kvartaly|подольские кварталы', parameter):
        if res_type == 'object':
            return 'Подольские Кварталы'
        return 'Москва'

    if re.search(r'pribrezhnyj.park|прибрежный парк', parameter):
        if res_type == 'object':
            return 'Прибрежный Парк'
        return 'Москва'

    if re.search(r'prigorod|пригород', parameter):
        if res_type == 'object':
            return 'ПРИГОРОД'
        return 'Москва'

    if re.search(r'putilkovo|путилково', parameter):
        if res_type == 'object':
            return 'ПУТИЛКОВО'
        return 'Москва'

    if re.search(r'pyatnitskie.luga|пятницкие луга', parameter):
        if res_type == 'object':
            return 'Пятницкие Луга'
        return 'Москва'

    if re.search(r'pyatnitskoe.58|pyatnickoe.58|пятницкое.58', parameter):
        if res_type == 'object':
            return 'Пятницкое 58'
        return 'Москва'

    if re.search(r'rublevskiy|рублевский квартал', parameter):
        if res_type == 'object':
            return 'Рублевский квартал'
        return 'Москва'

    if re.search(r'rumyancevo|rumyantsevo|квартал румянцево', parameter):
        if res_type == 'object':
            return 'Квартал Румянцево'
        return 'Москва'

    if re.search(r'sputnik|спутник', parameter) and not re.search(r'samoletum', parameter):
        if res_type == 'object':
            return 'СПУТНИК'
        return 'Москва'

    if re.search(r'stremyann...2|стремянный.2', parameter):
        if res_type == 'object':
            return 'Стремянный 2'
        return 'Москва'

    if re.search(r'strogino|квартал строгино', parameter):
        if res_type == 'object':
            return 'Квартал Строгино'
        return 'Москва'

    if re.search(r'tomilino|томилино', parameter):
        if res_type == 'object':
            return 'ТОМИЛИНО'
        return 'Москва'

    if re.search(r'troparevo|тропарево парк', parameter):
        if res_type == 'object':
            return 'Тропарево Парк'
        return 'Москва'

    if re.search(r'veresk|вереск', parameter):
        if res_type == 'object':
            return 'Вереск'
        return 'Москва'

    if re.search(r'vidnoe|новое видное', parameter):
        if res_type == 'object':
            return 'Новое Видное'
        return 'Москва'

    if re.search(r'zarechye|заречье парк', parameter):
        if res_type == 'object':
            return 'Заречье Парк'
        return 'Москва'

    if re.search(r'vere.ska.a.41|верейская', parameter):
        if res_type == 'object':
            return 'ВЕРЕЙСКАЯ'
        return 'Москва'

    if re.search(r'nekrasovka|некрасовка', parameter):
        if res_type == 'object':
            return 'Некрасовка'
        return 'Москва'

    if re.search(r'мята', parameter):
        if res_type == 'object':
            return 'Мята'
        return 'Москва'

    if re.search(r'кленовые аллеи', parameter):
        if res_type == 'object':
            return 'Кленовые Аллеи'
        return 'Москва'

    if re.search(r'vost-kotel|восточный кот.л', parameter):
        if res_type == 'object':
            return 'Восточный котел'
        return 'Москва'

    if re.search(r'olkhovyi-kvartal|ольховый', parameter):
        if res_type == 'object':
            return 'Ольховый Квартал'
        return 'Москва'

    if re.search(r'cl-nmsk_|кластер - новая москва|кластер нм|cluster novaya msk', parameter) and not re.search(r'ret-olv', parameter):
        if res_type == 'object':
            return 'Кластер - Новая Москва'
        return 'Москва'

    if re.search(r'cl-yug_|кластер - юг|южный.*кластер|cluster msk yug', parameter):
        if res_type == 'object':
            return 'Кластер - Юг'
        return 'Москва'

    if re.search(r'cl-sever_|кластер - север|север.*кластер|cluster msk sever', parameter):
        if res_type == 'object':
            return 'Кластер - Север'
        return 'Москва'

    if re.search(r'cl-zapad_|кластер.*запад|запад.*кластер|cluster msk zapad', parameter):
        if res_type == 'object':
            return 'Кластер - Запад'
        return 'Москва'

    if re.search(r'cl-vostok_|кластер.*восто|восто.*кластер|cluster msk vostok', parameter):
        if res_type == 'object':
            return 'Кластер - Восток'
        return 'Москва'

    if re.search(r'cl-bus_|кластер - бизнес-класс|cluster.*business|бизнес.класс', parameter):
        if res_type == 'object':
            return 'Кластер - Бизнес-класс'
        return 'Москва'
    
    if re.search(r'жк0', parameter) and re.search(r'spb', parameter):
        if res_type == 'object':
            return 'ЖИВИ В Рыбацком'
        return 'СПб'

    if re.search(r'жк0', parameter) and re.search(r'tmn', parameter):
        if res_type == 'object':
            return 'Чаркова, 72'
        return 'Тюмень'

    if re.search(r'жк0', parameter) and re.search(r'vldv', parameter):
        if res_type == 'object':
            return 'Сабанеева 125'
        return 'Владивосток'
    
    return '-'


