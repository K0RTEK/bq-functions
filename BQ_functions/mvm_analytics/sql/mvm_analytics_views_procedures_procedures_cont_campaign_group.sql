### procedures.cont_campaign_group(campaign)
  CASE
    WHEN NOT REGEXP_CONTAINS(LOWER(campaign),r'mg_') THEN 'Докаты'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_image_name') THEN 'Бренд'

    WHEN REGEXP_CONTAINS(LOWER(campaign),r'brand.*rsya') THEN 'Бренд РСЯ'

    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_dsa_') THEN 'DSA'

    WHEN REGEXP_CONTAINS(LOWER(campaign),r'smartbanner') THEN 'Смартбаннеры'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_tk_') THEN 'Товарные кампании'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_api_|_model_') THEN 'Модельные'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_hand_') THEN 'Ручные'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_cat-ven_') THEN 'Категорийно-вендорные'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_category_') THEN 'Категорийные'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_rem_|_rem-') THEN 'Ремаркетинг'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'autotarget') THEN 'Автотаргетинг'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_mc_') THEN 'Мастер кампаний'
    ELSE CONCAT('NaN - ',campaign)
  END