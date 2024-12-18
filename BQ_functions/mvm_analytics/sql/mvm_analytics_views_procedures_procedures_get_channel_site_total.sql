### procedures.get_channel_site_total(source,medium)
  CASE
    WHEN source LIKE '%yandex%' AND TRIM(medium) IN ('organic','referral') THEN 'Organic Yandex'
    WHEN source LIKE '%google%' AND TRIM(medium) IN ('organic') THEN 'Organic Google'
    WHEN medium = 'cpa' THEN 'CPA'
    WHEN source LIKE '%direct%' AND medium LIKE '%none%' THEN 'DIRECT'
    WHEN LOWER(medium) LIKE '%email%' THEN 'EMAIL'
    WHEN source = 'yandex' AND medium = 'cpc' THEN 'PAID'
    WHEN LOWER(source) = '2gis' OR LOWER(source) = 'yandex_maps' THEN 'PAID'
    WHEN REGEXP_CONTAINS(LOWER(source),r'regmarket|blizko|pulscen|price') AND medium = 'cpc' THEN 'PAID'
    WHEN source IN ('mt','vk','vkontakte','vkr') AND REGEXP_CONTAINS(medium,r'cpc|cpm') THEN 'PAID'
    WHEN source IN ('soloway') AND REGEXP_CONTAINS(medium,r'rs') THEN 'PAID'
    WHEN source IN ('Hybrid','hybrid') AND medium IN ('cpc','cpm') THEN 'PAID'
    ELSE 'OTHER'
  END