import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()
    
import re



def cont_campaign_type(campaign):
    campaign = is_none(campaign).lower()

    if not re.search(r'mg_', campaign):
        return 'Докаты'

    elif re.search(r'brand.*rsya|_image_name_s_', campaign) and not re.search(r'_smartbanner|_rem_|_rem-|_p_', campaign):
        return 'Бренд РСЯ'

    elif re.search(r'categories_rsya', campaign) and not re.search(r'_smartbanner|_rem_|_rem-|_p_', campaign):
        return 'РСЯ Категории'

    elif re.search(r'competitors_rsya|competitors_s_', campaign) and not re.search(r'_smartbanner|_rem_|_rem-|_p_', campaign):
        return 'РСЯ Конкуренты'

    elif re.search(r'_shared_keys_', campaign) and not re.search(r'_smartbanner|_rem_|_rem-|_p_', campaign):
        return 'РСЯ Общие ключи'

    elif re.search(r'_interesi_|_interests_', campaign) and not re.search(r'_smartbanner|_rem_|_rem-|_p_', campaign):
        return 'РСЯ Интересы'

    elif re.search(r'_rsya|_s_', campaign) and not re.search(r'_smartbanner|_rem_|_rem-|_p_', campaign):
        return 'РСЯ Остальное'

    elif re.search(r'_image_name', campaign) and not re.search(r'_cat_|_cat-ven_|_joint', campaign):
        return 'Бренд общий'

    elif re.search(r'_image_name', campaign) and re.search(r'_cat-ven_', campaign):
        return 'Бренд категорийно-вендорный'

    elif re.search(r'_image_name', campaign) and re.search(r'_cat_', campaign):
        return 'Бренд категорийный'

    elif re.search(r'_image_name', campaign) and re.search(r'_joint', campaign):
        return 'Бренд комбинированный'

    elif re.search(r'_dsa.feed|_dsa.*_fid|dsa_.*_flight', campaign):
        return 'DSA по фиду'

    elif re.search(r'_dsa.*content', campaign):
        return 'DSA по сайту'

    elif re.search(r'_dsa.gallery|yandex_shopping', campaign):
        return 'DSA галерея'

    elif re.search(r'vch_keywords', campaign):
        return 'ВЧ Ключи'

    elif re.search(r'competitors_markpl', campaign):
        return 'Конкуренты маркетплейсы'

    # Added by Вита on 30.11
    elif re.search(r'_rem_competitors', campaign):
        return 'Конкуренты ремаркетинг'

    elif re.search(r'telegramm', campaign):
        return 'Телеграмм'

    elif re.search(r'smartbanner', campaign) and not re.search(r'_competitors_', campaign):
        return 'Смартбаннеры'

    elif re.search(r'_tk_', campaign):
        return 'Товарные кампании'

    elif re.search(r'_api_', campaign):
        return 'Модельные К50'

    elif re.search(r'model|_model_h', campaign):
        return 'Модельные ручные'

    elif re.search(r'_hand_', campaign):
        return 'Ручные'

    elif re.search(r'_cat-ven_|_cat-combined_', campaign):
        return 'Категорийно-вендорные'

    elif re.search(r'_category_', campaign):
        return 'Категорийные'

    elif re.search(r'_rem_|_rem-', campaign) and not re.search(r'_smartbanners_|_competitors_', campaign):
        return 'Ремаркетинг'

    elif re.search(r'autotarget', campaign) and not re.search(r'_mc_', campaign):
        return 'Автотаргетинг'

    elif re.search(r'_mc_|_mс_', campaign) and not re.search(r'_s_', campaign):
        return 'Мастер кампаний'

    elif re.search(r'_compet', campaign):
        return 'Конкуренты'

    elif re.search(r'oups_yandexmarket', campaign):
        return 'Я.Маркет'

    elif re.search(r'_epk_|_united_', campaign):
        return 'Единая Перформанс Кампания'

    elif re.search(r'_vendors_', campaign):
        return 'Вендорские запросы'

    elif re.search(r'black_friday', campaign):
        return 'Чёрная Пятница'

    elif re.search(r'_pred-audience_', campaign):
        return 'Предиктивные аудитории'

    return f'NaN - {campaign}'
