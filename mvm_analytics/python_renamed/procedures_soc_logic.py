import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def soc_logic(campaign):
    campaign = is_none(campaign)
    if re.search(r'mg_', campaign):
        return 'Докаты'
    elif re.search(r'_int', campaign):
        return 'Интересы'
    elif re.search(r'_lal', campaign):
        return 'Look-alike'
    elif re.search(r'_grps', campaign):
        return 'Подписчики групп'
    elif re.search(r'_kw', campaign):
        return 'Ключевые запросы'
    elif re.search(r'_eng', campaign):
        return 'Заинтересованная аудитория (ВК)'
    elif re.search(r'_socdem', campaign):
        return 'Ограничения по возрасту и полу'
    elif re.search(r'_cart|_сart', campaign):
        return 'Добавили в корзину но не купили'
    elif re.search(r'_view', campaign):
        return 'Просмотры товаров'
    elif re.search(r'_checkout', campaign):
        return 'Начало оформления заказа'
    elif re.search(r'_purch', campaign):
        return 'Покупатели'
    elif re.search(r'_all', campaign):
        return 'Все взаимодействия с фидом'
    elif re.search(r'_comp', campaign):
        return 'Конкуренты (ключи, группы)'
    elif re.search(r'_base', campaign):
        return 'База, спиосок клиентов CRM'
    elif re.search(r'_pix', campaign):
        return 'Пиксель (для ретаргетинга, LAL)'
    elif re.search(r'_wide', campaign):
        return 'Привлечение потенциальных клиентов (площадка сама подбирает аудиторию)'
    else:
        return 'NaN - ' + campaign