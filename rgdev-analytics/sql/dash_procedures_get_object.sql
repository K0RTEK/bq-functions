### dash_procedures.get_object(ct_campaign_name,source,medium,campaign,content,term,campaign_name)
    CASE
      ### Михалковский
      WHEN REGEXP_CONTAINS(LOWER(ct_campaign_name),r'мих|mihalkovsky')
        THEN 'Михалковский'
      WHEN REGEXP_CONTAINS(LOWER(campaign),r'mihalkovskij') OR REGEXP_CONTAINS(LOWER(campaign_name),r'mihalkovskij')
        THEN 'Михалковский'

      ELSE 'Undefined Object'
    END