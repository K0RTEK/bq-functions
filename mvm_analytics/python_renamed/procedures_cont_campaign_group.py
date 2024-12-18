import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def cont_campaign_group(campaign):
    campaign = is_none(campaign)
    if re.search(r'mg_', campaign) is None:
        return 'Докаты'
    elif re.search(r'_image_name', campaign):
        return 'Бренд'
    elif re.search(r'brand.*rsya', campaign):
        return 'Бренд РСЯ'
    elif re.search(r'_dsa_', campaign):
        return 'DSA'
    elif re.search(r'smartbanner', campaign):
        return 'Смартбаннеры'
    elif re.search(r'_tk_', campaign):
        return 'Товарные кампании'
    elif re.search(r'_api_|_model_', campaign):
        return 'Модельные'
    elif re.search(r'_hand_', campaign):
        return 'Ручные'
    elif re.search(r'_cat-ven_', campaign):
        return 'Категорийно-вендорные'
    elif re.search(r'_category_', campaign):
        return 'Категорийные'
    elif re.search(r'_rem_|_rem-', campaign):
        return 'Ремаркетинг'
    elif re.search(r'autotarget', campaign):
        return 'Автотаргетинг'
    elif re.search(r'_mc_', campaign):
        return 'Мастер кампаний'
    else:
        return 'NaN - ' + campaign