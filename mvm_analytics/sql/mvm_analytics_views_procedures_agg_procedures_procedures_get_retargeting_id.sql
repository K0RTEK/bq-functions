### agg_procedures.get_retargeting_id`(date,source,medium,campaign,content,term)
    CASE
      ### Яндекс Директ
      WHEN source = 'yandex' AND medium = 'cpc' 
        THEN REGEXP_EXTRACT(LOWER(content),r're:([0-9]+)')
      
      ELSE 'NaN'
    END