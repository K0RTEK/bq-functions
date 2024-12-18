### agg_procedures.get_campaign_id`(date,source,medium,campaign,content,term)

  CASE
      ### Яндекс Директ
      WHEN source = 'yandex' AND medium = 'cpc' AND REGEXP_CONTAINS(LOWER(content),r'cid:')
        THEN REGEXP_EXTRACT(LOWER(content),r'cid:([0-9]+)')
      WHEN source = 'yandex' AND medium = 'cpc' AND REGEXP_CONTAINS(LOWER(campaign),r'cid:')
        THEN REGEXP_EXTRACT(LOWER(campaign),r'cid:([0-9]+)')
      WHEN source = 'yandex' AND medium = 'cpc' AND REGEXP_CONTAINS(LOWER(campaign),r'\|[0-9]{5,}')
        THEN REGEXP_EXTRACT(LOWER(campaign),r'\|([0-9]{5,})')
      ### Mytarget
      WHEN source = 'mt' AND medium = 'cpc' 
        THEN REGEXP_EXTRACT(LOWER(content),r'cid.([0-9]+)')
      ### Vkontakte
      WHEN source IN ('vk','vkontakte') AND medium = 'cpc' 
        THEN REGEXP_EXTRACT(LOWER(content),r'cid.([0-9]+)')
      
      ELSE 'NaN'
    END