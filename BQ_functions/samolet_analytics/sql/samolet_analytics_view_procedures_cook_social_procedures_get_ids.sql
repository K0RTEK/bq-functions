CASE
    WHEN id_type IN ('ad_id','adid') AND REGEXP_CONTAINS(LOWER(parameter),r'adid:([0-9]+)') THEN REGEXP_EXTRACT(LOWER(parameter),r'adid:([0-9]+)')
    WHEN id_type IN ('ad_id','adid') AND REGEXP_CONTAINS(LOWER(parameter),r'[0-9]+') AND NOT REGEXP_CONTAINS(LOWER(parameter),r'[^0-9]') THEN REGEXP_EXTRACT(LOWER(parameter),r'[0-9]+')
  END