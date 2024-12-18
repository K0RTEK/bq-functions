### agg_procedures.get_ad_group_id`(date,source,medium,campaign,content,term)
    CASE
      ### Яндекс Директ
      WHEN source = 'yandex' AND medium = 'cpc' THEN REGEXP_EXTRACT(LOWER(content),r'gid:([0-9]+)')
      ### VK Reklama
      WHEN source = 'vkr' AND medium = 'cpc' 
        THEN REGEXP_EXTRACT(REPLACE(LOWER(content),'-',''),r'gid.([0-9]+)')
        
      ELSE 'NaN'
    END