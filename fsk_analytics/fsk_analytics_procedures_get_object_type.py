def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_object_type(event_object: str) -> str:
    event_object = is_none(event_object)
    mgcom_objects = [
        'Коммерческая',
        'Дом на Воскресенском',
        'Дружба',
        'Молодежный',
        'Настроение',
        'Олимп',
        'Поколение',
        'Парк Апрель',
        'Режиссер',
        'Римский',
        'Рихард',
        'Сидней Сити',
        'Сидней Прайм',
        'Скай Гарден',
        'Сколковский',
        'Бренд ФСК',
        'Бренд ФСК OLV',
        'Бизнес ФСК',
        'ФСК Аутлет',
        'Реалист',
        'ФСК',
        'The Lake',
        'Сабурово Клаб'
    ]

    if event_object in mgcom_objects:
        return 'MGCom'
    elif 'NaN' in event_object:
        return 'NaN'
    else:
        return 'Other'
