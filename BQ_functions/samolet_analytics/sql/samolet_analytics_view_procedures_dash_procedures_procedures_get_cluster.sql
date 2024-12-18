### dash_procedures.get_cluster(date,parameter,res_type)
  CASE
		WHEN REGEXP_CONTAINS(LOWER(parameter),r'cl-nmsk_|новая москва')
			THEN CASE
				WHEN res_type = 'short_name' THEN 'Кластер - НМ'
				ELSE 'Кластер - Новая Москва'
			END
		WHEN REGEXP_CONTAINS(LOWER(parameter),r'cl-yug_|кластер - юг')
			THEN 'Кластер - Юг'
		WHEN REGEXP_CONTAINS(LOWER(parameter),r'cl-sever_|кластер - север')
			THEN 'Кластер - Север'
		WHEN REGEXP_CONTAINS(LOWER(parameter),r'cl-zapad_|кластер - запад')
			THEN 'Кластер - Запад'
		WHEN REGEXP_CONTAINS(LOWER(parameter),r'cl-vostok_|кластер - восток')
			THEN 'Кластер - Восток'
		WHEN REGEXP_CONTAINS(LOWER(parameter),r'cl-bus_|бизнес-класс')
			THEN CASE
				WHEN res_type = 'short_name' THEN 'Кластер - БК'
				ELSE 'Кластер - Бизнес-класс'
			END
		ELSE '-'
  END