### agg_procedures.get_campaign_name`(date,source,medium,campaign,content,term)

  CASE
      ### Яндекс Директ
      WHEN source = 'yandex' AND medium = 'cpc' AND REGEXP_CONTAINS(LOWER(campaign),r'cn:')
        THEN REGEXP_EXTRACT(campaign,r'cn:([^|]+)')
      WHEN source = 'yandex' AND medium = 'cpc' AND REGEXP_CONTAINS(LOWER(campaign),r'\|')
        THEN REGEXP_EXTRACT(campaign,r'[^|]+')
      
      ELSE campaign
    END