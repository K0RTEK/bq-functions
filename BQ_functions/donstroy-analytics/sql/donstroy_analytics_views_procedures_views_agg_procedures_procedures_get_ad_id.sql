-- agg_procedures.get_ad_id(date,utm_source,utm_medium,utm_campaign,utm_content,utm_term)
  
  CASE
  ### agg_context_yandex
    WHEN utm_source = 'yandex' AND utm_medium = 'cpc' THEN 
      CASE
        WHEN REGEXP_CONTAINS(LOWER(TRIM(utm_content)),r'a:[0-9]+') 
          THEN REGEXP_EXTRACT(LOWER(utm_content),r'a:([0-9]+)')
        ELSE 'NaN'
      END
    ELSE 'NaN'
  END