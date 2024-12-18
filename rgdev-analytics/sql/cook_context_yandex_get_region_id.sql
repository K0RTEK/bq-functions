### cook_context_yandex.get_region_id`(date, utm_source, utm_medium, utm_campaign, utm_content,term)
    ### ID Региона (reg)
                    regexp_extract(
                            CONCAT("|",TRIM(REPLACE(utm_content,":","|")),"|"), 
                            r'\|reg\|(.+?)\|')