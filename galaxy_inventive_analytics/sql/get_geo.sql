-- procedures.get_geo(channel, campaign, date)
  CASE

  -- Контекстная реклама
    WHEN channel = 'Контекст' THEN 
      CASE 
          WHEN REGEXP_CONTAINS(LOWER(campaign), r'msk') THEN 'Москва и МО' 
          WHEN REGEXP_CONTAINS(LOWER(campaign), r'spb') THEN 'Санкт-Петербург и ЛО'
          WHEN REGEXP_CONTAINS(LOWER(campaign), r'highcr') THEN 'Highcr'
          WHEN REGEXP_CONTAINS(LOWER(campaign), r'lowcr') THEN 'Lowcr'
          WHEN REGEXP_CONTAINS(LOWER(campaign), r'vpn') THEN 'ВПН'
          WHEN REGEXP_CONTAINS(LOWER(campaign), r'rf') THEN 'РФ'
          WHEN REGEXP_CONTAINS(LOWER(campaign), r'regions|ekb|smr|ufa') THEN 'Регионы'
          ELSE 'NaN'
      END   

  -- Соцсети
    WHEN channel = 'Соцсети' THEN 

      CASE 
        WHEN date <= '2022-12-31' THEN 
          CASE 
              WHEN REGEXP_CONTAINS(LOWER(campaign), r'_msk') THEN 'Москва и МО' 
              WHEN REGEXP_CONTAINS(LOWER(campaign), r'rf||pf_m_ret_dnmc_action') THEN 'РФ'
              WHEN REGEXP_CONTAINS(LOWER(campaign), r'_reg') THEN 'Регионы'
              ELSE 'NaN'
          END

        WHEN date > '2022-12-31' THEN 
          CASE 
              WHEN REGEXP_CONTAINS(LOWER(campaign), r'_msk-spb') THEN 'Москва и СПб' 
              WHEN REGEXP_CONTAINS(LOWER(campaign), r'_msk') THEN 'Москва и МО'
              WHEN REGEXP_CONTAINS(LOWER(campaign), r'_spb') THEN 'Санкт-Петербург и ЛО'
              WHEN REGEXP_CONTAINS(LOWER(campaign), r'_allrf|_rf|pf_m_ret_dnmc_action') THEN 'Вся РФ'
              WHEN REGEXP_CONTAINS(LOWER(campaign), r'_reg') THEN 'Регионы'
              ELSE 'NaN'
          END

    END
  END