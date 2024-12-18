-- procedures.social_format(campaign, date)

  CASE

    WHEN date <= '2022-12-31' THEN 
      CASE 
          WHEN REGEXP_CONTAINS(LOWER(campaign), r'_multi|_milti') THEN 'Мультиформат' 
          WHEN REGEXP_CONTAINS(LOWER(campaign), r'_nat') THEN 'Формат натив'
          WHEN REGEXP_CONTAINS(LOWER(campaign), r'_carusel|pf_m_ret_dnmc_action') THEN 'Карусель'
          WHEN REGEXP_CONTAINS(LOWER(campaign), r'_rs|_site|pf_m_dir_dnmc') THEN 'Реклама сайта'
          ELSE 'NaN'
      END

    WHEN date > '2022-12-31' THEN 
      CASE 
          WHEN REGEXP_CONTAINS(LOWER(campaign), r'carusel_|pf_m_ret_dnmc_action') THEN 'Карусель' 
          WHEN REGEXP_CONTAINS(LOWER(campaign), r'rs_|site_|pf_m_dir_dnmc') THEN 'Реклама сайта'
          WHEN REGEXP_CONTAINS(LOWER(campaign), r'multi_') THEN 'Мультиформат'
          WHEN REGEXP_CONTAINS(LOWER(campaign), r'nat_') THEN 'Натив'
          ELSE 'NaN'
      END

  END