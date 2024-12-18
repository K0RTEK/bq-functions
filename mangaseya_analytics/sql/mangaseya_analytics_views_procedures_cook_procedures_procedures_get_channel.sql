CASE
          ### CPA - Лидогенерация
            WHEN `cook_procedures.get_cpa`(
              CONCAT(
                IFNULL(calltracking,""),"_",
                IFNULL(utm_source,""),"_",
                IFNULL(utm_medium,""),"_",
                IFNULL(utm_campaign,""),"_",
                IFNULL(utm_content,""),"_",
                IFNULL(utm_term,""))
                ) IS NOT NULL 
            -- WHEN LOWER(calltracking) LIKE "%лидогенераторы%" 
              THEN "Лидогенерация"

            WHEN (LOWER(TRIM(utm_source)) = 'yandex' AND LOWER(TRIM(utm_medium)) IN ('cpc','cpm')) OR REGEXP_CONTAINS(LOWER(calltracking),r'яндекс(.|..)директ') 
              THEN 'Яндекс Директ'

            WHEN ( REGEXP_CONTAINS(LOWER(utm_source), r'google')
                AND REGEXP_CONTAINS(LOWER(utm_medium), r'cpc')
                AND ( REGEXP_CONTAINS(LOWER(utm_campaign), r'mg_')
                  OR REGEXP_CONTAINS(LOWER(utm_content), r'mg_')
                  OR REGEXP_CONTAINS(LOWER(utm_term), r'mg_') ) ) OR( REGEXP_CONTAINS(LOWER(calltracking), r'mg|sm')
                AND REGEXP_CONTAINS(LOWER(calltracking), r'google|гугл') ) 
              THEN 'Google Ads'

            WHEN traffic_source = 'Search engine traffic' AND utm_source IS NULL AND utm_medium IS NULL 
              THEN 'Поисковые системы'

            WHEN traffic_source = 'Link traffic'
                  AND utm_source IS NULL
                  AND utm_medium IS NULL 
              THEN 'Переходы по ссылкам' --

              -- WHEN REGEXP_CONTAINS(LOWER(utm_source), 'yandex') 
                  -- AND LOWER(utm_medium) = 'cpc|cpm' -- AND NOT ( -- REGEXP_CONTAINS(LOWER(utm_campaign), r'mg_') -- OR REGEXP_CONTAINS(LOWER(utm_content), r'mg_') -- OR REGEXP_CONTAINS(LOWER(utm_term), r'mg_') -- ) 
              -- THEN 'Чужая контекстная реклама'

            WHEN (
                  REGEXP_CONTAINS(LOWER(utm_source),r'vk_ads|vk_reklama')
                  OR REGEXP_CONTAINS(LOWER(utm_source),r'_vk$|^vk$|^vk_')
                  OR REGEXP_CONTAINS(LOWER(utm_source),r'mytarget|_mt$')
                  OR REGEXP_CONTAINS(LOWER(utm_source),r'facebook|fb_ig|inst|_fb$')
                  OR REGEXP_CONTAINS(LOWER(utm_source),r'tiktok')
                  OR REGEXP_CONTAINS(LOWER(utm_source),r'telegram') 
                  )
                  AND utm_medium IN ('cpc','cpm') 
              THEN 'Реклама в соц.сетях'

            END