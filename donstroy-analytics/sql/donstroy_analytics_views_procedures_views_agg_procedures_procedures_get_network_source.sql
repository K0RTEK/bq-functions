-- agg_procedures.get_network_source(date,utm_source,utm_medium,utm_campaign,utm_content,utm_term)
  
  CASE
  ### agg_context_yandex
    WHEN utm_source = 'yandex' AND utm_medium = 'cpc' THEN 
      CASE
        WHEN REGEXP_CONTAINS(LOWER(TRIM(utm_content)),r'\|s:[^|]+') 
          THEN REGEXP_EXTRACT(LOWER(utm_content),r'\|s:([^|]+)')
        ELSE 'NaN'
      END
    ELSE 'NaN'
  END