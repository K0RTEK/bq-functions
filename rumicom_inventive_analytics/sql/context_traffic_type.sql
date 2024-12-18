-- procedures.context_traffic_type(campaign)

  CASE 
    WHEN REGEXP_CONTAINS(LOWER(campaign), r'_p_') THEN 'Поиск' 
    WHEN REGEXP_CONTAINS(LOWER(campaign), r'_s_') THEN 'Сеть'
    WHEN REGEXP_CONTAINS(LOWER(campaign), r'tov|perfomance') THEN 'Товарная/ ЕПК'
    ELSE 'NaN'
  END