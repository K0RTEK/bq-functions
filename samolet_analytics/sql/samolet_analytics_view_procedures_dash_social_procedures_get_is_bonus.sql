CASE
  ### dash_social.get_is_bonus(date,parameter)
    WHEN REGEXP_CONTAINS(LOWER(parameter),r'bonus') THEN 'bonus'
    ELSE '-'
  END