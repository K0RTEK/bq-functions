### agg_procedures.get_device(date,source,medium,campaign,content,term)
  CASE
    WHEN source = 'yd' AND medium = 'cpc' 
      THEN REGEXP_EXTRACT(LOWER(content),r'dvc:([^|]+)')

    ELSE NULL
  END