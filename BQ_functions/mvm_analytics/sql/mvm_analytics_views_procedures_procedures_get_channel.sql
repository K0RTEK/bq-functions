### procedures.get_channel(source,medium)
  CASE
    WHEN medium = 'organic' THEN 'ORGANIC'
    WHEN source = 'yandex' AND medium = 'referral' THEN 'ORGANIC'
    WHEN medium = 'cpa' THEN 'CPA'
    WHEN medium = '(none)' THEN 'DIRECT'
    WHEN LOWER(medium) LIKE '%email%' THEN 'EMAIL'
    WHEN source = 'yandex' AND medium = 'cpc' THEN 'PAID'
    WHEN LOWER(source) = '2gis' OR LOWER(source) = 'yandex_maps' THEN 'GEO'
    WHEN REGEXP_CONTAINS(LOWER(source),r'regmarket|blizko|pulscen|price') AND medium = 'cpc' THEN 'PAID'
    WHEN source IN ('mt','vk','vkontakte','vkr') AND REGEXP_CONTAINS(medium,r'cpc|cpm') THEN 'PAID'
    WHEN source IN ('soloway') AND medium = 'rs' THEN 'PAID'
    WHEN source IN ('Hybrid','hybrid') AND medium IN ('cpc','cpm') THEN 'PAID'
    ELSE 'OTHER'
  END