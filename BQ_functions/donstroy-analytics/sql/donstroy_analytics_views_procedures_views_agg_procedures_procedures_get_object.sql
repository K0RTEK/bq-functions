-- agg_procedures.get_object(parameter)
  CASE
    WHEN REGEXP_CONTAINS(LOWER(TRIM(parameter)),r'событие|sobytie|sob-') THEN 'Событие'
    WHEN REGEXP_CONTAINS(LOWER(TRIM(parameter)),r'символ|simvol|sim-') THEN 'Символ'
    WHEN REGEXP_CONTAINS(LOWER(TRIM(parameter)),r'don-brand-mg') THEN 'donstroy.com'
    WHEN REGEXP_CONTAINS(LOWER(TRIM(parameter)),r'don-regiony') THEN 'РЕГИОНАЛЬНАЯ КАМПАНИЯ'
    WHEN REGEXP_CONTAINS(LOWER(TRIM(parameter)),r'don-kommercia-mg') THEN 'КОММЕРЧЕСКАЯ НЕДВИЖИМОСТЬ'
    ELSE 'Другой'
  END