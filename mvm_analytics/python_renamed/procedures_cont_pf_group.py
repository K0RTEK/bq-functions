import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def cont_pf_group(campaign,project):
    campaign = is_none(campaign)
    project = is_none(project)
    if not re.search(r'mg_',campaign) and re.search(r'_image_name',campaign):
        return 'Яндекс Докаты (Бренд)' if project == 'mvideo' else 'Докаты IProspect (Бренд)'
    elif not re.search(r'mg_',campaign) and not re.search(r'_image_name',campaign):
        return 'Яндекс Докаты (Небренд)' if project == 'mvideo' else ''
    elif re.search(r'_image_name|_brand',campaign):
        return 'Яндекс Бренд (общий)' if project == 'mvideo' else 'Яндекс Бренд'
    elif re.search(r'_dsa|_dsa-|shopping',campaign):
        return 'Яндекс DSA' if project == 'mvideo' else 'Яндекс DSA'
    elif re.search(r'smartbanner',campaign):
        return 'Яндекс Ретаргетинг (Смарт-баннеры)' if project == 'mvideo' else 'Яндекс Смарт-баннеры'
    elif re.search(r'_rem_|_rem-',campaign):
        return 'Яндекс Ретаргетинг (Смарт-баннеры)' if project == 'mvideo' else 'Яндекс Ремаркетинг'
    elif re.search(r'_tk_',campaign):
        return 'Яндекс Товарная РК' if project == 'mvideo' else 'Яндекс Товарная РК'
    elif re.search(r'mg_mc_p_',campaign):
        return 'Яндекс Мастер кампаний (остановили)'
    elif re.search(r'_api_|_model_|_hand_|_model_h',campaign):
        return 'Яндекс Api (к50)' if project == 'mvideo' else 'Яндекс API (К50) + Модельные ручные'
    elif re.search(r'_cat-ven_|_cat_|_category_',campaign):
        return 'Яндекс Категорийные РК (модельные+катвенд) + Автотаргет' if project == 'mvideo' else 'Яндекс Категорийные + Кат-вендорные + Автотаргет'
    elif re.search(r'autotarget',campaign):
        return 'Яндекс Категорийные РК (модельные+катвенд) + Автотаргет' if project == 'mvideo' else 'Яндекс Категорийные + Кат-вендорные + Автотаргет'
    elif re.search(r'all_mb_smartphone|_all_categories_rsya|compet',campaign):
        return 'Яндекс РСЯ (CPC)' if project == 'mvideo' else 'Яндекс РСЯ (Бренд + Категорийная + Конкуренты)'
    else:
        return 'NaN - ' + campaign