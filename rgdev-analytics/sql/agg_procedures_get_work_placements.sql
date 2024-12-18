### agg_procedures.get_work_placements(date,source,medium,campaign,content,term,ct_campaign_name)
  CASE 
    WHEN REGEXP_CONTAINS(LOWER(ct_campaign_name),r'яндекс.директ|yandex.direct') 
      THEN 'Яндекс Директ'
    WHEN source = 'yd' AND medium = 'cpc' 
      THEN 'Яндекс Директ'

    ELSE NULL
  END