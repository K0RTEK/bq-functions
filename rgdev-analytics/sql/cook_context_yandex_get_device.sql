### cook_context_yandex.get_device`(date, utm_source, utm_medium, utm_campaign, utm_content,term)
    ### Определение устройства
                    regexp_extract(
                            CONCAT("|",TRIM(REPLACE(utm_content,":","|")),"|"), 
                            r'\|dvc\|(.+?)\|')