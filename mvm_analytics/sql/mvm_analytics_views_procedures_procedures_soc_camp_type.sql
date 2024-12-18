### procedures.soc_camp_type(campaign)
  CASE
    WHEN NOT REGEXP_CONTAINS(LOWER(campaign),r'mg_') THEN 'Докаты'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_flight_') THEN 'Flight'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_pf_') THEN 'Performance'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_md_') THEN 'Media'
    ELSE CONCAT('NaN - ',campaign)
  END