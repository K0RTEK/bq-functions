### cook_context_yandex.get_placement`(date, utm_source, utm_medium, utm_campaign, utm_content,term)
    ### Плейсмент для объявлений сети
                    regexp_extract(
                            CONCAT("|",TRIM(REPLACE(utm_content,":","|")),"|"), 
                            r'\|src\|(.+?)\|')