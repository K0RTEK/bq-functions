### agg_procedures.get_criterion_id`(date,source,medium,campaign,content,term)
    CASE
      WHEN source = 'yandex' AND medium = 'cpc' THEN REGEXP_EXTRACT(LOWER(content),r'ph:([0-9]+)')
      ELSE 'NaN'
    END