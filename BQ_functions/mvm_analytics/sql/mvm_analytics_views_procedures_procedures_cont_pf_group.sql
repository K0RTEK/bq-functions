### procedures.cont_pf_group(campaign,project)
### project: eldorado, mvideo
  CASE
    WHEN NOT REGEXP_CONTAINS(LOWER(campaign),r'mg_') AND REGEXP_CONTAINS(LOWER(campaign),r'_image_name') 
      THEN IF(project = 'mvideo','Яндекс Докаты (Бренд)','Докаты IProspect (Бренд)')
    WHEN NOT REGEXP_CONTAINS(LOWER(campaign),r'mg_') AND NOT REGEXP_CONTAINS(LOWER(campaign),r'_image_name') 
      THEN IF(project = 'mvideo','Яндекс Докаты (Небренд)','')

    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_image_name|_brand') 
      THEN IF(project = 'mvideo','Яндекс Бренд (общий)','Яндекс Бренд')

    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_dsa|_dsa-|shopping') 
      THEN IF(project = 'mvideo','Яндекс DSA','Яндекс DSA')

    WHEN REGEXP_CONTAINS(LOWER(campaign),r'smartbanner') 
      THEN IF(project = 'mvideo','Яндекс Ретаргетинг (Смарт-баннеры)','Яндекс Смарт-баннеры')
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_rem_|_rem-') 
      THEN IF(project = 'mvideo','Яндекс Ретаргетинг (Смарт-баннеры)','Яндекс Ремаркетинг')

    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_tk_') 
      THEN IF(project = 'mvideo','Яндекс Товарная РК','Яндекс Товарная РК')

    WHEN REGEXP_CONTAINS(LOWER(campaign),r'mg_mc_p_') 
      THEN 'Яндекс Мастер кампаний (остановили)'

    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_api_|_model_|_hand_|_model_h') 
      THEN IF(project = 'mvideo','Яндекс Api (к50)','Яндекс API (К50) + Модельные ручные')

    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_cat-ven_|_cat_|_category_') 
      THEN IF(project = 'mvideo','Яндекс Категорийные РК (модельные+катвенд) + Автотаргет','Яндекс Категорийные + Кат-вендорные + Автотаргет')
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'autotarget') 
      THEN IF(project = 'mvideo','Яндекс Категорийные РК (модельные+катвенд) + Автотаргет','Яндекс Категорийные + Кат-вендорные + Автотаргет')

    WHEN REGEXP_CONTAINS(LOWER(campaign),r'all_mb_smartphone|_all_categories_rsya|compet') 
      THEN IF(project = 'mvideo','Яндекс РСЯ (CPC)','Яндекс РСЯ (Бренд + Категорийная + Конкуренты)')

    ELSE CONCAT('NaN - ',campaign)
  END