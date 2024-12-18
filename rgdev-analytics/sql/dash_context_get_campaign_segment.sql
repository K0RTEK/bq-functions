CASE
    WHEN REGEXP_CONTAINS(campaign_name,r'brand') THEN 'Бренд'
    WHEN REGEXP_CONTAINS(campaign_name,r'retargeting|remarketing|smart_banner') THEN 'Ретаргетинг'
    WHEN REGEXP_CONTAINS(campaign_name,r'cpa|autotargeting|convert|class') THEN 'Общие'
    WHEN REGEXP_CONTAINS(campaign_name,r'geo') THEN 'ГЕО'
    WHEN REGEXP_CONTAINS(campaign_name,r'competitors|konkurenty') THEN 'Конкуренты'

  END