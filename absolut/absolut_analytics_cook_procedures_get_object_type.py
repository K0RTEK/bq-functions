def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_object_type(object_name):
    object_name = is_none(object_name)
    if object_name in ['Первый Московский', 'Переделкино Ближнее', 'Сколково']:
        return 'Жилая недвижимость'
    elif object_name in ['Порт Плаза', 'Омега Плаза', 'Омега 2']:
        return 'Коммерческая недвижимость'
    return 'Неизвестный'
