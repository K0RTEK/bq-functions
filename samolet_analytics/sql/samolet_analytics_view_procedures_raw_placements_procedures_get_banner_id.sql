### raw_placements.get_banner_id(utm_content)
  CASE
    WHEN REGEXP_CONTAINS(LOWER(utm_content),r'adid:') THEN REGEXP_EXTRACT(LOWER(utm_content),r'adid:([0-9]+)')
    WHEN REGEXP_CONTAINS(LOWER(utm_content),r'adid":') THEN REGEXP_EXTRACT(LOWER(utm_content),r'adid":([0-9]+)')
    WHEN NOT REGEXP_CONTAINS(LOWER(utm_content),r'[^0-9]') THEN REGEXP_EXTRACT(LOWER(utm_content),r'[0-9]+')
  END