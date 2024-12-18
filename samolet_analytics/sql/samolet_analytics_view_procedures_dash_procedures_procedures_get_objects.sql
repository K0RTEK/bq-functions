### dash_procedures.get_objects(date,parameter,res_type)
		### Москва
  CASE
  	WHEN REGEXP_CONTAINS(LOWER(parameter),r'mg_vka_soc_samolet_msk_lead_lead-b|mg_vka_soc_samolet_msk_lead_ret-b|mg_vka_soc_samolet_msk_traf_click-b')
			THEN CASE
				WHEN res_type = 'object' THEN 'Кэшбэк'
				WHEN res_type = 'crm_direction' THEN 'Москва'
				ELSE 'Москва'
			END
  	WHEN REGEXP_CONTAINS(LOWER(parameter),r'commercial.auc')
			THEN CASE
				WHEN res_type = 'object' THEN 'Аукцион'
				WHEN res_type = 'crm_direction' THEN 'Москва'
				ELSE 'Москва'
			END
  	WHEN REGEXP_CONTAINS(LOWER(parameter),r'l2c_')
			THEN CASE
				WHEN res_type = 'object' THEN 'Lead2Call'
				WHEN res_type = 'crm_direction' THEN 'Москва'
				ELSE 'Москва'
			END
  	WHEN REGEXP_CONTAINS(LOWER(parameter),r'жк0') AND (REGEXP_CONTAINS(LOWER(parameter),r'msk|mmo') OR NOT REGEXP_CONTAINS(LOWER(parameter),r'istra|spb|tmn|vldv'))
			THEN CASE
				WHEN res_type = 'object' THEN 'ПРИГОРОД'
				WHEN res_type = 'crm_direction' THEN 'Москва'
				ELSE 'Москва'
			END
  	WHEN REGEXP_CONTAINS(LOWER(parameter),r'behappy|формула счастья')
			THEN CASE
				WHEN res_type = 'object' THEN 'Формула счастья'
				WHEN res_type = 'crm_direction' THEN 'Флайт'
				ELSE 'Москва'
			END
    WHEN REGEXP_CONTAINS(LOWER(parameter),r'alhimovo|алхимово')
			THEN CASE
				WHEN res_type = 'object' THEN 'АЛХИМОВО'
				WHEN res_type = 'crm_direction' THEN 'Москва'
				ELSE 'Москва'
			END
  	WHEN REGEXP_CONTAINS(LOWER(parameter),r'aviatorov|квартал авиаторов')
			THEN CASE
				WHEN res_type = 'object' THEN 'Квартал Авиаторов'
				WHEN res_type = 'crm_direction' THEN 'Москва'
				ELSE 'Москва'
			END
    WHEN REGEXP_CONTAINS(LOWER(parameter),r'bogdanovsk|богдановский лес')
			THEN CASE
				WHEN res_type = 'object' THEN 'Богдановский Лес'
				WHEN res_type = 'crm_direction' THEN 'Москва'
				ELSE 'Москва'
			END
  	WHEN REGEXP_CONTAINS(LOWER(parameter),r'cvet poliany|tsvetochnye-poljany|цветочные поляны')
			THEN CASE
				WHEN res_type = 'object' THEN 'Цветочные Поляны'
				WHEN res_type = 'crm_direction' THEN 'Москва'
				ELSE 'Москва'
			END
  	WHEN REGEXP_CONTAINS(LOWER(parameter),r'dolina.yauz|долина яузы')
			THEN CASE
				WHEN res_type = 'object' THEN 'Долина Яузы'
				WHEN res_type = 'crm_direction' THEN 'Москва'
				ELSE 'Москва'
			END
  	WHEN REGEXP_CONTAINS(LOWER(parameter),r'domashni|квартал домашний')
			THEN CASE
				WHEN res_type = 'object' THEN 'Квартал Домашний'
				WHEN res_type = 'crm_direction' THEN 'Москва'
				ELSE 'Москва'
			END
    WHEN REGEXP_CONTAINS(LOWER(parameter),r'egorovo|егорово парк')
			THEN CASE
				WHEN res_type = 'object' THEN 'Егорово Парк'
				WHEN res_type = 'crm_direction' THEN 'Москва'
				ELSE 'Москва'
			END
  	WHEN REGEXP_CONTAINS(LOWER(parameter),r'eko.bunino|эко бунино')
			THEN CASE
				WHEN res_type = 'object' THEN 'Эко Бунино'
				WHEN res_type = 'crm_direction' THEN 'Москва'
				ELSE 'Москва'
			END
  	WHEN REGEXP_CONTAINS(LOWER(parameter),r'gercena|kvartal-gertzena|квартал герцена')
			THEN CASE
				WHEN res_type = 'object' THEN 'Квартал Герцена'
				WHEN res_type = 'crm_direction' THEN 'Москва'
				ELSE 'Москва'
			END
  	WHEN REGEXP_CONTAINS(LOWER(parameter),r'gorki.park|горки парк')
			THEN CASE
				WHEN res_type = 'object' THEN 'Горки Парк'
				WHEN res_type = 'crm_direction' THEN 'Москва'
				ELSE 'Москва'
			END
  	WHEN REGEXP_CONTAINS(LOWER(parameter),r'ivakino|ивакино')
			THEN CASE
				WHEN res_type = 'object' THEN 'ИВАКИНО'
				WHEN res_type = 'crm_direction' THEN 'Москва'
				ELSE 'Москва'
			END
  	WHEN REGEXP_CONTAINS(LOWER(parameter),r'kvartal.maryino|квартал марьино')
			THEN CASE
				WHEN res_type = 'object' THEN 'Квартал Марьино'
				WHEN res_type = 'crm_direction' THEN 'Москва'
				ELSE 'Москва'
			END
  	WHEN REGEXP_CONTAINS(LOWER(parameter),r'kvartal.na.vode|квартал на воде')
			THEN CASE
				WHEN res_type = 'object' THEN 'Квартал на воде'
				WHEN res_type = 'crm_direction' THEN 'Москва'
				ELSE 'Москва'
			END
  	WHEN REGEXP_CONTAINS(LOWER(parameter),r'kvartal.zapadn|квартал западный')
			THEN CASE
				WHEN res_type = 'object' THEN 'Квартал Западный'
				WHEN res_type = 'crm_direction' THEN 'Москва'
				ELSE 'Москва'
			END
    WHEN REGEXP_CONTAINS(LOWER(parameter),r'lubercy|люберцы')
			THEN CASE
				WHEN res_type = 'object' THEN 'ЛЮБЕРЦЫ'
				WHEN res_type = 'crm_direction' THEN 'Москва'
				ELSE 'Москва'
			END
    WHEN REGEXP_CONTAINS(LOWER(parameter),r'molzhaninovo|молжаниново')
			THEN CASE
				WHEN res_type = 'object' THEN 'МОЛЖАНИНОВО'
				WHEN res_type = 'crm_direction' THEN 'Москва'
				ELSE 'Москва'
			END
    WHEN REGEXP_CONTAINS(LOWER(parameter),r'mytischi|мытищи парк')
			THEN CASE
				WHEN res_type = 'object' THEN 'Мытищи Парк'
				WHEN res_type = 'crm_direction' THEN 'Москва'
				ELSE 'Москва'
			END
  	WHEN REGEXP_CONTAINS(LOWER(parameter),r'vnukovo|новое внуково')
			THEN CASE
				WHEN res_type = 'object' THEN 'НОВОЕ ВНУКОВО'
				WHEN res_type = 'crm_direction' THEN 'Москва'
				ELSE 'Москва'
			END
    WHEN REGEXP_CONTAINS(LOWER(parameter),r'nova|nova select') AND NOT REGEXP_CONTAINS(LOWER(parameter),r'novaya')
			THEN CASE
				WHEN res_type = 'object' THEN 'Nova Select'
				WHEN res_type = 'crm_direction' THEN 'Москва'
				ELSE 'Москва'
			END
  	WHEN REGEXP_CONTAINS(LOWER(parameter),r'novodanilovskaya|новоданиловская')
			THEN CASE
				WHEN res_type = 'object' THEN 'НОВОДАНИЛОВСКАЯ'
				WHEN res_type = 'crm_direction' THEN 'Москва'
				ELSE 'Москва'
			END
  	WHEN REGEXP_CONTAINS(LOWER(parameter),r'novograd.pavlino|новоград павлино')
			THEN CASE
				WHEN res_type = 'object' THEN 'Новоград Павлино'
				WHEN res_type = 'crm_direction' THEN 'Москва'
				ELSE 'Москва'
			END
  	WHEN REGEXP_CONTAINS(LOWER(parameter),r'o.tyabrskaya.98|октябрьская.98')
			THEN CASE
				WHEN res_type = 'object' THEN 'Октябрьская 98'
				WHEN res_type = 'crm_direction' THEN 'Москва'
				ELSE 'Москва'
			END
    WHEN REGEXP_CONTAINS(LOWER(parameter),r'ostafievo|остафьево')
			THEN CASE
				WHEN res_type = 'object' THEN 'ОСТАФЬЕВО'
				WHEN res_type = 'crm_direction' THEN 'Москва'
				ELSE 'Москва'
			END
  	WHEN REGEXP_CONTAINS(LOWER(parameter),r'podolskie.kvartaly|подольские кварталы')
			THEN CASE
				WHEN res_type = 'object' THEN 'Подольские Кварталы'
				WHEN res_type = 'crm_direction' THEN 'Москва'
				ELSE 'Москва'
			END
  	WHEN REGEXP_CONTAINS(LOWER(parameter),r'pribrezhnyj.park|прибрежный парк')
			THEN CASE
				WHEN res_type = 'object' THEN 'Прибрежный Парк'
				WHEN res_type = 'crm_direction' THEN 'Москва'
				ELSE 'Москва'
			END
    WHEN REGEXP_CONTAINS(LOWER(parameter),r'prigorod|пригород')
			THEN CASE
				WHEN res_type = 'object' THEN 'ПРИГОРОД'
				WHEN res_type = 'crm_direction' THEN 'Москва'
				ELSE 'Москва'
			END
  	WHEN REGEXP_CONTAINS(LOWER(parameter),r'putilkovo|путилково')
			THEN CASE
				WHEN res_type = 'object' THEN 'ПУТИЛКОВО'
				WHEN res_type = 'crm_direction' THEN 'Москва'
				ELSE 'Москва'
			END
    WHEN REGEXP_CONTAINS(LOWER(parameter),r'pyatnitskie.luga|пятницкие луга')
			THEN CASE
				WHEN res_type = 'object' THEN 'Пятницкие Луга'
				WHEN res_type = 'crm_direction' THEN 'Москва'
				ELSE 'Москва'
			END
  	WHEN REGEXP_CONTAINS(LOWER(parameter),r'pyatnitskoe.58|pyatnickoe.58|пятницкое.58')
			THEN CASE
				WHEN res_type = 'object' THEN 'Пятницкое 58'
				WHEN res_type = 'crm_direction' THEN 'Москва'
				ELSE 'Москва'
			END
    WHEN REGEXP_CONTAINS(LOWER(parameter),r'rublevskiy|рублевский квартал')
			THEN CASE
				WHEN res_type = 'object' THEN 'Рублевский квартал'
				WHEN res_type = 'crm_direction' THEN 'Москва'
				ELSE 'Москва'
			END
  	WHEN REGEXP_CONTAINS(LOWER(parameter),r'rumyancevo|rumyantsevo|квартал румянцево')
			THEN CASE
				WHEN res_type = 'object' THEN 'Квартал Румянцево'
				WHEN res_type = 'crm_direction' THEN 'Москва'
				ELSE 'Москва'
			END
  	WHEN REGEXP_CONTAINS(LOWER(parameter),r'sputnik|спутник') AND NOT REGEXP_CONTAINS(LOWER(parameter),r'samoletum')
			THEN CASE
				WHEN res_type = 'object' THEN 'СПУТНИК'
				WHEN res_type = 'crm_direction' THEN 'Москва'
				ELSE 'Москва'
			END
  	WHEN REGEXP_CONTAINS(LOWER(parameter),r'stremyann...2|стремянный.2')
			THEN CASE
				WHEN res_type = 'object' THEN 'Стремянный 2'
				WHEN res_type = 'crm_direction' THEN 'Москва'
				ELSE 'Москва'
			END
  	WHEN REGEXP_CONTAINS(LOWER(parameter),r'strogino|квартал строгино')
			THEN CASE
				WHEN res_type = 'object' THEN 'Квартал Строгино'
				WHEN res_type = 'crm_direction' THEN 'Москва'
				ELSE 'Москва'
			END
    WHEN REGEXP_CONTAINS(LOWER(parameter),r'tomilino|томилино')
			THEN CASE
				WHEN res_type = 'object' THEN 'ТОМИЛИНО'
				WHEN res_type = 'crm_direction' THEN 'Москва'
				ELSE 'Москва'
			END
  	WHEN REGEXP_CONTAINS(LOWER(parameter),r'troparevo|тропарево парк') AND NOT REGEXP_CONTAINS(LOWER(parameter),r'samoletum')
			THEN CASE
				WHEN res_type = 'object' THEN 'Тропарево Парк'
				WHEN res_type = 'crm_direction' THEN 'Москва'
				ELSE 'Москва'
			END
  	WHEN REGEXP_CONTAINS(LOWER(parameter),r'veresk|вереск')
			THEN CASE
				WHEN res_type = 'object' THEN 'Вереск'
				WHEN res_type = 'crm_direction' THEN 'Москва'
				ELSE 'Москва'
			END
  	WHEN REGEXP_CONTAINS(LOWER(parameter),r'vidnoe|новое видное')
			THEN CASE
				WHEN res_type = 'object' THEN 'Новое Видное'
				WHEN res_type = 'crm_direction' THEN 'Москва'
				ELSE 'Москва'
			END
  	WHEN REGEXP_CONTAINS(LOWER(parameter),r'zarechye|заречье парк')
			THEN CASE
				WHEN res_type = 'object' THEN 'Заречье Парк'
				WHEN res_type = 'crm_direction' THEN 'Москва'
				ELSE 'Москва'
			END
  	WHEN REGEXP_CONTAINS(LOWER(parameter),r'vere.ska.a.41|верейская')
			THEN CASE
				WHEN res_type = 'object' THEN 'ВЕРЕЙСКАЯ'
				WHEN res_type = 'crm_direction' THEN 'Москва'
				ELSE 'Москва'
			END
  	WHEN REGEXP_CONTAINS(LOWER(parameter),r'nekrasovka|некрасовка')
			THEN CASE
				WHEN res_type = 'object' THEN 'Некрасовка'
				WHEN res_type = 'crm_direction' THEN 'Москва'
				ELSE 'Москва'
			END		
  	WHEN REGEXP_CONTAINS(LOWER(parameter),r'мята')
			THEN CASE
				WHEN res_type = 'object' THEN 'Мята'
				WHEN res_type = 'crm_direction' THEN 'Москва'
				ELSE 'Москва'
			END			
  	WHEN REGEXP_CONTAINS(LOWER(parameter),r'кленовые аллеи')
			THEN CASE
				WHEN res_type = 'object' THEN 'Кленовые Аллеи'
				WHEN res_type = 'crm_direction' THEN 'Москва'
				ELSE 'Москва'
			END	
  	WHEN REGEXP_CONTAINS(LOWER(parameter),r'vost-kotel|восточный кот.л')
			THEN CASE
				WHEN res_type = 'object' THEN 'Восточный котел'
				WHEN res_type = 'crm_direction' THEN 'Москва'
				ELSE 'Москва'
			END
  	WHEN REGEXP_CONTAINS(LOWER(parameter),r'olkhovyi-kvartal|ольховый')
			THEN CASE
				WHEN res_type = 'object' THEN 'Ольховый Квартал'
				WHEN res_type = 'crm_direction' THEN 'Москва'
				ELSE 'Москва'
			END
		WHEN REGEXP_CONTAINS(LOWER(parameter),r'cl-nmsk_|кластер - новая москва|кластер нм|cluster novaya msk') AND NOT REGEXP_CONTAINS(LOWER(parameter),r'ret-olv')
			THEN CASE
				WHEN res_type = 'object' THEN 'Кластер - Новая Москва'
				WHEN res_type = 'crm_direction' THEN 'Москва'
				ELSE 'Москва'
			END
		WHEN REGEXP_CONTAINS(LOWER(parameter),r'cl-yug_|кластер - юг|южный.*кластер|cluster msk yug')
			THEN CASE
				WHEN res_type = 'object' THEN 'Кластер - Юг'
				WHEN res_type = 'crm_direction' THEN 'Москва'
				ELSE 'Москва'
			END
		WHEN REGEXP_CONTAINS(LOWER(parameter),r'cl-sever_|кластер - север|север.*кластер|cluster msk sever')
			THEN CASE
				WHEN res_type = 'object' THEN 'Кластер - Север'
				WHEN res_type = 'crm_direction' THEN 'Москва'
				ELSE 'Москва'
			END
		WHEN REGEXP_CONTAINS(LOWER(parameter),r'cl-zapad_|кластер.*запад|запад.*кластер|cluster msk zapad')
			THEN CASE
				WHEN res_type = 'object' THEN 'Кластер - Запад'
				WHEN res_type = 'crm_direction' THEN 'Москва'
				ELSE 'Москва'
			END
		WHEN REGEXP_CONTAINS(LOWER(parameter),r'cl-vostok_|кластер.*восто|восто.*кластер|cluster msk vostok')
			THEN CASE
				WHEN res_type = 'object' THEN 'Кластер - Восток'
				WHEN res_type = 'crm_direction' THEN 'Москва'
				ELSE 'Москва'
			END
		WHEN REGEXP_CONTAINS(LOWER(parameter),r'cl-bus_|кластер - бизнес-класс|cluster.*business|бизнес.класс')
			THEN CASE
				WHEN res_type = 'object' THEN 'Кластер - Бизнес-класс'
				WHEN res_type = 'crm_direction' THEN 'Москва'
				ELSE 'Москва'
			END

		### Регионы
		WHEN REGEXP_CONTAINS(LOWER(parameter),r'жк0') AND REGEXP_CONTAINS(LOWER(parameter),r'spb')
			THEN CASE
				WHEN res_type = 'object' THEN 'ЖИВИ В Рыбацком'
				WHEN res_type = 'crm_direction' THEN 'СПб'
				ELSE 'Регионы'
			END
  	WHEN REGEXP_CONTAINS(LOWER(parameter),r'жк0') AND REGEXP_CONTAINS(LOWER(parameter),r'tmn')
			THEN CASE
				WHEN res_type = 'object' THEN 'Чаркова, 72'
				WHEN res_type = 'crm_direction' THEN 'Тюмень'
				ELSE 'Регионы'
			END
  	WHEN REGEXP_CONTAINS(LOWER(parameter),r'жк0') AND REGEXP_CONTAINS(LOWER(parameter),r'vldv')
			THEN CASE
				WHEN res_type = 'object' THEN 'Сабанеева 125'
				WHEN res_type = 'crm_direction' THEN 'Владивосток'
				ELSE 'Регионы'
			END	
  	WHEN REGEXP_CONTAINS(LOWER(parameter),r'astrid|астрид')
			THEN CASE
				WHEN res_type = 'object' THEN 'АСТРИД (Колпино)'
				WHEN res_type = 'crm_direction' THEN 'СПб'
				ELSE 'Регионы'
			END	
  	WHEN REGEXP_CONTAINS(LOWER(parameter),r'spb brand|ipt.spb|mbl.sbp|spb.samolet|samolet.spb.*dinrem|спб общий') AND NOT REGEXP_CONTAINS(LOWER(parameter),r'detmetr')
			THEN CASE
				WHEN res_type = 'object' THEN 'СПБ общий'
				WHEN res_type = 'crm_direction' THEN 'СПб'
				ELSE 'Регионы'
			END
  	WHEN REGEXP_CONTAINS(LOWER(parameter),r'kolpino|красный кирпичник|новое колпино')
			THEN CASE
				WHEN res_type = 'object' THEN 'Красный Кирпичник (Новое Колпино)'
				WHEN res_type = 'crm_direction' THEN 'СПб'
				ELSE 'Регионы'
			END
  	WHEN REGEXP_CONTAINS(LOWER(parameter),r'kurort.kvartal|kurortkvartal|курортный квартал|песочный')
			THEN CASE
				WHEN res_type = 'object' THEN 'Курортный Квартал (Песочный)'
				WHEN res_type = 'crm_direction' THEN 'СПб'
				ELSE 'Регионы'
			END
    WHEN REGEXP_CONTAINS(LOWER(parameter),r'lagolovo|лаголово')
			THEN CASE
				WHEN res_type = 'object' THEN 'Квартал Лаголово'
				WHEN res_type = 'crm_direction' THEN 'СПб'
				ELSE 'Регионы'
			END
  	WHEN REGEXP_CONTAINS(LOWER(parameter),r'lavriki|лаврики')
			THEN CASE
				WHEN res_type = 'object' THEN 'Новые Лаврики'
				WHEN res_type = 'crm_direction' THEN 'СПб'
				ELSE 'Регионы'
			END
  	WHEN REGEXP_CONTAINS(LOWER(parameter),r'nevskaya.dolina|невская долина')
			THEN CASE
				WHEN res_type = 'object' THEN 'Невская Долина'
				WHEN res_type = 'crm_direction' THEN 'СПб'
				ELSE 'Регионы'
			END
  	WHEN REGEXP_CONTAINS(LOWER(parameter),r'rybacko|живи.*рыбацком')
			THEN CASE
				WHEN res_type = 'object' THEN 'ЖИВИ В Рыбацком'
				WHEN res_type = 'crm_direction' THEN 'СПб'
				ELSE 'Регионы'
			END
  	WHEN REGEXP_CONTAINS(LOWER(parameter),r'sunday|санд.й|сосновая поляна')
			THEN CASE
				WHEN res_type = 'object' THEN 'САНДЕЙ'
				WHEN res_type = 'crm_direction' THEN 'СПб'
				ELSE 'Регионы'
			END
    WHEN REGEXP_CONTAINS(LOWER(parameter),r'toriki|квартал торики')
			THEN CASE
				WHEN res_type = 'object' THEN 'Квартал Торики'
				WHEN res_type = 'crm_direction' THEN 'СПб'
				ELSE 'Регионы'
			END
  	WHEN REGEXP_CONTAINS(LOWER(parameter),r'yuzhnaya.neva|yuzhaya.neva|южная нева')
			THEN CASE
				WHEN res_type = 'object' THEN 'Южная Нева'
				WHEN res_type = 'crm_direction' THEN 'СПб'
				ELSE 'Регионы'
			END
  	WHEN REGEXP_CONTAINS(LOWER(parameter),r'charkova|чаркова.*72|тюмень')
			THEN CASE
				WHEN res_type = 'object' THEN 'Чаркова, 72'
				WHEN res_type = 'crm_direction' THEN 'Тюмень'
				ELSE 'Регионы'
			END
  	WHEN REGEXP_CONTAINS(LOWER(parameter),r'sabaneeva|сабанеева.*125')
			THEN CASE
				WHEN res_type = 'object' THEN 'Сабанеева 125'
				WHEN res_type = 'crm_direction' THEN 'Владивосток'
				ELSE 'Регионы'
			END
  	WHEN REGEXP_CONTAINS(LOWER(parameter),r'малая охта')
			THEN CASE
				WHEN res_type = 'object' THEN 'МАЛАЯ ОХТА'
				WHEN res_type = 'crm_direction' THEN 'СПб'
				ELSE 'Регионы'
			END		
  	WHEN REGEXP_CONTAINS(LOWER(parameter),r'ne(i|j)but|нейбута')
			THEN CASE
				WHEN res_type = 'object' THEN 'Квартал Нейбута'
				WHEN res_type = 'crm_direction' THEN 'Владивосток'
				ELSE 'Регионы'
			END		

		### Сервисы
  	WHEN REGEXP_CONTAINS(LOWER(parameter),r'жк0') AND REGEXP_CONTAINS(LOWER(parameter),r'istra')
			THEN CASE
				WHEN res_type = 'object' THEN 'Истра Дом'
				WHEN res_type = 'crm_direction' THEN 'ИЖС'
				ELSE 'Сервисы'
			END
    WHEN REGEXP_CONTAINS(LOWER(parameter),r'celeport|clprt_samolet|clprt|целепорт')
			THEN CASE
				WHEN res_type = 'object' THEN 'Целепорт'
				WHEN res_type = 'crm_direction' THEN 'Целепорт'
				ELSE 'Сервисы'
			END
  	WHEN REGEXP_CONTAINS(LOWER(parameter),r'samolet.rto|rto.samolet|_rto_|и живи-ка')
			THEN CASE
				WHEN res_type = 'object' THEN 'И живи-ка'
				WHEN res_type = 'crm_direction' THEN 'И живи-ка'
				ELSE 'Сервисы'
			END
  	WHEN REGEXP_CONTAINS(LOWER(parameter),r'port.emm')
			THEN CASE
				WHEN res_type = 'object' THEN 'Port EMM'
				WHEN res_type = 'crm_direction' THEN 'ИЖС'
				ELSE 'Сервисы'
			END
  	WHEN REGEXP_CONTAINS(LOWER(parameter),r'shkola-proektirovan|школа проектирования')
			THEN CASE
				WHEN res_type = 'object' THEN 'Школа проектирования'
				WHEN res_type = 'crm_direction' THEN 'ИЖС'
				ELSE 'Сервисы'
			END
  	WHEN REGEXP_CONTAINS(LOWER(parameter),r'pushkino.dom|пушкино дом')
			THEN CASE
				WHEN res_type = 'object' THEN 'Пушкино Дом'
				WHEN res_type = 'crm_direction' THEN 'ИЖС'
				ELSE 'Сервисы'
			END
  	WHEN REGEXP_CONTAINS(LOWER(parameter),r'istra|истра дом')
			THEN CASE
				WHEN res_type = 'object' THEN 'Истра Дом'
				WHEN res_type = 'crm_direction' THEN 'ИЖС'
				ELSE 'Сервисы'
			END
  	WHEN REGEXP_CONTAINS(LOWER(parameter),r'dmitrov.dom|дмитров')
			THEN CASE
				WHEN res_type = 'object' THEN 'Дмитров Дом'
				WHEN res_type = 'crm_direction' THEN 'ИЖС'
				ELSE 'Сервисы'
			END
  	WHEN REGEXP_CONTAINS(LOWER(parameter),r'zagorod-fest|загород fest')
			THEN CASE
				WHEN res_type = 'object' THEN 'Загород Fest'
				WHEN res_type = 'crm_direction' THEN 'Флайт'
				ELSE 'Сервисы'
			END
  	WHEN REGEXP_CONTAINS(LOWER(parameter),r'life.samolet|life') AND NOT REGEXP_CONTAINS(LOWER(parameter),r'samoletum|dinrem|kv-life-min')
			THEN CASE
				WHEN res_type = 'object' THEN 'LIFE'
				WHEN res_type = 'crm_direction' THEN 'Флайт'
				ELSE 'Сервисы'
			END

		### СММ
  	WHEN REGEXP_CONTAINS(LOWER(parameter),r'samolet.smm|смм')
			THEN CASE
				WHEN res_type = 'object' THEN 'СММ'
				WHEN res_type = 'crm_direction' THEN 'СММ'
				ELSE 'СММ'
			END

		### Самолетум
  	WHEN REGEXP_CONTAINS(LOWER(parameter),r'samoletum-school-sputnik|школа')
			THEN CASE
				WHEN res_type = 'object' THEN 'Школа'
				WHEN res_type = 'crm_direction' THEN 'Самолетум'
				ELSE 'Самолетум'
			END
  	WHEN REGEXP_CONTAINS(LOWER(parameter),r'samoletum-school-curriculum|доп. образование')
			THEN CASE
				WHEN res_type = 'object' THEN 'Доп. образование'
				WHEN res_type = 'crm_direction' THEN 'Самолетум'
				ELSE 'Самолетум'
			END
  	WHEN REGEXP_CONTAINS(LOWER(parameter),r'samoletum.sad|самолетум сад')
			THEN CASE
				WHEN res_type = 'object' THEN 'Самолетум Сад ДОД'
				WHEN res_type = 'crm_direction' THEN 'Самолетум'
				ELSE 'Самолетум'
			END
  	WHEN REGEXP_CONTAINS(LOWER(parameter),r'samoletum-school-dod|дод')
			THEN CASE
				WHEN res_type = 'object' THEN 'ДОД'
				WHEN res_type = 'crm_direction' THEN 'Самолетум'
				ELSE 'Самолетум'
			END
  	WHEN REGEXP_CONTAINS(LOWER(parameter),r'samoletum|samoletum|самолетум')
			THEN CASE
				WHEN res_type = 'object' THEN 'Самолетум'
				WHEN res_type = 'crm_direction' THEN 'Самолетум'
				ELSE 'Самолетум'
			END

		### Общебренд
    WHEN REGEXP_CONTAINS(LOWER(parameter),r'senler')
			THEN CASE
				WHEN res_type = 'object' THEN 'Senler'
				WHEN res_type = 'crm_direction' THEN 'Москва'
				ELSE 'Москва'
			END	
    WHEN REGEXP_CONTAINS(LOWER(parameter),r'_flash|flash sale|flashsale|флешсейл')
			THEN CASE
				WHEN res_type = 'object' THEN 'Flash sale - общебренд'
				WHEN res_type = 'crm_direction' THEN 'Москва'
				ELSE 'Москва'
			END		
    WHEN REGEXP_CONTAINS(LOWER(parameter),r'trdn-flat|трейд.ин')
			THEN CASE
				WHEN res_type = 'object' THEN 'Общебренд (Трейд-ин)'
				WHEN res_type = 'crm_direction' THEN 'Москва'
				ELSE 'Москва'
			END	
    WHEN REGEXP_CONTAINS(LOWER(parameter),r'lead-vk-engineer|lead-ovik-engineer|main-engineer|hr вакансии')
			THEN CASE
				WHEN res_type = 'object' THEN 'HR вакансии'
				WHEN res_type = 'crm_direction' THEN 'Вакансии'
				ELSE 'Сервисы'
			END		
    WHEN date < '2024-05-01' AND REGEXP_CONTAINS(LOWER(parameter),r'mbl_msk|_mbl_|квартиры с мебелью')
			THEN CASE
				WHEN res_type = 'object' THEN 'Квартиры с мебелью'
				WHEN res_type = 'crm_direction' THEN 'Москва'
				ELSE 'Москва'
			END		
    WHEN date < '2024-05-01' AND REGEXP_CONTAINS(LOWER(parameter),r'ipt_msk|ipt-|ипотека')
			THEN CASE
				WHEN res_type = 'object' THEN 'Ипотека'
				WHEN res_type = 'crm_direction' THEN 'Москва'
				ELSE 'Москва'
			END	
    WHEN date < '2024-05-01' AND REGEXP_CONTAINS(LOWER(parameter),r'_installment|рассрочка')
			THEN CASE
				WHEN res_type = 'object' THEN 'Рассрочка'
				WHEN res_type = 'crm_direction' THEN 'Москва'
				ELSE 'Москва'
			END	
    WHEN date < '2024-05-01' AND  REGEXP_CONTAINS(LOWER(parameter),r'samolet.*_ret|rem_samolet_ret|lead-p_minpay.vid_samolet_ct_ndv_lead_mmo_23_55_2|общебренд ретаргетинг|общий ремаркетинг')
			THEN CASE
				WHEN res_type = 'object' THEN 'Общебренд ретаргетинг'
				WHEN res_type = 'crm_direction' THEN 'Москва'
				ELSE 'Москва'
			END				
    WHEN date >= '2024-05-01' AND  REGEXP_CONTAINS(LOWER(parameter),r'samolet_msk_lead_ret-olv|ретаргетинг olv бренд')
			THEN CASE
				WHEN res_type = 'object' THEN 'Ретаргетинг OLV Бренд'
				WHEN res_type = 'crm_direction' THEN 'Москва'
				ELSE 'Москва'
			END		
    WHEN date >= '2024-05-01' AND  REGEXP_CONTAINS(LOWER(parameter),r'cl-nmsk_msk_lead_ret-olv|ретаргетинг olv кластер новая москва')
			THEN CASE
				WHEN res_type = 'object' THEN 'Ретаргетинг OLV Кластер Новая Москва'
				WHEN res_type = 'crm_direction' THEN 'Москва'
				ELSE 'Москва'
			END		
    WHEN date >= '2024-05-01' AND  REGEXP_CONTAINS(LOWER(parameter),r'samolet_msk_lead|samolet_msk_traf|samolet_msk_quiz|бренд самолет|общий ремаркетинг|ipt_msk|ipt-|ипотека|mbl_msk|_mbl_|квартиры с мебелью|_installment|рассрочка|samolet.*_ret|samolet.*_lal|rem_samolet_ret|lead-p_minpay.vid_samolet_ct_ndv_lead_mmo_23_55_2|общебренд ретаргетинг|общий ремаркетинг') AND NOT REGEXP_CONTAINS(LOWER(parameter),r'dinrem')
			THEN CASE
				WHEN res_type = 'object' THEN 'Бренд Самолет'
				WHEN res_type = 'crm_direction' THEN 'Москва'
				ELSE 'Москва'
			END		
    WHEN REGEXP_CONTAINS(LOWER(parameter),r'samolet.*d.nre|samolet_msk_traf_dinrem|samolet.lal|общебренд динрем|mg_samolet_msk_lead_lead-30d-1875-mmo_banner_02-24|mg_samolet_msk_lead_sub-1875-mmo_banner_02-24|mg_samolet_msk_lead_sub-2565-mmo_banner_02-24')
			THEN CASE
				WHEN res_type = 'object' THEN 'Общебренд динрем'
				WHEN res_type = 'crm_direction' THEN 'Москва'
				ELSE 'Москва'
			END	
    WHEN REGEXP_CONTAINS(LOWER(parameter),r'quiz-mt|общебренд мт')
			THEN CASE
				WHEN res_type = 'object' THEN 'Общебренд МТ'
				WHEN res_type = 'crm_direction' THEN 'Москва'
				ELSE 'Москва'
			END	
    WHEN REGEXP_CONTAINS(LOWER(parameter),r'petsflats')
			THEN CASE
				WHEN res_type = 'object' THEN 'Petsflats'
				WHEN res_type = 'crm_direction' THEN 'Москва'
				ELSE 'Москва'
			END	
    WHEN REGEXP_CONTAINS(LOWER(parameter),r'_detmetr.*msk|детский метр москва')
			THEN CASE
				WHEN res_type = 'object' THEN 'Детский метр Москва'
				WHEN res_type = 'crm_direction' THEN 'Москва'
				ELSE 'Москва'
			END	
    WHEN REGEXP_CONTAINS(LOWER(parameter),r'_detmetr.*spb|детский метр спб')
			THEN CASE
				WHEN res_type = 'object' THEN 'Детский метр СПб'
				WHEN res_type = 'crm_direction' THEN 'СПб'
				ELSE 'Регионы'
			END	
    WHEN REGEXP_CONTAINS(LOWER(parameter),r'brand.msk|samolet_msk|ipt_msk|zhk_samolet_ct_vk|samoletgroup|samolet.*bonus')
			THEN CASE
				WHEN res_type = 'object' THEN 'SAMOLETGROUP'
				WHEN res_type = 'crm_direction' THEN 'Москва'
				ELSE 'Москва'
			END

		ELSE '-'
  END