-- procedures.context_traffic_type(campaign)

  CASE 
    WHEN REGEXP_CONTAINS(LOWER(campaign), r'_p_|search') THEN 'Поиск' 
    WHEN REGEXP_CONTAINS(LOWER(campaign), r'_s_') THEN 'Сеть'
    WHEN REGEXP_CONTAINS(LOWER(campaign), r'tovarnaya|epk_') THEN 'Товарная/ЕПК' 
    ELSE 'NaN'
  END