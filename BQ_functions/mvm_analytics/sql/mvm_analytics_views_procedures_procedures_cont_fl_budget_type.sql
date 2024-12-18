### procedures.cont_fl_budget_type(campaign)
  CASE
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_kd_') THEN 'Вендорский'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_fed_') THEN 'МВМ'
    ELSE CONCAT('NaN - ', campaign)
  END