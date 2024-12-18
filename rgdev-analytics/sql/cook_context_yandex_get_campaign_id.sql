### cook_context_yandex.get_campaign_id`(date, utm_source, utm_medium, utm_campaign, utm_content,term)
    ### Определение ID Кампании
                    regexp_extract(
                            CONCAT("|",TRIM(REPLACE(utm_content,":","|")),"|"), 
                            r'\|cid\|(.+?)\|')