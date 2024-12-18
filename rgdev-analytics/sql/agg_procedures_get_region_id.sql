### agg_procedures.get_region_id(date,source,medium,campaign,content,term)

  CASE
    WHEN source = 'yd' AND medium = 'cpc' 
      THEN REGEXP_EXTRACT(LOWER(content),r'reg:([0-9]+)')

    ELSE NULL
  END