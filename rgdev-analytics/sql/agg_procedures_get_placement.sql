### agg_procedures.get_placement(date,source,medium,campaign,content,term)

  CASE
    WHEN source = 'yd' AND medium = 'cpc' 
      THEN REGEXP_EXTRACT(LOWER(content),r'src:([^|]+)')

    ELSE NULL
  END