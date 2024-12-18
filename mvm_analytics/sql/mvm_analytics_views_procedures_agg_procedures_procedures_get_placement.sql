### agg_procedures.get_placement`(date,source,medium,campaign,content,term)
    CASE
      WHEN source = 'yandex' AND medium = 'cpc' THEN REGEXP_EXTRACT(LOWER(content),r'src:([^|]+)')
      ELSE 'NaN'
    END