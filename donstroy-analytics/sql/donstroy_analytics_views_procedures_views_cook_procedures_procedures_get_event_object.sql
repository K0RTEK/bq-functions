### `cook_procedures.get_event_object`(date, [param1,param2]) as event_object
  /*
  Относится только к ОПРЕДЕЛЁННОМУ СОБЫТИЮ (соответствует напр. Объекту встречи или сделки) 
  Источники уже ПОСЛЕ кабинета
  На случай коррекций - заложена дата (если можно обойтись без неё)
  */
  CASE
    -- Сначала описать точные вхождения (пример:"Объект по CRM") 
    -- Может содержать внутри исключения по тому же принципу
    -- WHEN EXISTS(SELECT * FROM UNNEST(parameters) AS x WHERE LOWER(TRIM(x)) in ('dummy','dummy'))
    --   THEN 'placeholder'
    -- Затем регулярки
    WHEN EXISTS(SELECT * FROM UNNEST(parameters) AS x WHERE REGEXP_CONTAINS(LOWER(TRIM(x)), r'^событие'))
      THEN 'Событие'
    WHEN EXISTS(SELECT * FROM UNNEST(parameters) AS x WHERE REGEXP_CONTAINS(LOWER(TRIM(x)), r'^символ'))
      THEN 'Символ'
    WHEN EXISTS(SELECT * FROM UNNEST(parameters) AS x WHERE REGEXP_CONTAINS(LOWER(TRIM(x)), r'^региональн'))
      THEN 'РЕГИОНАЛЬНАЯ КАМПАНИЯ'
    WHEN EXISTS(SELECT * FROM UNNEST(parameters) AS x WHERE REGEXP_CONTAINS(LOWER(TRIM(x)), r'^коммерческа'))
      THEN 'КОММЕРЧЕСКАЯ НЕДВИЖИМОСТЬ'
    WHEN EXISTS(SELECT * FROM UNNEST(parameters) AS x WHERE REGEXP_CONTAINS(LOWER(TRIM(x)), r'^donstroy'))
      THEN 'donstroy.com'
    -- Либо в налл
    -- ELSE CAST(NULL AS STRING)
    ELSE `cook_procedures.get_campaign_object`(date, parameters) -- ??? 
  END