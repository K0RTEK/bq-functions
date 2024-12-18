-- procedures.social_clarification(campaign, date)

CASE

  WHEN date <= '2022-12-31' THEN 'NaN'

  WHEN date > '2022-12-31' THEN 
    CASE 
      WHEN REGEXP_CONTAINS(LOWER(campaign), r'14d_') THEN '14 дней' 
      WHEN REGEXP_CONTAINS(LOWER(campaign), r'10d_') THEN '10 дней' 
      WHEN REGEXP_CONTAINS(LOWER(campaign), r'7d_|pf_m_dir_kw_s22_msk_23-55_multi_cross_mt|pf_m_dir_kw_s22_rf_23-55_multi_cross_mt|pf_m_dir_kw_flip4_msk_23-55_multi_cross_mt|pf_m_dir_kw_flip4_rf_23-55_multi_cross_mt|pf_m_dir_kw_fold4_msk_23-55_multi_cross_mt|pf_m_dir_kw_fold4_rf_23-55_multi_cross_mt') THEN '7 дней' 
      WHEN REGEXP_CONTAINS(LOWER(campaign), r'phone_') THEN 'Интерес к покупке мобильного телефона'
      WHEN REGEXP_CONTAINS(LOWER(campaign), r'checkout') THEN 'Начало оформления заказа'
      WHEN REGEXP_CONTAINS(LOWER(campaign), r'cart') THEN 'Корзина'
      WHEN REGEXP_CONTAINS(LOWER(campaign), r'auto') THEN 'Автоинтересы'
      WHEN REGEXP_CONTAINS(LOWER(campaign), r'brand-3d') THEN 'Брендовые ключи 3 дня'
      WHEN REGEXP_CONTAINS(LOWER(campaign), r'view') THEN 'Просмотр'
      WHEN REGEXP_CONTAINS(LOWER(campaign), r'action') THEN 'Любое действие'
      WHEN REGEXP_CONTAINS(LOWER(campaign), r'site14') THEN 'Посещение сайта в течение 14 дней'
      ELSE 'NaN'
    END

END