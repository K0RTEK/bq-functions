-- procedures.get_geo(channel, campaign, date)
  CASE

  -- Контекстная реклама
    WHEN channel = 'Контекст' THEN 
      CASE 
          WHEN REGEXP_CONTAINS(LOWER(campaign), r'_rf|perfomance') THEN 'РФ'
          ELSE 'NaN'
      END   
  END