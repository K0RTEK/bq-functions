### procedures.cont_campaign_type(campaign)
  CASE
    WHEN NOT REGEXP_CONTAINS(LOWER(campaign),r'mg_') THEN 'Докаты'

    -- WHEN REGEXP_CONTAINS(LOWER(campaign),r'rsya') THEN 'РСЯ'

    WHEN REGEXP_CONTAINS(LOWER(campaign),r'brand.*rsya|_image_name_s_') AND NOT REGEXP_CONTAINS(LOWER(campaign),r'_smartbanner|_rem_|_rem-|_p_') THEN 'Бренд РСЯ'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'categories_rsya') AND NOT REGEXP_CONTAINS(LOWER(campaign),r'_smartbanner|_rem_|_rem-|_p_') THEN 'РСЯ Категории'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'competitors_rsya|competitors_s_') AND NOT REGEXP_CONTAINS(LOWER(campaign),r'_smartbanner|_rem_|_rem-|_p_') THEN 'РСЯ Конкуренты'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_shared_keys_') AND NOT REGEXP_CONTAINS(LOWER(campaign),r'_smartbanner|_rem_|_rem-|_p_') THEN 'РСЯ Общие ключи'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_interesi_|_interests_') AND NOT REGEXP_CONTAINS(LOWER(campaign),r'_smartbanner|_rem_|_rem-|_p_') THEN 'РСЯ Интересы'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_rsya|_s_') AND NOT REGEXP_CONTAINS(LOWER(campaign),r'_smartbanner|_rem_|_rem-|_p_') THEN 'РСЯ Остальное'

    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_image_name') AND NOT REGEXP_CONTAINS(LOWER(campaign),r'_cat_|_cat-ven_|_joint') THEN 'Бренд общий'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_image_name') AND REGEXP_CONTAINS(LOWER(campaign),r'_cat-ven_') THEN 'Бренд категорийно-вендорный'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_image_name') AND REGEXP_CONTAINS(LOWER(campaign),r'_cat_') THEN 'Бренд категорийный'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_image_name') AND REGEXP_CONTAINS(LOWER(campaign),r'_joint') THEN 'Бренд комбинированный'

    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_dsa.feed|_dsa.*_fid|dsa_.*_flight') THEN 'DSA по фиду'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_dsa.*content') THEN 'DSA по сайту'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_dsa.gallery|yandex_shopping') THEN 'DSA галерея'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'vch_keywords') THEN 'ВЧ Ключи'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'competitors_markpl') THEN 'Конкуренты маркетплейсы'

    -- Вита добавила 30.11
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_rem_competitors') THEN 'Конкуренты ремаркетинг'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'telegramm') THEN 'Телеграмм'

    WHEN REGEXP_CONTAINS(LOWER(campaign),r'smartbanner') AND NOT REGEXP_CONTAINS(LOWER(campaign),r'_competitors_') THEN 'Смартбаннеры'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_tk_') THEN 'Товарные кампании'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_api_') THEN 'Модельные К50'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'model|_model_h') THEN 'Модельные ручные'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_hand_') THEN 'Ручные'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_cat-ven_|_cat-combined_') THEN 'Категорийно-вендорные'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_category_') THEN 'Категорийные'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_rem_|_rem-') AND NOT REGEXP_CONTAINS(LOWER(campaign),r'_smartbanners_|_competitors_') THEN 'Ремаркетинг'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'autotarget') AND NOT REGEXP_CONTAINS(LOWER(campaign),r'_mc_') THEN 'Автотаргетинг'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_mc_|_mс_') AND NOT REGEXP_CONTAINS(LOWER(campaign),r'_s_') THEN 'Мастер кампаний'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_compet') THEN 'Конкуренты'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'oups_yandexmarket') THEN 'Я.Маркет'

    -- Вита добавила 21.11
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_epk_|_united_') THEN 'Единая Перформанс Кампания'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_vendors_') THEN 'Вендорские запросы'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'black_friday') THEN 'Чёрная Пятница'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_pred-audience_') THEN 'Предиктивные аудитории'

    ELSE CONCAT('NaN - ',campaign)
  END