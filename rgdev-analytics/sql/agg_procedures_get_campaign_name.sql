### agg_procedures.get_campaign_name(date,source,medium,campaign,content,term)
  CASE
    ### Яндекс Директ
    WHEN source = 'yd' AND medium = 'cpc'
      THEN campaign
    ELSE NULL
  END