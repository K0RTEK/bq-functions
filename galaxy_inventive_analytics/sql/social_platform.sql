-- procedures.social_platform(campaign, date)

CASE

  WHEN date <= '2022-12-31' THEN 'NaN'

  WHEN date > '2022-12-31' THEN 
    CASE 
      WHEN REGEXP_CONTAINS(LOWER(campaign), r'cross_|pf_m_dir_dnmc|pf_m_ret_dnmc_action') THEN 'Все устройства' 
      WHEN REGEXP_CONTAINS(LOWER(campaign), r'mob_') THEN 'Мобилка'
      WHEN REGEXP_CONTAINS(LOWER(campaign), r'web_') THEN 'Веб'
      ELSE 'NaN'
    END

END