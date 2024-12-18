### dash_procedures.get_soc_traf_type(campaign)
  CASE
    WHEN NOT REGEXP_CONTAINS(LOWER(campaign),r'mg_') THEN 'Докаты'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_flight_') THEN 'Flight'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_dir_') THEN 'Прямой'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_dnmc_') THEN 'Динрем'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_sttc_') THEN 'Статический ретаргетинг'
    ELSE CONCAT('NaN - ',campaign)
  END