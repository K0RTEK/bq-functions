### procedures.cont_fl_jira_num(campaign)

  CASE
    WHEN REGEXP_EXTRACT(LOWER(campaign),r'_([0-9]+)_.*\...-..\...\...') IS NOT NULL
      THEN REGEXP_EXTRACT(LOWER(campaign),r'_([0-9]+)_.*\...-..\...\...')
    WHEN REGEXP_EXTRACT(LOWER(campaign),r'_([0-9]+)_.*\...-.\...\...') IS NOT NULL
      THEN REGEXP_EXTRACT(LOWER(campaign),r'_([0-9]+)_.*\...-.\...\...')
    WHEN REGEXP_EXTRACT(LOWER(campaign),r'_([0-9]+)_.*-.*') IS NOT NULL
      THEN REGEXP_EXTRACT(LOWER(campaign),r'_([0-9]+)_.*-.*')
    ELSE 'NaN'
  END