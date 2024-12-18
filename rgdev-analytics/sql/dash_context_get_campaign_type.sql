CASE
    WHEN REGEXP_CONTAINS(campaign_name,r'mkb') THEN 'МКБ'
    WHEN REGEXP_CONTAINS(campaign_name,r'_s_.*brand_development') THEN 'Поиск_бренд застройщика'
    WHEN REGEXP_CONTAINS(campaign_name,r'_s_.*brand') THEN 'Поиск_бренд'
    WHEN REGEXP_CONTAINS(campaign_name,r'_s_.*remarketing') THEN 'Поиск_ретаргетинг'
    WHEN REGEXP_CONTAINS(campaign_name,r'_s_.*convert') THEN 'Поиск_общие'
    WHEN REGEXP_CONTAINS(campaign_name,r'_s_.*geo') THEN 'Поиск_Гео'
    WHEN REGEXP_CONTAINS(campaign_name,r'_mk_') THEN 'Мастер кампаний'
    WHEN REGEXP_CONTAINS(campaign_name,r'_n_.*retargeting') THEN 'РСЯ_Ретаргетинг'
    WHEN REGEXP_CONTAINS(campaign_name,r'_n_.*smart_banner') THEN 'Смартбаннеры'
    WHEN REGEXP_CONTAINS(campaign_name,r'_n_|_epk_') THEN 'РСЯ'
    WHEN REGEXP_CONTAINS(campaign_name,r'quiz') THEN 'Квиз'
  END