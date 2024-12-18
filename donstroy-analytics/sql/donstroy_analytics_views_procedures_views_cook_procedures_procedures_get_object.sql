-- cook_procedures.get_object(parameter)
  CASE
    WHEN REGEXP_CONTAINS(LOWER(TRIM(parameter)),r'don-sobytie-mg') THEN 'Событие'
    WHEN REGEXP_CONTAINS(LOWER(TRIM(parameter)),r'don-simvol-mg') THEN 'Символ'
    WHEN REGEXP_CONTAINS(LOWER(TRIM(parameter)),r'don-regiony') THEN 'РЕГИОНАЛЬНАЯ КАМПАНИЯ'
    WHEN REGEXP_CONTAINS(LOWER(TRIM(parameter)),r'don-kommercia-mg') THEN 'КОММЕРЧЕСКАЯ НЕДВИЖИМОСТЬ'
    WHEN REGEXP_CONTAINS(LOWER(TRIM(parameter)),r'don-brand-mg') THEN 'donstroy.com'

    WHEN REGEXP_CONTAINS(LOWER(TRIM(parameter)),r'событие|sobytie|sob-') THEN 'Событие'
    WHEN REGEXP_CONTAINS(LOWER(TRIM(parameter)),r'символ|simvol|sim-') THEN 'Символ'
    WHEN REGEXP_CONTAINS(LOWER(TRIM(parameter)),r'don-regiony|региональн') THEN 'РЕГИОНАЛЬНАЯ КАМПАНИЯ'
    WHEN REGEXP_CONTAINS(LOWER(TRIM(parameter)),r'don-kommercia-mg|коммерческа') THEN 'КОММЕРЧЕСКАЯ НЕДВИЖИМОСТЬ'
    WHEN REGEXP_CONTAINS(LOWER(TRIM(parameter)),r'don-brand-mg|donstroy') THEN 'donstroy.com'
    ELSE 'Другой'
  END