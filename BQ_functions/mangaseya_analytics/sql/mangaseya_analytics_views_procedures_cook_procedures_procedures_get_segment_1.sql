CASE
  WHEN REGEXP_CONTAINS(LOWER(TRIM(parameter)),'(_|^)mkb(_|$)')
    THEN 'МКБ'
  WHEN REGEXP_CONTAINS(LOWER(TRIM(parameter)),'(_|^)srch(_|$)')
    THEN 'Поиск'
  WHEN REGEXP_CONTAINS(LOWER(TRIM(parameter)),'(_|^)net(_|$)')
    THEN 'РСЯ'
  WHEN REGEXP_CONTAINS(LOWER(TRIM(parameter)),'(_|^)mc-direct(_|$)')
    THEN 'МК'
END