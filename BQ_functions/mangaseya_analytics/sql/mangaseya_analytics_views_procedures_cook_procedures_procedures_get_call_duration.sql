### cook_procedures.get_call_duration(call_duration)

    CASE
        WHEN CHAR_LENGTH(call_duration) > 8 OR CAST(REGEXP_EXTRACT(call_duration,'..:..:(.*)') AS INT) >= 60
            THEN 
                PARSE_TIME('%H:%M:%S', 
                    CONCAT('0:',
                        IF(
                            CHAR_LENGTH( IFNULL(REGEXP_EXTRACT(CAST(CAST(REGEXP_EXTRACT(call_duration,'..:..:(.*)') AS INT)/60 AS STRING),r'(.*)\.'),CAST(CAST(REGEXP_EXTRACT(call_duration,'..:..:(.*)') AS INT)/60 AS STRING))) <2, 
                            CONCAT('0', IFNULL(REGEXP_EXTRACT(CAST(CAST(REGEXP_EXTRACT(call_duration,'..:..:(.*)') AS INT)/60 AS STRING),r'(.*)\.'),CAST(CAST(REGEXP_EXTRACT(call_duration,'..:..:(.*)') AS INT)/60 AS STRING))),
                            IFNULL(REGEXP_EXTRACT(CAST(CAST(REGEXP_EXTRACT(call_duration,'..:..:(.*)') AS INT)/60 AS STRING),r'(.*)\.'),CAST(CAST(REGEXP_EXTRACT(call_duration,'..:..:(.*)') AS INT)/60 AS STRING))
                            )
                        ,':',
                        IF(
                            CHAR_LENGTH(CAST(ROUND(CAST(CONCAT('0.', IFNULL(REGEXP_EXTRACT(CAST(ROUND(CAST(REGEXP_EXTRACT(call_duration,'..:..:(.*)') AS INT)/60,2) AS STRING),r'\.(.*)') ,'0')) AS NUMERIC)*60,0) AS STRING)) <2,
                            CONCAT('0', CAST(ROUND(CAST(CONCAT('0.', IFNULL(REGEXP_EXTRACT(CAST(ROUND(CAST(REGEXP_EXTRACT(call_duration,'..:..:(.*)') AS INT)/60,2) AS STRING),r'\.(.*)') ,'0')) AS NUMERIC)*60,0) AS STRING)),
                            CAST(ROUND(CAST(CONCAT('0.',REGEXP_EXTRACT(CAST(ROUND(CAST(REGEXP_EXTRACT(call_duration,'..:..:(.*)') AS INT)/60,2) AS STRING),r'\.(.*)') ) AS NUMERIC)*60,0) AS STRING)
                            )
                    )
                )
        ELSE PARSE_TIME('%H:%M:%S',call_duration) 
  END