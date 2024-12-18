import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_campaign_type(campaign):
    # Приведение строки к нижнему регистру
    campaign = is_none(campaign)

    # Проверка регулярных выражений по аналогии с CASE WHEN
    if re.search(r'brand', campaign):
        return 'Брендовая'
    elif re.search(r'cat_', campaign):
        return 'Категорийная'
    elif re.search(r'vendor', campaign):
        return 'Вендорная'
    elif re.search(r'model_hand', campaign):
        return 'Модельная'
    elif re.search(r'dsa', campaign):
        return 'ДСА'
    elif re.search(r'autotargeting', campaign):
        return 'Автотаргетинг'
    elif re.search(r'smartbanner', campaign):
        return 'Смартбаннеры'
    elif re.search(r'tovarnaya', campaign):
        return 'Товарная Кампания'
    elif re.search(r'model_k50', campaign):
        return 'к50'
    elif re.search(r'rem', campaign):
        return 'Ретаргетинг'
    elif re.search(r'artdigital', campaign):
        return 'Артдиджитал'
    elif re.search(r'model_epk|epk_all', campaign):
        return 'ЕПК'
    else:
        return 'Прочее'

