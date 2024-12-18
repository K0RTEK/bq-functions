### cook_context_yandex.get_group_id`(date, utm_source, utm_medium, utm_campaign, utm_content,term)
    ### ID группы объявлений
                    regexp_extract(
                            CONCAT("|",TRIM(REPLACE(utm_content,":","|")),"|"), 
                            r'\|gid\|(.+?)\|')