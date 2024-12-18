### agg_procedures.get_criterion_id(date,source,medium,campaign,content,term)
  CASE
    WHEN source = 'yd' AND medium = 'cpc' 
      THEN REGEXP_EXTRACT(LOWER(content),r'astat:([0-9]+)')

    ELSE NULL
  END