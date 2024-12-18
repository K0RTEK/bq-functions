### raw_crm.get_date(parameter)
	DATE(
		2024,
		CASE		
			WHEN REGEXP_CONTAINS(parameter,r'янв') THEN 1
			WHEN REGEXP_CONTAINS(parameter,r'фев') THEN 2	
			WHEN REGEXP_CONTAINS(parameter,r'мар') THEN 3	
			WHEN REGEXP_CONTAINS(parameter,r'апр') THEN 4	
			WHEN REGEXP_CONTAINS(parameter,r'мая') THEN 5	
			WHEN REGEXP_CONTAINS(parameter,r'июн') THEN 6	
			WHEN REGEXP_CONTAINS(parameter,r'июл') THEN 7	
			WHEN REGEXP_CONTAINS(parameter,r'авг') THEN 8	
			WHEN REGEXP_CONTAINS(parameter,r'сен') THEN 9	
			WHEN REGEXP_CONTAINS(parameter,r'окт') THEN 10	
			WHEN REGEXP_CONTAINS(parameter,r'ноя') THEN 11	
			WHEN REGEXP_CONTAINS(parameter,r'дек') THEN 12	
		END,
		CAST(REGEXP_EXTRACT(parameter,r'[0-9]+') AS INT64)
		)