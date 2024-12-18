### agg_procedures.get_ad_id`(date,source,medium,campaign,content,term)
    CASE
      ### Яндекс Директ
      WHEN source = 'yandex' AND medium = 'cpc' 
        THEN REGEXP_EXTRACT(LOWER(content),r'aid:([0-9]+)')
      ### MyTarget
      WHEN source = 'mt' AND medium = 'cpc' AND NOT REGEXP_CONTAINS(LOWER(content),r'[^0-9]+') 
        THEN REGEXP_EXTRACT(LOWER(content),r'[0-9]+')
      WHEN source = 'mt' AND medium = 'cpc' 
        THEN REGEXP_EXTRACT(LOWER(content),r'aid.([0-9]+)')
      ### Vkontakte
      WHEN source IN ('vk','vkontakte') AND medium = 'cpc' AND NOT REGEXP_CONTAINS(LOWER(content),r'[^0-9]+') 
        THEN REGEXP_EXTRACT(LOWER(content),r'[0-9]+')
      WHEN source IN ('vk','vkontakte') AND medium = 'cpc' 
        THEN REGEXP_EXTRACT(LOWER(content),r'aid.([0-9]+)')
      ### VK Reklama
      WHEN source = 'vkr' AND medium = 'cpc' AND NOT REGEXP_CONTAINS(LOWER(content),r'[^0-9]+') 
        THEN REGEXP_EXTRACT(LOWER(content),r'[0-9]+')
      WHEN source = 'vkr' AND medium = 'cpc'
        THEN REGEXP_EXTRACT(REPLACE(LOWER(content),'-',''),r'aid.([0-9]+)')
      
      ELSE 'NaN'
    END