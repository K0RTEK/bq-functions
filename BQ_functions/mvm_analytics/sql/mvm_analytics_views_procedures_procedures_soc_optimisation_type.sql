### procedures.soc_optimisation_type(campaign)
  CASE
    WHEN NOT REGEXP_CONTAINS(LOWER(campaign),r'mg_') THEN 'Докаты'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_cpa') THEN 'Предельная цена ВКР'
    ELSE 'Other'
  END