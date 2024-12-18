### `cook_procedures.get_event_object`(date, [param1,param2]) as event_object
          /*
          Относится только к ОПРЕДЕЛЁННОМУ СОБЫТИЮ (соответствует напр. Объекту встречи или сделки) 
          Также источники уже ПОСЛЕ кабинета
          На случай коррекций - заложена дата (но лучше если можно обойтись без неё)
          */
          CASE
            -- Сначала описать точные вхождения (пример:"Объект по CRM") 
            -- Может содержать внутри исключения по тому же принципу
            WHEN EXISTS(SELECT * FROM UNNEST(parameters) AS x WHERE x in ('dummy','dummy'))
              THEN 'placeholder'
            -- Затем регулярки
            WHEN EXISTS(SELECT * FROM UNNEST(parameters) AS x WHERE REGEXP_CONTAINS(x, r'dummy'))
              THEN 'placeholder'
            -- Либо в налл
            -- ELSE CAST(NULL AS STRING)
            ELSE `cook_procedures.get_campaign_object`(date, parameters)
          END