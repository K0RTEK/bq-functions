-- procedures.social_perform_type(campaign, date)

CASE

  WHEN date <= '2022-12-31' THEN 'NaN'

  WHEN date > '2022-12-31' THEN 
    CASE 
      WHEN REGEXP_CONTAINS(LOWER(campaign), r'pf_') THEN 'Перформ' 
      WHEN REGEXP_CONTAINS(LOWER(campaign), r'md_') THEN 'Медийка'
      ELSE 'NaN'
    END

END