### cook_context_yandex.get_banner_id`(date, utm_source, utm_medium, utm_campaign, utm_content,term)
    ### ID Ообъявления (ad_id,b,banner)
                    regexp_extract(
                            CONCAT("|",TRIM(REPLACE(utm_content,":","|")),"|"), 
                            r'\|aid\|(.+?)\|')