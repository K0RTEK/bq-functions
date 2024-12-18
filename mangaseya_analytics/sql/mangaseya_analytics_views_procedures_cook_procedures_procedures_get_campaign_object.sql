### `cook_procedures.get_campaign_object`(date, [param1,param2]) as campaign_object
          /*
          Относится только к источнику, недопустимо использовать к "объекту интереса" или подобным полям
          Может относиться к CRM/Колтрекеру для определения статики 
          например CPA не имеют кабинета, указанием на источник служит кампания колтрекера
          На случай коррекций - заложена дата (но лучше если можно обойтись без неё)
          ИСКЛЮЧИТЕЛЬНО информация из кабинета
          */
          CASE
            -- Сначала описать точные вхождения(примеры:кабинет, суффикс) 
            -- Может содержать внутри исключения по тому же принципу
            WHEN EXISTS(SELECT * FROM UNNEST(parameters) AS x WHERE LOWER(TRIM(x)) in ('63803','96021540','mangazeya-na-rechnom-mg','rechnoi'))
              THEN 'Мангазея на Речном'
            -- Затем регулярки
            WHEN EXISTS(SELECT * FROM UNNEST(parameters) AS x WHERE REGEXP_CONTAINS(TRIM(LOWER(x)), r'на.речном|na.rechnom'))
              THEN 'Мангазея на Речном'
            ELSE CAST(NULL AS STRING)
          END