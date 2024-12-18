### procedures.cont_search_network(campaign)
  CASE
      -- Вита добавила 21.11
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_tk_|_epk_|_united_') THEN 'Поиск+Сеть'

    WHEN NOT REGEXP_CONTAINS(LOWER(campaign),r'mg_') THEN 'Докаты'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_p_|search|_dsa|yandex_shopping|yandexmarket') THEN 'Поиск'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_s_|rsya') THEN 'Сеть'

    ELSE CONCAT('NaN - ',campaign)
  END