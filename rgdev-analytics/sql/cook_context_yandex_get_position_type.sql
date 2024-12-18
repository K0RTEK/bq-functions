### cook_context_yandex.get_position_type`(date, utm_source, utm_medium, utm_campaign, utm_content,term)
    ### Тип позиции
      CAST(NULL AS STRING)
                    -- regexp_extract(
                    --         CONCAT("|",TRIM(REPLACE(utm_content,":","|")),"|"), 
                    --         r'\|pos\|(.+?)\|')