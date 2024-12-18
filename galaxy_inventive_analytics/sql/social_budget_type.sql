-- procedures.social_budget_type(campaign, date)

CASE

  WHEN date <= '2022-12-31' THEN
    CASE 
      WHEN REGEXP_CONTAINS(LOWER(campaign), r'_m_') THEN 'основной' 
      ELSE 'NaN'
    END

  WHEN date > '2022-12-31' THEN 
    CASE 
      WHEN REGEXP_CONTAINS(LOWER(campaign), r'_m_') THEN 'основной' 
      WHEN REGEXP_CONTAINS(LOWER(campaign), r'_f_') THEN 'флайт'
      ELSE 'NaN'
    END

END