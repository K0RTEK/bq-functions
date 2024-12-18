import re
import datetime as dt

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def context_campaign_type(campaign):
    campaign = is_none(campaign)
    if re.search(r'brand', campaign):
        return 'Брендовая'
    elif re.search(r'cat_vendor_bt_', campaign):
        return 'Катвендорная КБТ'
    elif re.search(r'cat_|cat_vendor', campaign):
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
    elif re.search(r'hand-gmc', campaign):
        return 'Смарт-шоппинг'
    elif re.search(r'model_k50', campaign):
        return 'к50'
    elif re.search(r'tovarnaya_test1_rf', campaign):
        return 'Товарная кампания Пн-Чт'
    elif re.search(r'tovarnaya_test2_rf', campaign):
        return 'Товарная кампания Пт-Вс'
    elif re.search(r'tovarnaya_lowaov_rf', campaign):
        return 'Товарная кампания Низкие чеки'
    elif re.search(r'tovarnaya2_rf', campaign):
        return 'Товарная кампания Высокие чеки'
    elif re.search(r'rem', campaign):
        return 'Ретаргетинг корзина'
    elif re.search(r'general', campaign):
        return 'Объединенные модельные и категорийные'
    elif re.search(r'epk', campaign):
        return 'ЕПК'
    else:
        return 'NaN'