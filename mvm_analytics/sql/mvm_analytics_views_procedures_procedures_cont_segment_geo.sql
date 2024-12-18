### procedures.cont_segment_geo(campaign)

-- сегменты только для Эльдорадо, условия прописаны в задаче https://pf.mgcom.ru/task/1086081 

  CASE
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_mo$|_mo_') THEN 'МО'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_msk') THEN 'Москва'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_spb') THEN 'СПБ'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_novosibirsk') THEN 'Новосибирск'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_ekaterinburg') THEN 'Екатеринбург'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_nn') THEN 'Нижний Новгород'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_rostov') THEN 'Ростов'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_kazan') THEN 'Казань'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_krasnodar') THEN 'Краснодар'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_chelyabinsk') THEN 'Челябинск'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_spbo') THEN 'СПБо'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_samara') THEN 'Самара'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_krasnoyarsk') THEN 'Красноярск'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_irkutsk') THEN 'Иркутск'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_all-rf') THEN 'РФ'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'armavir') THEN 'Армавир'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'kamyshin') THEN 'Камышин'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'maykop') THEN 'Майкоп'

    ELSE 'NaN'
  END