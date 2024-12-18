CASE
  WHEN REGEXP_CONTAINS(LOWER(TRIM(parameter)),'(_|^)brand(_|$)')
    THEN 'Бренд'
  WHEN REGEXP_CONTAINS(LOWER(TRIM(parameter)),'(_|^)geo(_|$)')
    THEN 'Гео'
  WHEN REGEXP_CONTAINS(LOWER(TRIM(parameter)),'(_|^)compet(_|$)')
    THEN 'Конкуренты'
  WHEN REGEXP_CONTAINS(LOWER(TRIM(parameter)),'(_|^)generic(_|$)')
    THEN 'Общие'
  WHEN REGEXP_CONTAINS(LOWER(TRIM(parameter)),'(_|^)lal(_|$)')
    THEN 'LAL'
  WHEN REGEXP_CONTAINS(LOWER(TRIM(parameter)),'(_|^)polygon(_|$)|(_|^)audiences(_|$)')
    THEN 'Аудитории'
  WHEN REGEXP_CONTAINS(LOWER(TRIM(parameter)),'(_|^)remarketing(_|$)')
    THEN 'Ретаргетинг'
END