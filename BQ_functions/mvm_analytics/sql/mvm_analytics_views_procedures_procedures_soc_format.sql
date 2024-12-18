### procedures.soc_format(campaign)
  CASE
    WHEN NOT REGEXP_CONTAINS(LOWER(campaign),r'mg_') THEN 'Докаты'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_flight') THEN 'Flight'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_mlt|_multi') THEN 'Мульти'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_crsl') THEN 'Карусель'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_bnr') THEN 'Баннер'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_rs|mg_pf_vk_alw_dir_kw_playstation_rf_approved') THEN 'Реклама сайта'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_dro') THEN 'Динамическая подборка товаров из фида (не ретаргетинг)'
    ELSE CONCAT('NaN - ',campaign)
  END