def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_placement_price(placement_smartis: str) -> str:
    placement_smartis = is_none(placement_smartis)
    if 'avito' in placement_smartis:
        return 'Авито'
    elif 'jcat' in placement_smartis:
        return 'JCAT'
    elif 'cian' in placement_smartis:
        return 'Циан'
    elif 'svetvokne' in placement_smartis:
        return 'Svetvokne'
    elif 'm2' in placement_smartis or 'м2' in placement_smartis:
        return 'М2'
    elif 'realty' in placement_smartis:
        return 'Realty'
    elif 'общее' in placement_smartis:
        return 'Базы недвижимости // Общее'
    elif 'яндекс' in placement_smartis:
        return 'Яндекс.Недвижимость'
    elif 'domclick' in placement_smartis or 'домклик' in placement_smartis:
        return 'Домклик'
    elif 'novostroy-m' in placement_smartis:
        return 'Новострой-М'
    elif 'avaho' in placement_smartis or 'авахо' in placement_smartis:
        return 'Авахо'
    elif 'move' in placement_smartis:
        return 'Move.ru'
    elif 'мирквартир' in placement_smartis:
        return 'МирКвартир'
    else:
        return f'NaN - {placement_smartis}'
