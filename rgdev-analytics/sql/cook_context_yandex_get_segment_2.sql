### cook_context_yandex.get_segment_2`(campaign_name)
    -- ( |_|-|^)( |-|_|$)
    CASE
      WHEN REGEXP_CONTAINS(LOWER(campaign_name),r'( |_|-|^)brand( |-|_|$)') 
        AND NOT REGEXP_CONTAINS(LOWER(campaign_name),r'Без исключений') 
        THEN 'Бренд'

      WHEN REGEXP_CONTAINS(LOWER(campaign_name),r'( |_|-|^)compet( |-|_|$)|( |_|-|^)competitors( |-|_|$)') 
        AND NOT REGEXP_CONTAINS(LOWER(campaign_name),r'Без исключений') 
        THEN 'Конкуренты'

      WHEN REGEXP_CONTAINS(LOWER(campaign_name),r'( |_|-|^)geo( |-|_|$)') 
        AND NOT REGEXP_CONTAINS(LOWER(campaign_name),r'Без исключений') 
        THEN 'Гео'

      WHEN REGEXP_CONTAINS(LOWER(campaign_name),r'(_|-|^)generic( |-|_|$)') 
        AND NOT REGEXP_CONTAINS(LOWER(campaign_name),r'autotargeting') 
        THEN 'Общие'

      WHEN REGEXP_CONTAINS(LOWER(campaign_name),r'( |_|-|^)визитка( |-|_|$)|(^|_| |-)vizitka( |-|_|$)') 
        AND NOT REGEXP_CONTAINS(LOWER(campaign_name),r'Без исключений') 
        THEN 'Визитка'

      WHEN REGEXP_CONTAINS(LOWER(campaign_name),r'( |_|-|^)retargeting( |-|_|$)|( |_|-|^)remarketing( |-|_|$)|( |_|-|^)retarget( |-|_|$)|( |_|-|^)remarket( |-|_|$)') 
        AND NOT REGEXP_CONTAINS(LOWER(campaign_name),r'Без исключений') 
        THEN 'Ретаргетинг'

      WHEN REGEXP_CONTAINS(LOWER(campaign_name),r'( |_|-|^)search( |-|_|$)') 
        -- AND NOT REGEXP_CONTAINS(LOWER(campaign_name),r'(_|-|^)brand( |-|_|$)') 
        THEN 'Поиск'

      WHEN REGEXP_CONTAINS(LOWER(campaign_name),r'( |_|-|^)network( |-|_|$)') 
        -- AND NOT REGEXP_CONTAINS(LOWER(campaign_name),r'( |_|-|^)retargeting( |-|_|$)|( |_|-|^)remarketing( |-|_|$)|( |_|-|^)retarget( |-|_|$)|( |_|-|^)remarket( |-|_|$)') 
        THEN 'РСЯ'

      WHEN REGEXP_CONTAINS(LOWER(campaign_name),r'( |_|-|^)mc( |-|_|$)') 
        AND NOT REGEXP_CONTAINS(LOWER(campaign_name),r'Без исключений') 
        THEN 'Мастер кампаний'

      WHEN REGEXP_CONTAINS(LOWER(campaign_name),r'( |_|-|^)tc( |-|_|$)') 
        AND NOT REGEXP_CONTAINS(LOWER(campaign_name),r'Без исключений') 
        THEN 'Товарная кампания'
        
      ELSE 'Прочее'
    END