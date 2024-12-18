### procedures.cont_mg_or_non_mg(campaign,project_name)

--изменения по задаче https://pf.mgcom.ru/task/1133201
  CASE
    WHEN project_name = 'eldorado' AND REGEXP_CONTAINS(LOWER(campaign),r'dsa|_tk_|_smartbanners_|image|_autotarget_|yandex_shopping_segmented_') AND NOT REGEXP_CONTAINS(LOWER(campaign),r'flight')  
      THEN 'non-MGCom'
    WHEN project_name = 'mvideo' AND REGEXP_CONTAINS(LOWER(campaign),r'image') AND NOT REGEXP_CONTAINS(LOWER(campaign),r'flight')
      THEN 'non-MGCom'
    ELSE 'MGCom'


    -- WHEN project_name = 'eldorado' AND NOT REGEXP_CONTAINS(LOWER(campaign),r'flight|image') AND REGEXP_CONTAINS(LOWER(campaign),r'_api_|_cat-ven_|mg_rem|_all_mb_smartphone_|_all_categories_|mg_category_|_model_hand_|_competitors|brand_rsya') 
    --   THEN 'MGCom'
    -- WHEN project_name = 'eldorado' AND REGEXP_CONTAINS(LOWER(campaign),r'_eldo_flight_rf_fed_')
    --   THEN 'MGCom'
    -- WHEN project_name = 'mvideo' AND NOT REGEXP_CONTAINS(LOWER(campaign),r'flight|image') AND REGEXP_CONTAINS(LOWER(campaign),r'_api_|_cat-ven_|mg_rem|_all_mb_smartphone_|_all_categories_|mg_category_|_model_hand_|_competitors') 
    --   THEN 'MGCom'
    -- WHEN project_name = 'mvideo' AND REGEXP_CONTAINS(LOWER(campaign),r'_mv_flight_rf_fed_')
    --   THEN 'MGCom'
    -- ELSE 'non-MGCom'
  END