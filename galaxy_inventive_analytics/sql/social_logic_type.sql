-- procedures.social_logic_type(campaign, date)

CASE

  WHEN date <= '2022-12-31' THEN 'NaN'

  WHEN date > '2022-12-31' THEN 
    CASE 
      WHEN REGEXP_CONTAINS(LOWER(campaign), r'kw_') THEN 'ключи' 
      WHEN REGEXP_CONTAINS(LOWER(campaign), r'int_') THEN 'интересы'
      WHEN REGEXP_CONTAINS(LOWER(campaign), r'auto') THEN 'автоинтересы'
      WHEN REGEXP_CONTAINS(LOWER(campaign), r'dnmc_') THEN 'динрем'
      WHEN REGEXP_CONTAINS(LOWER(campaign), r'sttc_|stts_') THEN 'стат.ремаркетинг'
      ELSE 'NaN'
    END

END