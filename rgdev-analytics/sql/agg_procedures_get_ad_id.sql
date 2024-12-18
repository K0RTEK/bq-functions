### agg_procedures.get_ad_id(date,source,medium,campaign,content,term)
  CASE
    ### Яндекс Директ
    WHEN source = 'yd' AND medium = 'cpc' 
      THEN REGEXP_EXTRACT(LOWER(content),r'aid:([0-9]+)')
    
    ELSE NULL
  END