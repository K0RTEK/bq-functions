-- procedures.social_age(campaign, date)
CASE

  WHEN date <= '2022-12-31' THEN 'NaN'

  WHEN date > '2022-12-31' THEN 
    CASE 
      WHEN REGEXP_CONTAINS(LOWER(campaign), r'18_|pf_m_dir_dnmc|pf_m_ret_dnmc_action') THEN '18' 
      WHEN REGEXP_CONTAINS(LOWER(campaign), r'18-55_') THEN '18-55'
      WHEN REGEXP_CONTAINS(LOWER(campaign), r'18-50_') THEN '18-50'
      WHEN REGEXP_CONTAINS(LOWER(campaign), r'23-55_') THEN '23-55'
      ELSE 'NaN'
    END

END