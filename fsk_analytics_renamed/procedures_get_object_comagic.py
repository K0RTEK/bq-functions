import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_object_comagic(campaign_name: str) -> str:
    campaign_name = is_none(campaign_name)

    if re.search(r'lake', campaign_name):
        return 'The Lake'
    elif re.search(r'сидней|sidney|sydney', campaign_name) and not re.search(r'prime|прайм', campaign_name):
       return 'Сидней Сити'
    elif re.search(r'сидней|sidney|sydney', campaign_name) and re.search(r'prime|прайм', campaign_name):
       return 'Сидней Прайм'
    elif re.search(r'вторич', campaign_name):
       return 'Вторичка'
    elif re.search(r'leningrad|ленинград', campaign_name):
       return 'Первый Ленинградский'
    elif re.search(r'говорово|govorovo', campaign_name):
       return 'Движение Говорово'
    elif re.search(r'гагаринский', campaign_name):
       return 'Гагаринский'
    elif re.search(r'дружба', campaign_name):
       return 'Дружба'
    elif re.search(r'роттердам|rotterdam', campaign_name):
       return 'Роттердам'
    elif re.search(r'движение|dvizhen', campaign_name) and not re.search(r'говорово|govorovo', campaign_name):
       return 'Движение'
    elif re.search(r'бтл-дв|btl', campaign_name):
       return 'Движение BTL'
    elif re.search(r'домодедово', campaign_name):
       return 'Домодедово Парк'
    elif re.search(r'на набережной', campaign_name):
       return 'На Набережной'
    elif re.search(r'флагман', campaign_name):
       return 'Флагман'
    elif re.search(r'западное кунцево', campaign_name):
       return 'Западное Кунцево'
    elif re.search(r'чижевского', campaign_name):
       return 'Чижевского'
    elif re.search(r'лисицына', campaign_name):
       return 'Лисицына'
    elif re.search(r'лухмановский', campaign_name):
       return 'ТЦ Лухмановский'
    elif re.search(r'лагерь салют', campaign_name):
       return 'Лагерь Салют'
    elif re.search(r'планерная', campaign_name):
       return 'БО Планерная'
    elif re.search(r'магистральная', campaign_name):
       return 'Магистральная'
    elif re.search(r'адмирал', campaign_name):
       return 'Адмирал'
    elif re.search(r'столичный квартал', campaign_name):
       return 'Столичный квартал'
    elif re.search(r'созидатель', campaign_name):
       return 'ДК Созидатель'
    elif re.search(r'москворецкий', campaign_name):
       return 'Москворецкий'
    elif re.search(r'юбилейный', campaign_name):
       return 'Первый Юбилейный'
    elif re.search(r'garden|гарден', campaign_name):
       return 'Скай Гарден'
    elif re.search(r'архитектор', campaign_name):
       return 'Архитектор'
    elif re.search(r'дом на воскресенском', campaign_name):
       return 'Дом на Воскресенском'
    elif re.search(r'коммерческая|коммерция|псн аренда|мясницкая', campaign_name):
       return 'Коммерческая'
    elif re.search(r'кладов', campaign_name):
       return 'Кладовые'
    elif re.search(r'машиноместа', campaign_name):
       return 'Машиноместа'
    elif re.search(r'молод.жный', campaign_name):
       return 'Молодежный'
    elif re.search(r'настроение|nastroen', campaign_name):
       return 'Настроение'
    elif re.search(r'олимп', campaign_name):
       return 'Олимп'
    elif re.search(r'парк апрель|aprel', campaign_name):
       return 'Парк Апрель'
    elif re.search(r'шереметьевский', campaign_name):
       return '1-й Шереметьевский'
    elif re.search(r'донской', campaign_name):
       return '1-й Донской'
    elif re.search(r'uzhniy|южный', campaign_name):
       return '1-й Южный'
    elif re.search(r'режисс.р', campaign_name):
       return 'Режиссер'
    elif re.search(r'римски|rimsk', campaign_name):
       return 'Римский'
    elif re.search(r'рихард|rihard', campaign_name):
       return 'Рихард'
    elif re.search(r'сабурово', campaign_name):
       return 'Сабурово Клаб'
    elif re.search(r'жаворонки|zhavoronk', campaign_name):
       return 'Жаворонки Клаб'
    elif re.search(r'сколковский', campaign_name):
       return 'Сколковский'
    elif re.search(r'поколение', campaign_name):
       return 'Поколение'
    elif re.search(r'некрасовка', campaign_name):
       return 'Некрасовка'
    elif re.search(r'новогиреев.кий', campaign_name):
       return 'Новогиреевский'
    elif re.search(r'лермонтовский', campaign_name):
       return 'Первый Лермонтовский'
    elif re.search(r'центр.2', campaign_name):
       return 'Центр-2'
    elif re.search(r'центр', campaign_name) and not re.search(r'центральн|центр.2', campaign_name):
       return 'Центр'
    elif re.search(r'тушино', campaign_name):
       return 'Новое Тушино'
    elif re.search(r'скандинавский|skandinav', campaign_name):
       return 'Скандинавский'
    elif re.search(r'московский', campaign_name):
       return 'Град Московский'
    elif re.search(r'датский', campaign_name):
       return 'Датский'
    elif re.search(r'дыхание', campaign_name):
       return 'Дом Дыхание'
    elif re.search(r'некрасовка', campaign_name):
       return 'Некрасовка'
    elif re.search(r'новое измайлово', campaign_name):
       return 'Новое Измайлово'
    elif re.search(r'раменский', campaign_name):
       return 'Новый Раменский'
    elif re.search(r'андреевский', campaign_name):
       return 'Первый Андреевский'
    elif re.search(r'солнцево', campaign_name):
       return 'Солнцево'
    elif re.search(r'спецпроект|avito.*лендинг фск', campaign_name):
       return 'Спецпроект'
    elif re.search(r'центральный', campaign_name):
       return 'Центральный'
    elif re.search(r'битца|битце', campaign_name):
       return 'Южная Битца'
    elif re.search(r'дск', campaign_name):
       return 'Бренд ДСК'
    elif re.search(r'realist|реалист', campaign_name):
       return 'Реалист'
    elif re.search(r'бизнес', campaign_name) and not re.search(r'аутлет|outlet', campaign_name):
       return 'Бизнес ФСК'
    elif re.search(r'olv.*бренд|бренд.*olv| olv', campaign_name):
       return 'Бренд ФСК OLV'
    elif re.search(r'бренд фск|аутлет|outlet|фск лидер', campaign_name):
       return 'Бренд ФСК'
    elif campaign_name in [
        'MG | Контекст Бренд | Яндекс Директ |',
        'MG | Контекст Сеть | Яндекс Директ |',
        'MG | Соц сети | Прозвон Lead2Call',
        'MG_Instagram'
    ]:
        return 'Невозможно определить Объект'

    return 'NaN'
