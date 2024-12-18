### procedures.cont_geo(campaign)
  CASE
    WHEN NOT REGEXP_CONTAINS(LOWER(campaign),r'mg_') THEN 'Докаты'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_msk') THEN 'МСК + МО'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_spb') THEN 'СПБ + ЛО'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_cfo') THEN 'Центральный ФО (без МСК и МО)'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_szfo') THEN 'Северо-Западный ФО (без СПБ и ЛО)'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_yufo') THEN 'Южный ФО'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_dvfo') THEN 'Дальневосточный ФО'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_sfo') THEN 'Сибирский ФО'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_urfo') THEN 'Уральский ФО'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_pfo') THEN 'Приволжский ФО'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_skfo') THEN 'Северо-Кавказский ФО'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_all-rf|_rf|joint.*_all') THEN 'Россия(Кроме крыма)'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_top-regions') THEN 'Регионы сильные'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_low-regions') THEN 'Регионы слабые'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_region') THEN 'Регионы'

    WHEN REGEXP_CONTAINS(LOWER(campaign),r'ekat|_nn|novos|samara|_ufa|nizhnij novgorod|kazan|chelyab|belgorod|izhevsk|krasnodar|kursk|perm|tula|volgograd|yaroslavl|barnaul|irkutsk|khabarovsk|krasnoyarsk|murmansk|omsk|ryazan|saratov|sochi|stavropol|tyumen|vladivostok|voronezh') THEN 'Регионы сильные'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'rnd|chelny|ivanovo|kaluga|lipetsk|rostov|smolensk|vladimir') THEN 'Регионы слабые'

    ELSE CONCAT('NaN - ',campaign)
  END