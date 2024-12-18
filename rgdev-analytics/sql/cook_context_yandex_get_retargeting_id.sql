### cook_context_yandex.get_retargeting_id`(date, utm_source, utm_medium, utm_campaign, utm_content,term)
    ### Ретаргетинг (ret,rt)
                    regexp_extract(
                            CONCAT("|",TRIM(REPLACE(utm_content,":","|")),"|"), 
                            r'\|ret\|(.+?)\|')