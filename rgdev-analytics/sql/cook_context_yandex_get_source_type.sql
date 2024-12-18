### cook_context_yandex.get_source_type`(date, utm_source, utm_medium, utm_campaign, utm_content,term)
    ### Тип размещения поиск/сеть
                    CASE
                    WHEN regexp_contains(lower(utm_term), r'src\|context|src\|{n}|src%7ccontext|src:context|st\|context|st%7ccontext|st:context|st\|{n}|st%7c{n}|src%7c{n}|src:{n}|st:{n}') OR
                            regexp_contains(lower(utm_content), r'src\|context|src\|{n}|src%7ccontext|src:context|st\|context|st%7ccontext|st:context|st\|{n}|st%7c{n}|src%7c{n}|src:{n}|st:{n}')
                            THEN 'ad_network'
                    WHEN regexp_contains(lower(utm_term), r'src\|search|src\|g|src%7csearch|src:search|st\|search|st%7csearch|st:search|st\|s|st:s|st\|g|src:g|src\|s|src:s|src%7cs|src%7cg|st%7cs|st%7cg|src:d|src\|d|src%7cd|st:d|st\|d|st%7cd') OR
                            regexp_contains(lower(utm_content), r'src\|search|src\|g|src%7csearch|src:search|st\|search|st%7csearch|st:search|st\|s|st:s|st\|g|src:g|src\|s|src:s|src%7cs|src%7cg|st%7cs|st%7cg|src:d|src\|d|src%7cd|st:d|st\|d|st%7cd')
                            THEN 'search'
                    END