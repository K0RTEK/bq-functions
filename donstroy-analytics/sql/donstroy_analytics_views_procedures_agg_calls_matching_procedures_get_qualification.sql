-- agg_calls_matching.get_qualification(crm_stage, date)
  
  IF(
    REGEXP_CONTAINS(LOWER(TRIM(crm_stage)),r'перевод в продажу|новый|продажа завершена неуспешно'),
    'Квалифицированный',
    'Неквалифицированный')