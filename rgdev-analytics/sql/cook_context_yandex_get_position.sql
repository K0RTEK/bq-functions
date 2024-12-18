### cook_context_yandex.get_position`(date, utm_source, utm_medium, utm_campaign, utm_content,term)
    ### Позиция показа (pos, для сети=0)
                    regexp_extract(
                            CONCAT("|",TRIM(REPLACE(utm_content,":","|")),"|"), 
                            r'\|pos\|(.+?)\|')