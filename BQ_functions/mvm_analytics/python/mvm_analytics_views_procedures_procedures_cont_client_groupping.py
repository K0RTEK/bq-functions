import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

import re

# Helper function to handle None values
def is_none(value):
    return value if value is not None else ''

def cont_client_groupping(campaign):
    campaign = is_none(campaign).lower()

    if not re.search(r'mg_', campaign):
        result = 'Докаты'
    elif re.search(r'_dsa.feed|_dsa.*_fid|dsa_.*_flight', campaign):
        result = 'DSA фид'
    elif re.search(r'_dsa.*content', campaign):
        result = 'DSA сайт'
    elif re.search(r'_dsa.gallery|yandex_shopping', campaign):
        result = 'DSA галерея'
    elif re.search(r'smartbanner', campaign):
        result = 'Смартбаннеры (рем)'
    elif re.search(r'_rem_|_rem-', campaign):
        result = 'Ремаркетинг'
    elif re.search(r'_image_name_p_', campaign) and not re.search(r'_cat_|_cat-ven_|_joint', campaign):
        result = 'Бренд общий'
    elif re.search(r'_image_name', campaign) and re.search(r'_cat-ven_', campaign):
        result = 'Бренд катвендор'
    elif re.search(r'_image_name', campaign) and re.search(r'_cat_', campaign):
        result = 'Бренд категорийный'
    elif re.search(r'_image_name', campaign) and re.search(r'_joint', campaign):
        result = 'Бренд смешанный'
    elif re.search(r'brand.*rsya', campaign):
        result = 'Бренд_РСЯ'
    elif re.search(r'_api_', campaign) and not re.search(r'_price', campaign):
        result = 'API-кампании (модельные K-50)'
    elif re.search(r'_api_', campaign) and re.search(r'_price', campaign):
        result = 'Остальное'
    elif re.search(r'_mc_', campaign):
        result = 'Мастер кампаний'
    elif re.search(r'_tk_', campaign):
        result = 'Торговые кампании'
    elif re.search(r'mg.*comp', campaign):
        result = 'Конкуренты'
    elif re.search(r'autotarget', campaign):
        result = 'Автотаргетинг'
    elif re.search(r'oups_yandexmarket', campaign):
        result = 'Я.Маркет'
    elif re.search(r'_category_', campaign):
        result = 'Категорийные ручные'
    elif re.search(r'_cat-ven_', campaign):
        result = 'Катвендорные ручные'
    elif re.search(r'_model_hand_', campaign):
        result = 'Модельные ручные'
    else:
        result = f'NaN - {campaign}'

    if re.search(r'_s_|rsya', campaign) and not re.search(r'_rem_|_rem-|smartbanner', campaign):
        result += ' РСЯ тотал'

    return result
