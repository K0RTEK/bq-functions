/* 
            "S" = разделитель, его невозможно встретить в исходнике, потому что он прошёл через LOWER
            Для учёта случаев когда впороли пробел, например, стоит S*
            +? = ленивый квантификатор, подхватит всё что там лежит по этому определению.

            -- Обязательные:
              `cook_context_yandex.utm_decode`(date,'campaign_id',utm_source,utm_medium,utm_campaign,utm_content,utm_term) as campaign_id,
              `cook_context_yandex.utm_decode`(date,'ad_group_id',utm_source,utm_medium,utm_campaign,utm_content,utm_term) as ad_group_id,
              `cook_context_yandex.utm_decode`(date,'ad_id',utm_source,utm_medium,utm_campaign,utm_content,utm_term) as ad_id,
              `cook_context_yandex.utm_decode`(date,'criterion_id',utm_source,utm_medium,utm_campaign,utm_content,utm_term) as criterion_id,
              `cook_context_yandex.utm_decode`(date,'device',utm_source,utm_medium,utm_campaign,utm_content,utm_term) as device,
              `cook_context_yandex.utm_decode`(date,'direct_placement',utm_source,utm_medium,utm_campaign,utm_content,utm_term) as direct_placement,
              `cook_context_yandex.utm_decode`(date,'region_id',utm_source,utm_medium,utm_campaign,utm_content,utm_term) as region_id,

            -- Не обязательные:
              `cook_context_yandex.utm_decode`(date,'banner_id',utm_source,utm_medium,utm_campaign,utm_content,utm_term) as banner_id,
              `cook_context_yandex.utm_decode`(date,'position',utm_source,utm_medium,utm_campaign,utm_content,utm_term) as position,
              `cook_context_yandex.utm_decode`(date,'position_type',utm_source,utm_medium,utm_campaign,utm_content,utm_term) as position_type,
              `cook_context_yandex.utm_decode`(date,'retargeting_id',utm_source,utm_medium,utm_campaign,utm_content,utm_term) as retargeting_id,
              `cook_context_yandex.utm_decode`(date,'source_type',utm_source,utm_medium,utm_campaign,utm_content,utm_term) as source_type,
            */
            CASE
              WHEN parameter = 'campaign_id' THEN REGEXP_EXTRACT(REGEXP_REPLACE(LOWER(TRIM(
                utm_content)), r'(^|$| |\||%7|:)', 'S'),
                r'ScidS*(.+?)S')
              WHEN parameter = 'ad_group_id' THEN REGEXP_EXTRACT(REGEXP_REPLACE(LOWER(TRIM(
                utm_content)), r'(^|$| |\||%7|:)', 'S'),
                r'SgidS*(.+?)S')
              WHEN parameter = 'ad_id' THEN REGEXP_EXTRACT(REGEXP_REPLACE(LOWER(TRIM(
                utm_content)), r'(^|$| |\||%7|:)', 'S'),
                r'SadidS*(.+?)S')
              WHEN parameter = 'criterion_id' THEN REGEXP_EXTRACT(REGEXP_REPLACE(LOWER(TRIM(
                utm_content)), r'(^|$| |\||%7|:)', 'S'),
                r'Skw_idS*(.+?)S')
              WHEN parameter = 'device' THEN REGEXP_EXTRACT(REGEXP_REPLACE(LOWER(TRIM(
                utm_content)), r'(^|$| |\||%7|:)', 'S'),
                r'SdtS*(.+?)S')
              WHEN parameter = 'direct_placement' THEN REGEXP_EXTRACT(REGEXP_REPLACE(LOWER(TRIM(
                utm_content)), r'(^|$| |\||%7|:)', 'S'),
                r'SsS*(.+?)S')
              WHEN parameter = 'region_id' THEN REGEXP_EXTRACT(REGEXP_REPLACE(LOWER(TRIM(
                utm_content)), r'(^|$| |\||%7|:)', 'S'),
                r'SgeoS*(.+?)S')
              WHEN parameter = 'banner_id' THEN REGEXP_EXTRACT(REGEXP_REPLACE(LOWER(TRIM(
                utm_content)), r'(^|$| |\||%7|:)', 'S'),
                r'SNonaInfoS*(.+?)S')
              WHEN parameter = 'position' THEN REGEXP_EXTRACT(REGEXP_REPLACE(LOWER(TRIM(
                utm_content)), r'(^|$| |\||%7|:)', 'S'),
                r'SpS*(.+?)S')
              WHEN parameter = 'position_type' THEN REGEXP_EXTRACT(REGEXP_REPLACE(LOWER(TRIM(
                utm_content)), r'(^|$| |\||%7|:)', 'S'),
                r'SptS*(.+?)S')
              WHEN parameter = 'retargeting_id' THEN REGEXP_EXTRACT(REGEXP_REPLACE(LOWER(TRIM(
                utm_content)), r'(^|$| |\||%7|:)', 'S'),
                r'SreS*(.+?)S')

              WHEN parameter = 'source_type' -- нужен для универсальных кампаний и не метчится ними полностью из-за разницы в типе (?)
                THEN REGEXP_EXTRACT(REGEXP_REPLACE(LOWER(TRIM(
                utm_content)), r'(^|$| |\||%7|:)', 'S'),
                r'SstS*(.+?)S')
            END