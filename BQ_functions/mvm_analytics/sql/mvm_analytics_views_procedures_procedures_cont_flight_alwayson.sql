### procedures.cont_flight_alwayson(campaign)
  CASE
    WHEN NOT REGEXP_CONTAINS(LOWER(campaign),r'mg_') THEN 'Докаты'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'flight') AND REGEXP_CONTAINS(LOWER(campaign),r'_fed_') THEN 'Flight Фед. бюджет'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'flight') AND NOT REGEXP_CONTAINS(LOWER(campaign),r'_fed_') THEN 'Flight Венд. бюджет'
    ELSE 'AlwaysOn'
  END