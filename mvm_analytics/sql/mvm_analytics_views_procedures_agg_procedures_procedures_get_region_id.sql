### agg_procedures.get_region_id(date,project,source,medium,campaign,content,term)
    CASE
      WHEN source = 'yandex' AND medium = 'cpc' THEN REGEXP_EXTRACT(LOWER(content),r'region:([0-9]+)')
      ELSE 'NaN'
    END