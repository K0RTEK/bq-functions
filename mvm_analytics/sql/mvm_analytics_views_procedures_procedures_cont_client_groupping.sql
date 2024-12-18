### procedures.cont_client_groupping(campaign)
  CONCAT(
    CASE
      WHEN NOT REGEXP_CONTAINS(LOWER(campaign),r'mg_') THEN 'Докаты'
      WHEN REGEXP_CONTAINS(LOWER(campaign),r'_dsa.feed|_dsa.*_fid|dsa_.*_flight') THEN 'DSA фид'
      WHEN REGEXP_CONTAINS(LOWER(campaign),r'_dsa.*content') THEN 'DSA сайт'
      WHEN REGEXP_CONTAINS(LOWER(campaign),r'_dsa.gallery|yandex_shopping') THEN 'DSA галерея'

      WHEN REGEXP_CONTAINS(LOWER(campaign),r'smartbanner') THEN 'Смартбаннеры (рем)'
      WHEN REGEXP_CONTAINS(LOWER(campaign),r'_rem_|_rem-') THEN 'Ремаркетинг'

      WHEN REGEXP_CONTAINS(LOWER(campaign),r'_image_name_p_') AND NOT REGEXP_CONTAINS(LOWER(campaign),r'_cat_|_cat-ven_|_joint') THEN 'Бренд общий'
      WHEN REGEXP_CONTAINS(LOWER(campaign),r'_image_name') AND REGEXP_CONTAINS(LOWER(campaign),r'_cat-ven_') THEN 'Бренд катвендор'
      WHEN REGEXP_CONTAINS(LOWER(campaign),r'_image_name') AND REGEXP_CONTAINS(LOWER(campaign),r'_cat_') THEN 'Бренд категорийный'
      WHEN REGEXP_CONTAINS(LOWER(campaign),r'_image_name') AND REGEXP_CONTAINS(LOWER(campaign),r'_joint') THEN 'Бренд смешанный'
      WHEN REGEXP_CONTAINS(LOWER(campaign),r'brand.*rsya') THEN 'Бренд_РСЯ'

      WHEN REGEXP_CONTAINS(LOWER(campaign),r'_api_') AND NOT REGEXP_CONTAINS(LOWER(campaign),r'_price') THEN 'API-кампании (модельные K-50)'
      WHEN REGEXP_CONTAINS(LOWER(campaign),r'_api_') AND REGEXP_CONTAINS(LOWER(campaign),r'_price') THEN 'Остальное'
      WHEN REGEXP_CONTAINS(LOWER(campaign),r'_mc_') THEN 'Мастер кампаний'
      WHEN REGEXP_CONTAINS(LOWER(campaign),r'_tk_') THEN 'Торговые кампании'
      WHEN REGEXP_CONTAINS(LOWER(campaign),r'mg.*comp') THEN 'Конкуренты'
      WHEN REGEXP_CONTAINS(LOWER(campaign),r'autotarget') THEN 'Автотаргетинг'
      WHEN REGEXP_CONTAINS(LOWER(campaign),r'oups_yandexmarket') THEN 'Я.Маркет'

      WHEN REGEXP_CONTAINS(LOWER(campaign),r'_category_') THEN 'Категорийные ручные'
      WHEN REGEXP_CONTAINS(LOWER(campaign),r'_cat-ven_') THEN 'Катвендорные ручные'
      WHEN REGEXP_CONTAINS(LOWER(campaign),r'_model_hand_') THEN 'Модельные ручные'
      ELSE CONCAT('NaN - ',campaign)
    END,
    IF(REGEXP_CONTAINS(LOWER(campaign),r'_s_|rsya') AND NOT REGEXP_CONTAINS(LOWER(campaign),r'_rem_|_rem-|smartbanner'),' РСЯ тотал','')
  )