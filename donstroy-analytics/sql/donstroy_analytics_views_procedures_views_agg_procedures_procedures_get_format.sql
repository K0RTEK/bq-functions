### agg_procedures.get_format`(date,ct_source,ct_medium,crm_advertising_source,utm_source,utm_medium,utm_campaign,utm_content,utm_term)
  CASE
    WHEN REGEXP_CONTAINS(LOWER(utm_term),'tgb') OR REGEXP_CONTAINS(LOWER(utm_source),'tgb') THEN 'ТГБ'
    WHEN REGEXP_CONTAINS(LOWER(utm_term),'banner') OR REGEXP_CONTAINS(LOWER(utm_source),'banner') THEN 'Баннер'
    WHEN REGEXP_CONTAINS(LOWER(utm_term),'spec') OR REGEXP_CONTAINS(LOWER(utm_source),'spec') THEN 'Спецпроект'
    WHEN REGEXP_CONTAINS(LOWER(utm_term),'pin')THEN 'PIN'
    WHEN REGEXP_CONTAINS(LOWER(utm_term),'poi') THEN 'POI'
    WHEN REGEXP_CONTAINS(LOWER(utm_term),'billboard') THEN 'Биллборд'
    WHEN REGEXP_CONTAINS(LOWER(utm_term),'snippet') THEN 'Сниппет'
    WHEN REGEXP_CONTAINS(LOWER(utm_term),'push') OR REGEXP_CONTAINS(LOWER(utm_medium),'push') THEN 'Пуш'
    WHEN REGEXP_CONTAINS(LOWER(utm_term),'kontekstno') THEN 'Контекстное размещение'
    WHEN REGEXP_CONTAINS(LOWER(utm_term),'statika') THEN 'Статика'
    WHEN REGEXP_CONTAINS(LOWER(utm_term),'brendiro') THEN 'Брендирование'
    ELSE 'NaN'
  END