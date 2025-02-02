### dash_procedures.get_object_cluster(date,parameter,res_type)
		### Москва
  CASE
  	WHEN dash_procedures.get_objects(date,parameter,'crm_direction') = 'Москва' 
      THEN CASE
        WHEN dash_procedures.get_objects(date,parameter,'object') = 'ПРИГОРОД'
          THEN 'Кластер - Юг'
        WHEN dash_procedures.get_objects(date,parameter,'object') = 'АЛХИМОВО'
          THEN 'Кластер - Новая Москва'
        WHEN dash_procedures.get_objects(date,parameter,'object') = 'Квартал Авиаторов'
          THEN 'Кластер - Восток'
        WHEN dash_procedures.get_objects(date,parameter,'object') = 'Богдановский Лес'
          THEN 'Кластер - Юг'
        WHEN dash_procedures.get_objects(date,parameter,'object') = 'Цветочные Поляны'
          THEN 'Кластер - Новая Москва'
        WHEN dash_procedures.get_objects(date,parameter,'object') = 'Долина Яузы'
          THEN 'Кластер - Восток'
        WHEN dash_procedures.get_objects(date,parameter,'object') = 'Квартал Домашний'
          THEN 'Кластер - Юг'
        WHEN dash_procedures.get_objects(date,parameter,'object') = 'Егорово Парк'
          THEN 'Кластер - Восток'
        WHEN dash_procedures.get_objects(date,parameter,'object') = 'Эко Бунино'
          THEN 'Кластер - Новая Москва'
        WHEN dash_procedures.get_objects(date,parameter,'object') = 'Квартал Герцена'
          THEN 'Кластер - Юг'
        WHEN dash_procedures.get_objects(date,parameter,'object') = 'Горки Парк'
          THEN 'Кластер - Юг'
        WHEN dash_procedures.get_objects(date,parameter,'object') = 'ИВАКИНО'
          THEN 'Кластер - Север'
        WHEN dash_procedures.get_objects(date,parameter,'object') = 'Квартал Марьино'
          THEN 'Кластер - Новая Москва'
        WHEN dash_procedures.get_objects(date,parameter,'object') = 'Квартал на воде'
          THEN 'Кластер - Бизнес-класс'
        WHEN dash_procedures.get_objects(date,parameter,'object') = 'Квартал Западный'
          THEN 'Кластер - Новая Москва'
        WHEN dash_procedures.get_objects(date,parameter,'object') = 'ЛЮБЕРЦЫ'
          THEN 'Кластер - Восток'
        WHEN dash_procedures.get_objects(date,parameter,'object') = 'МОЛЖАНИНОВО'
          THEN 'Кластер - Север'
        WHEN dash_procedures.get_objects(date,parameter,'object') = 'Мытищи Парк'
          THEN 'Кластер - Восток'
        WHEN dash_procedures.get_objects(date,parameter,'object') = 'НОВОЕ ВНУКОВО'
          THEN 'Кластер - Новая Москва'
        WHEN dash_procedures.get_objects(date,parameter,'object') = 'Nova Select'
          THEN '-'
        WHEN dash_procedures.get_objects(date,parameter,'object') = 'НОВОДАНИЛОВСКАЯ'
          THEN 'Кластер - Бизнес-класс'
        WHEN dash_procedures.get_objects(date,parameter,'object') = 'Новоград Павлино'
          THEN 'Кластер - Восток'
        WHEN dash_procedures.get_objects(date,parameter,'object') = 'Ольховый Квартал'
          THEN 'Кластер - Новая Москва'
        WHEN dash_procedures.get_objects(date,parameter,'object') = 'Октябрьская 98'
          THEN 'Кластер - Бизнес-класс'
        WHEN dash_procedures.get_objects(date,parameter,'object') = 'ОСТАФЬЕВО'
          THEN 'Кластер - Новая Москва'
        WHEN dash_procedures.get_objects(date,parameter,'object') = 'Подольские Кварталы'
          THEN 'Кластер - Новая Москва'
        WHEN dash_procedures.get_objects(date,parameter,'object') = 'Прибрежный Парк'
          THEN 'Кластер - Юг'
        WHEN dash_procedures.get_objects(date,parameter,'object') = 'ПРИГОРОД'
          THEN 'Кластер - Юг'
        WHEN dash_procedures.get_objects(date,parameter,'object') = 'ПУТИЛКОВО'
          THEN 'Кластер - Север'
        WHEN dash_procedures.get_objects(date,parameter,'object') = 'Пятницкие Луга'
          THEN 'Кластер - Север'
        WHEN dash_procedures.get_objects(date,parameter,'object') = 'Пятницкое 58'
          THEN 'Кластер - Север'
        WHEN dash_procedures.get_objects(date,parameter,'object') = 'Рублевский квартал'
          THEN 'Кластер - Запад'
        WHEN dash_procedures.get_objects(date,parameter,'object') = 'Квартал Румянцево'
          THEN 'Кластер - Новая Москва'
        WHEN dash_procedures.get_objects(date,parameter,'object') = 'СПУТНИК'
          THEN 'Кластер - Запад'
        WHEN dash_procedures.get_objects(date,parameter,'object') = 'Стремянный 2'
          THEN 'Кластер - Бизнес-класс'
        WHEN dash_procedures.get_objects(date,parameter,'object') = 'Квартал Строгино'
          THEN 'Кластер - Запад'
        WHEN dash_procedures.get_objects(date,parameter,'object') = 'ТОМИЛИНО'
          THEN 'Кластер - Восток'
        WHEN dash_procedures.get_objects(date,parameter,'object') = 'Тропарево Парк'
          THEN 'Кластер - Бизнес-класс'
        WHEN dash_procedures.get_objects(date,parameter,'object') = 'Вереск'
          THEN 'Кластер - Бизнес-класс'
        WHEN dash_procedures.get_objects(date,parameter,'object') = 'Новое Видное'
          THEN 'Кластер - Юг'
        WHEN dash_procedures.get_objects(date,parameter,'object') = 'Заречье Парк'
          THEN 'Кластер - Бизнес-класс'
        WHEN dash_procedures.get_objects(date,parameter,'object') = 'ВЕРЕЙСКАЯ'
          THEN 'Кластер - Бизнес-класс'
        WHEN dash_procedures.get_objects(date,parameter,'object') = 'Некрасовка'
          THEN 'Кластер - Бизнес-класс'		
        WHEN dash_procedures.get_objects(date,parameter,'object') = 'Мята'
          THEN 'Кластер - Бизнес-класс'			
        WHEN dash_procedures.get_objects(date,parameter,'object') = 'Кленовые Аллеи'
          THEN 'Кластер - Новая Москва'	
        WHEN dash_procedures.get_objects(date,parameter,'object') = 'Восточный котел'
          THEN 'Кластер - Восток'
        WHEN dash_procedures.get_objects(date,parameter,'object') = 'Квартал Ольховый'
          THEN 'Кластер - Новая Москва'
        WHEN dash_procedures.get_objects(date,parameter,'object') = 'Кластер - Новая Москва'
          THEN 'Кластер - Новая Москва'
        WHEN dash_procedures.get_objects(date,parameter,'object') = 'Кластер - Юг'
          THEN 'Кластер - Юг'
        WHEN dash_procedures.get_objects(date,parameter,'object') = 'Кластер - Север'
          THEN 'Кластер - Север'
        WHEN dash_procedures.get_objects(date,parameter,'object') = 'Кластер - Запад'
          THEN 'Кластер - Запад'
        WHEN dash_procedures.get_objects(date,parameter,'object') = 'Кластер - Восток'
          THEN 'Кластер - Восток'
        WHEN dash_procedures.get_objects(date,parameter,'object') = 'Кластер - Бизнес-класс'
          THEN 'Кластер - Бизнес-класс'
          
		    ELSE '-'
      END
      
		ELSE '-'
  END