-- procedures.context_campaign_type(campaign)

  CASE 
    WHEN REGEXP_CONTAINS(LOWER(campaign), r'brand') THEN 'Брендовая' 
    WHEN REGEXP_CONTAINS(LOWER(campaign), r'cat_vendor_bt_') THEN 'Катвендорная КБТ'
    WHEN REGEXP_CONTAINS(LOWER(campaign), r'cat_|cat_vendor') THEN 'Категорийная'
    WHEN REGEXP_CONTAINS(LOWER(campaign), r'vendor') THEN 'Вендорная'
    WHEN REGEXP_CONTAINS(LOWER(campaign), r'model_hand') THEN 'Модельная'
    WHEN REGEXP_CONTAINS(LOWER(campaign), r'dsa') THEN 'ДСА' 
    WHEN REGEXP_CONTAINS(LOWER(campaign), r'autotargeting') THEN 'Автотаргетинг'
    WHEN REGEXP_CONTAINS(LOWER(campaign), r'smartbanner') THEN 'Смартбаннеры'
    WHEN REGEXP_CONTAINS(LOWER(campaign), r'hand-gmc') THEN 'Смарт-шоппинг'
    WHEN REGEXP_CONTAINS(LOWER(campaign), r'model_k50') THEN 'к50'
    WHEN REGEXP_CONTAINS(LOWER(campaign), r'tovarnaya_test1_rf') THEN 'Товарная кампания Пн-Чт'
    WHEN REGEXP_CONTAINS(LOWER(campaign), r'tovarnaya_test2_rf') THEN 'Товарная кампания Пт-Вс'
    WHEN REGEXP_CONTAINS(LOWER(campaign), r'tovarnaya_lowaov_rf') THEN 'Товарная кампания Низкие чеки'
    WHEN REGEXP_CONTAINS(LOWER(campaign), r'tovarnaya2_rf') THEN 'Товарная кампания Высокие чеки'
    WHEN REGEXP_CONTAINS(LOWER(campaign), r'rem') THEN 'Ретаргетинг корзина'
    WHEN REGEXP_CONTAINS(LOWER(campaign), r'general') THEN 'Объединенные модельные и категорийные'
    WHEN REGEXP_CONTAINS(LOWER(campaign), r'epk') THEN 'ЕПК'
    ELSE 'NaN'
  END