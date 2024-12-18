### procedures.cont_category(campaign)

-- сегменты только для Эльдорадо, условия прописаны в задаче https://pf.mgcom.ru/task/1086081 

  CASE
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_tv_') THEN 'Телевизоры'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'smartphone') THEN 'Смартфоны'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'conditioners') THEN 'Кондиционеры'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'notebook') THEN 'Ноутбуки'

-- условия прописаны в задаче https://pf.mgcom.ru/task/1273599

    WHEN REGEXP_CONTAINS(LOWER(campaign),r'duhovie-shkafy|ovens') THEN 'Духовые шкафы'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'fridges|refrigerators|holodilniki') THEN 'Холодильники'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'obogrevateli') THEN 'Обогреватели'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'laptops|notebook') THEN 'Ноутбуки'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'planshety|tablets') THEN 'Планшеты'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'game-console') THEN 'Игровые консоли'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'dyson') THEN 'Дайсон'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'kitchen|cookers|cooktops') THEN 'Панели и плиты'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'pylesosy') THEN 'Пылесосы'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'sushilnye-mashiny|_dm_') THEN 'Сушильные машины'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'coffee') THEN 'Кофемашины'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'vytyazhki') THEN 'Вытяжки'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'posudomoechnye-mashiny|_dw_') THEN 'Посудомоечные машины'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_smart-chasy_') THEN 'Умные часы'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'vstroyka') THEN 'Встройка'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'stiralnie-mashiny|stiralnye-mashiny') THEN 'Стиральные машины'

    ELSE 'NaN'
  END