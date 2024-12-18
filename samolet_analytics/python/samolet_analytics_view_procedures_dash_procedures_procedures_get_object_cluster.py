import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_object_cluster(date, parameter, res_type):
    if is_none(dash_procedures.get_objects(date, parameter, 'crm_direction')) == 'москва':
        object_name = is_none(dash_procedures.get_objects(date, parameter, 'object'))
        if object_name == 'пригород':
            return 'Кластер - Юг'
        elif object_name == 'алхимово':
            return 'Кластер - Новая Москва'
        elif object_name == 'квартал авиаторов':
            return 'Кластер - Восток'
        elif object_name == 'богдановский лес':
            return 'Кластер - Юг'
        elif object_name == 'цветочные поляны':
            return 'Кластер - Новая Москва'
        elif object_name == 'долина яузы':
            return 'Кластер - Восток'
        elif object_name == 'квартал домашний':
            return 'Кластер - Юг'
        elif object_name == 'егорово парк':
            return 'Кластер - Восток'
        elif object_name == 'эко бунино':
            return 'Кластер - Новая Москва'
        elif object_name == 'квартал герцена':
            return 'Кластер - Юг'
        elif object_name == 'горки парк':
            return 'Кластер - Юг'
        elif object_name == 'ивакино':
            return 'Кластер - Север'
        elif object_name == 'квартал марьино':
            return 'Кластер - Новая Москва'
        elif object_name == 'квартал на воде':
            return 'Кластер - Бизнес-класс'
        elif object_name == 'квартал западный':
            return 'Кластер - Новая Москва'
        elif object_name == 'люберцы':
            return 'Кластер - Восток'
        elif object_name == 'молжаниново':
            return 'Кластер - Север'
        elif object_name == 'мытищи парк':
            return 'Кластер - Восток'
        elif object_name == 'новое внуково':
            return 'Кластер - Новая Москва'
        elif object_name == 'nova select':
            return '-'
        elif object_name == 'новоданиловская':
            return 'Кластер - Бизнес-класс'
        elif object_name == 'новоград павлино':
            return 'Кластер - Восток'
        elif object_name == 'ольховый квартал':
            return 'Кластер - Новая Москва'
        elif object_name == 'октябрьская 98':
            return 'Кластер - Бизнес-класс'
        elif object_name == 'остафьево':
            return 'Кластер - Новая Москва'
        elif object_name == 'подольские кварталы':
            return 'Кластер - Новая Москва'
        elif object_name == 'прибрежный парк':
            return 'Кластер - Юг'
        elif object_name == 'пригород':
            return 'Кластер - Юг'
        elif object_name == 'путилково':
            return 'Кластер - Север'
        elif object_name == 'пятницкие луга':
            return 'Кластер - Север'
        elif object_name == 'пятницкое 58':
            return 'Кластер - Север'
        elif object_name == 'рублевский квартал':
            return 'Кластер - Запад'
        elif object_name == 'квартал румянцево':
            return 'Кластер - Новая Москва'
        elif object_name == 'сputnik':
            return 'Кластер - Запад'
        elif object_name == 'стремянный 2':
            return 'Кластер - Бизнес-класс'
        elif object_name == 'квартал строгино':
            return 'Кластер - Запад'
        elif object_name == 'томилино':
            return 'Кластер - Восток'
        elif object_name == 'тропарево парк':
            return 'Кластер - Бизнес-класс'
        elif object_name == 'вереск':
            return 'Кластер - Бизнес-класс'
        elif object_name == 'новое видное':
            return 'Кластер - Юг'
        elif object_name == 'заречье парк':
            return 'Кластер - Бизнес-класс'
        elif object_name == 'верейская':
            return 'Кластер - Бизнес-класс'
        elif object_name == 'некрасовка':
            return 'Кластер - Бизнес-класс'
        elif object_name == 'мята':
            return 'Кластер - Бизнес-класс'
        elif object_name == 'кленовые аллеи':
            return 'Кластер - Новая Москва'
        elif object_name == 'восточный котел':
            return 'Кластер - Восток'
        elif object_name == 'квартал ольховый':
            return 'Кластер - Новая Москва'
        elif object_name == 'кластер - новая москва':
            return 'Кластер - Новая Москва'
        elif object_name == 'кластер - юг':
            return 'Кластер - Юг'
        elif object_name == 'кластер - север':
            return 'Кластер - Север'
        elif object_name == 'кластер - запад':
            return 'Кластер - Запад'
        elif object_name == 'кластер - восток':
            return 'Кластер - Восток'
        elif object_name == 'кластер - бизнес-класс':
            return 'Кластер - Бизнес-класс'
        else:
            return '-'
    else:
        return '-'