### procedures.cont_fl_period(campaign)

  CASE
    WHEN REGEXP_EXTRACT(LOWER(campaign),r'(..\...-..\...\...)') IS NOT NULL
      THEN REGEXP_EXTRACT(LOWER(campaign),r'(..\...-..\...\...)')
    WHEN REGEXP_EXTRACT(LOWER(campaign),r'(..\...\.....-..\...\.....)') IS NOT NULL
      THEN REGEXP_EXTRACT(LOWER(campaign),r'(..\...\.....-..\...\.....)')
    WHEN REGEXP_EXTRACT(LOWER(campaign),r'(..\...-..\...)') IS NOT NULL
      THEN REGEXP_EXTRACT(LOWER(campaign),r'(..\...-..\...)')
    WHEN REGEXP_EXTRACT(LOWER(campaign),r'(..\...-.\...\...)') IS NOT NULL
      THEN REGEXP_EXTRACT(LOWER(campaign),r'(..\...-.\...\...)')
    ELSE 'NaN'
  END