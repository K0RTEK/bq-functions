CASE
  ### cook_social.get_additions(date,parameter)
    WHEN REGEXP_CONTAINS(LOWER(parameter),r'mg_|clprt|_rto_') THEN '-' 
    WHEN REGEXP_CONTAINS(LOWER(parameter),r'samolet_msk_traf_dinrem|cl-bus_msk_traf_dinrem') THEN '-' 
    ELSE 'Докаты'
  END