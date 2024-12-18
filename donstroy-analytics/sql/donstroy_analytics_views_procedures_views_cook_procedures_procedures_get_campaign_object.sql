### `cook_procedures.get_campaign_object`(date, [param1,param2]) as campaign_object
  /*
  Относится только к источнику, недопустимо использовать к "объекту интереса" или подобным полям
  Может относиться к CRM/Колтрекеру для определения статики 
  например CPA не имеют кабинета, указанием на источник служит кампания колтрекера
  На случай коррекций - заложена дата (если можно обойтись без неё)
  ИСКЛЮЧИТЕЛЬНО информация из кабинетов / характеризующие источник
  */
  CASE
    -- Сначала описать точные вхождения(примеры:кабинет, суффикс) 
    -- Может содержать внутри исключения по тому же принципу
    WHEN EXISTS(SELECT * FROM UNNEST(parameters) AS x WHERE LOWER(TRIM(x)) in ('don-sobytie-mg'))
      THEN 'Событие'
    WHEN EXISTS(SELECT * FROM UNNEST(parameters) AS x WHERE LOWER(TRIM(x)) in ('don-simvol-mg'))
      THEN 'Символ'
    WHEN EXISTS(SELECT * FROM UNNEST(parameters) AS x WHERE LOWER(TRIM(x)) in ('don-regiony'))
      THEN 'РЕГИОНАЛЬНАЯ КАМПАНИЯ'
    WHEN EXISTS(SELECT * FROM UNNEST(parameters) AS x WHERE LOWER(TRIM(x)) in ('don-kommercia-mg'))
      THEN 'КОММЕРЧЕСКАЯ НЕДВИЖИМОСТЬ'
    WHEN EXISTS(SELECT * FROM UNNEST(parameters) AS x WHERE LOWER(TRIM(x)) in ('don-brand-mg'))
      THEN 'donstroy.com'

    -- Затем регулярки
    WHEN EXISTS(SELECT * FROM UNNEST(parameters) AS x WHERE REGEXP_CONTAINS(LOWER(TRIM(x)), r'^sobytie|^sob'))
      THEN 'Событие'
    WHEN EXISTS(SELECT * FROM UNNEST(parameters) AS x WHERE REGEXP_CONTAINS(LOWER(TRIM(x)), r'^simvol|^sim'))
      THEN 'Символ'
    WHEN EXISTS(SELECT * FROM UNNEST(parameters) AS x WHERE REGEXP_CONTAINS(LOWER(TRIM(x)), r'^donstroy'))
      THEN 'donstroy.com | КОММЕРЧЕСКАЯ НЕДВИЖИМОСТЬ | РЕГИОНАЛЬНАЯ КАМПАНИЯ'
    ELSE CAST(NULL AS STRING)
  END