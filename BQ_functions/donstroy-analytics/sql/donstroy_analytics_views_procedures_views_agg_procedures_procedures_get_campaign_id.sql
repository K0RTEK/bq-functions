-- agg_procedures.get_campaign_id(date,utm_source,utm_medium,utm_campaign,utm_content,utm_term)
  
  CASE
  ### agg_context_yandex
    WHEN utm_source = 'yandex' AND utm_medium = 'cpc' THEN 
      CASE
        WHEN REGEXP_CONTAINS(LOWER(TRIM(utm_content)),r'c:[0-9]+') 
          THEN REGEXP_EXTRACT(LOWER(utm_content),r'c:([0-9]+)')
        WHEN REGEXP_CONTAINS(LOWER(TRIM(utm_campaign)),r'\|[0-9]+') 
          THEN REGEXP_EXTRACT(LOWER(utm_campaign),r'\|([0-9]+)')
        ELSE 'NaN'
      END
    ELSE 'NaN'
  END