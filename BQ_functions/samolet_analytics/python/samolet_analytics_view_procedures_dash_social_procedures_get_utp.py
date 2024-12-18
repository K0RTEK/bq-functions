import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_segment(date, ad_name):
    ad_name = is_none(ad_name)

    segments = {
        r'ipt': 'Ипотека',
        r'_rassr': 'Рассрочка',
        r'_sale': 'Скидка',
        r'_mozh': 'Можнотека',
        r'minprice': 'Минимальная цена',
        r'minpay': 'Минимальный платеж',
        r'_invst': 'Инвестиции',
        r'_fransh': 'Франшиза',
        r'_metr': 'Метр от Самолет',
        r'_trade': 'trade-in',
        r'_vgd': 'Выгода до Х',
        r'_none': 'Ничего',
        r'_new': 'Новые квартиры / апарты',
        r'_bron': 'Старт бронирования',
        r'_st.sale': 'Старт продаж',
        r'_newkorp': 'Новый корпус',
        r'_start': 'Cтарт продаж',
        r'_sdacha': 'Сдача дома',
        r'_samokot': 'Самокот',
        r'_flamingo': 'Фламинго СММ',
        r'_zas': 'Заселение',
        r'_key': 'Выдача ключей',
        r'mbl': 'Квартиры с мебелью',
        r'kuxn': 'Кватиры с кухней',
        r'otdel': 'Отделка',
        r'park': 'Парк',
        r'metro': 'Метро',
        r'dt.sad': 'Детский сад',
        r'mck': 'МЦК',
        r'mcd': 'МЦД',
        r'otdel-minprice': 'Отделка + мин цена',
        r'mbl-minprice': 'Мебель + мин цена',
        r'mbl-minpay': 'Мебель + мин платеж',
        r'otdel-minpay': 'Отделка + мин платеж',
        r'centr-minprice': 'Центр + мин цена',
        r'centr-minpay': 'Центра + мин платеж',
        r'metro-minprice': 'Метро + мин цена',
        r'metro-minpay': 'Метро + мин платеж',
        r'mck-minprice': 'МЦК + мин цена',
        r'mck-minpay': 'МЦК + мин платеж',
        r'_curriculum': 'Кружки и секции',
        r'_personal-plan': 'Песональный учебный план',
        r'_20students': 'Не более 20 учеников',
        r'_bez-pvz': 'Без взноса пвз',
        r'_dobavim': 'Добавим до Х%',
        r'_nakop': 'Накопить на квартиру',
        r'_dod': 'День открытых дверей',
        r'_1-11-klass': '1-11 классы',
        r'_invitation': 'Приглашаем на ДОД',
        r'_school-present': 'Презентация школы',
        r'_14feb': '14 февраля',
        r'_free-reс': 'бесплатные рекомендации',
        r'_10rec': '10 рекомендаций',
        r'_sravny': 'Сравнить с похожими людьми',
        r'_happy': 'Исследование счастья',
        r'_flash': 'Flash-sale',
        r'apart.ot-14.5': 'Минимальная цена',
        r'apart.bk|apart.pyatn.sh': 'Апартаменты',
        r'obsh-3.9|obsh0': 'Общий посыл',
        r'private-ter': 'Приватная территория',
        r'reka': 'Река',
        r'terrace': 'Терасса'
    }

    for key, value in segments.items():
        if re.search(key, ad_name):
            return value