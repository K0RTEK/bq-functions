CASE
    WHEN REGEXP_CONTAINS(LOWER(parameter),r'vk/cpc|vka/cpc|vka/cpm|vk/lead| вкр ') THEN 'VK Ads'
    WHEN REGEXP_CONTAINS(LOWER(parameter),r'mt/cpc| мт ') THEN 'MT'
  END