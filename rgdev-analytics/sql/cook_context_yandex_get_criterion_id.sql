### cook_context_yandex.get_criterion_id`(date, utm_source, utm_medium, utm_campaign, utm_content,term)


                  ifnull(regexp_extract(lower(utm_term), r'\|ret:(\d+)\|'), regexp_extract(lower(utm_content), r'\|ret:(\d+)\|')
                  )