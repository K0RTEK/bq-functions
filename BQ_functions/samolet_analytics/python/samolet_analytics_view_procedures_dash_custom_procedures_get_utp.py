import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_segment(ad_name):
    ad_name = is_none(ad_name)
    if re.search(r'ipt', ad_name):
        return 'Ипотека'
    elif re.search(r'_rassr', ad_name):
        return 'Рассрочка'
    elif re.search(r'_sale', ad_name):
        return 'Скидка'
    elif re.search(r'_mozh', ad_name):
        return 'Можнотека'
    elif re.search(r'minprice', ad_name):
        return 'Минимальная цена'
    elif re.search(r'minpay', ad_name):
        return 'Минимальный платеж'
    elif re.search(r'_invst', ad_name):
        return 'Инвестиции'
    elif re.search(r'_fransh', ad_name):
        return 'Франшиза'
    elif re.search(r'_metr', ad_name):
        return 'Метр от Самолет'
    elif re.search(r'_trade', ad_name):
        return 'trade-in'
    elif re.search(r'_vgd', ad_name):
        return 'Выгода до Х'
    elif re.search(r'_none', ad_name):
        return 'Ничего'
    elif re.search(r'_new', ad_name):
        return 'Новые квартиры / апарты'
    elif re.search(r'_bron', ad_name):
        return 'Старт бронирования'
    elif re.search(r'_st\.sale', ad_name):
        return 'Старт продаж'
    elif re.search(r'_newkorp', ad_name):
        return 'Новый корпус'
    elif re.search(r'_start', ad_name):
        return 'Cтарт продаж'
    elif re.search(r'_sdacha', ad_name):
        return 'Сдача дома'
    elif re.search(r'_samokot', ad_name):
        return 'Самокот'
    elif re.search(r'_flamingo', ad_name):
        return 'Фламинго СММ'
    elif re.search(r'_zas', ad_name):
        return 'Заселение'
    elif re.search(r'_key', ad_name):
        return 'Выдача ключей'
    elif re.search(r'mbl', ad_name):
        return 'Квартиры с мебелью'
    elif re.search(r'kuxn', ad_name):
        return 'Кватиры с кухней'
    elif re.search(r'otdel', ad_name):
        return 'Отделка'
    elif re.search(r'park', ad_name):
        return 'Парк'
    elif re.search(r'metro', ad_name):
        return 'Метро'
    elif re.search(r'dt\.sad', ad_name):
        return 'Детский сад'
    elif re.search(r'mck', ad_name):
        return 'МЦК'
    elif re.search(r'mcd', ad_name):
        return 'МЦД'
    elif re.search(r'otdel-minprice', ad_name):
        return 'Отделка + мин цена'
    elif re.search(r'mbl-minprice', ad_name):
        return 'Мебель + мин цена'
    elif re.search(r'mbl-minpay', ad_name):
        return 'Мебель + мин платеж'
    elif re.search(r'otdel-minpay', ad_name):
        return 'Отделка + мин платеж'
    elif re.search(r'centr-minprice', ad_name):
        return 'Центр + мин цена'
    elif re.search(r'centr-minpay', ad_name):
        return 'Центра + мин платеж'
    elif re.search(r'metro-minprice', ad_name):
        return 'Метро + мин цена'
    elif re.search(r'metro-minpay', ad_name):
        return 'Метро + мин платеж'
    elif re.search(r'mck-minprice', ad_name):
        return 'МЦК + мин цена'
    elif re.search(r'mck-minpay', ad_name):
        return 'МЦК + мин платеж'
    elif re.search(r'_curriculum', ad_name):
        return 'Кружки и секции'
    elif re.search(r'_personal-plan', ad_name):
        return 'Песональный учебный план'
    elif re.search(r'_20students', ad_name):
        return 'Не более 20 учеников'
    elif re.search(r'_bez-pvz', ad_name):
        return 'Без взноса пвз'
    elif re.search(r'_dobavim', ad_name):
        return 'Добавим до Х%'
    elif re.search(r'_nakop', ad_name):
        return 'Накопить на квартиру'
    elif re.search(r'_dod', ad_name):
        return 'День открытых дверей'
    elif re.search(r'_1-11-klass', ad_name):
        return '1-11 классы'
    elif re.search(r'_invitation', ad_name):
        return 'Приглашаем на ДОД'
    elif re.search(r'_school-present', ad_name):
        return 'Презентация школы'
    elif re.search(r'_14feb', ad_name):
        return '14 февраля'
    elif re.search(r'_free-reс', ad_name):
        return 'бесплатные рекомендации'
    elif re.search(r'_10rec', ad_name):
        return '10 рекомендаций'
    elif re.search(r'_sravny', ad_name):
        return 'Сравнить с похожими людьми'
    elif re.search(r'_happy', ad_name):
        return 'Исследование счастья'
    elif re.search(r'_flash', ad_name):
        return 'Flash-sale'
    elif re.search(r'apart\.ot-14\.5', ad_name):
        return 'Минимальная цена'
    elif re.search(r'apart\.bk|apart\.pyatn\.sh', ad_name):
        return 'Апартаменты'
    elif re.search(r'obsh-3\.9|obsh0', ad_name):
        return 'Общий посыл'
    elif re.search(r'private-ter', ad_name):
        return 'Приватная территория'
    elif re.search(r'reka', ad_name):
        return 'Река'
    elif re.search(r'terrace', ad_name):
        return 'Терасса'
    else:
        return ''