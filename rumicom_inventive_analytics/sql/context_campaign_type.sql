-- procedures.context_campaign_type(campaign)

  CASE 
    WHEN REGEXP_CONTAINS(LOWER(campaign), r'brand') THEN 'Брендовая' 
    WHEN REGEXP_CONTAINS(LOWER(campaign), r'mkb') THEN 'МКБ'
    WHEN REGEXP_CONTAINS(LOWER(campaign), r'vendor') THEN 'Вендорная'
    WHEN REGEXP_CONTAINS(LOWER(campaign), r'model') THEN 'Модельная'
    WHEN REGEXP_CONTAINS(LOWER(campaign), r'dsa') THEN 'ДСА' 
    WHEN REGEXP_CONTAINS(LOWER(campaign), r'retargeting') THEN 'Ретаргетинг'
    WHEN REGEXP_CONTAINS(LOWER(campaign), r'smartbanner') THEN 'Смартбаннеры'
    WHEN REGEXP_CONTAINS(LOWER(campaign), r'tov_campaign_test1') THEN 'Товарная кампания (пн-чт)'
    WHEN REGEXP_CONTAINS(LOWER(campaign), r'tov_campaign_test2') THEN 'Товарная кампания (пт-вс)'
    WHEN REGEXP_CONTAINS(LOWER(campaign), r'tov') THEN 'Товарная'
    WHEN REGEXP_CONTAINS(LOWER(campaign), r'perfomance') THEN 'ЕПК'
    WHEN REGEXP_CONTAINS(LOWER(campaign), r'general') THEN 'General рк'
    WHEN REGEXP_CONTAINS(LOWER(campaign), r'elektrosamokaty_xiaomi') THEN 'РК по самокатам'
    WHEN REGEXP_CONTAINS(LOWER(campaign), r'pylesosy_xiaomi') THEN 'РК по пылесосам'
    ELSE 'NaN'
  END