### agg_procedures.get_device`(date,source,medium,campaign,content,term)
    -- CASE
    --   WHEN source = 'yandex' AND medium = 'cpc' THEN REGEXP_EXTRACT(LOWER(content),r'dvc:([^|]+)')
    --   ELSE 'NaN'
    -- END

    CASE
      WHEN REGEXP_CONTAINS(LOWER(content),r'dvc:mobile') THEN 'mobile'
      WHEN REGEXP_CONTAINS(LOWER(content),r'dvc:desktop') THEN 'desktop'
      WHEN REGEXP_CONTAINS(LOWER(content),r'dvc:tablet') THEN 'tablet'
      ELSE 'NaN'
    END