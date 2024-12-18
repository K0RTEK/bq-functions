### agg_procedures.get_work_placement(source_groupping, date, project, source, medium, campaign, content, term)

CASE

    ### Context
    WHEN source IN ('yandex','yandexdirect_int') AND medium IN ('cpc','af_web_banner','')
            THEN IF(source_groupping = 'placement','Яндекс Директ','context')

    ### Social
    WHEN source = 'mt' AND medium IN ('cpc','cpm','af_web_banner','')
            THEN IF(source_groupping = 'placement','MyTarget','social')

    WHEN source IN ('vk','vkontakte') AND medium IN ('cpc','cpm','af_web_banner','')
            THEN IF(source_groupping = 'placement','Vkontakte','social')

    WHEN source = 'vkr' AND medium IN ('cpc','cpm','af_web_banner','')
            THEN IF(source_groupping = 'placement','VK Reklama','social')

    ### RTG
    WHEN (REGEXP_CONTAINS(LOWER(source),r'soloway') AND medium = 'rs') OR REGEXP_CONTAINS(LOWER(source),r'adriver.ru')
            THEN IF(source_groupping = 'placement','Soloway','rtg')
    WHEN ((date BETWEEN '2023-04-01' AND '2023-08-09') OR date >= '2023-08-24') 
        AND source = 'hybrid' AND medium = 'cpc' AND NOT REGEXP_CONTAINS(LOWER(campaign),'flight')
            THEN IF(source_groupping = 'placement','Hybrid','rtg')
    WHEN date BETWEEN '2023-08-10' AND '2023-08-23'
        AND LOWER(source) = 'hybrid' AND medium = 'cpm' AND REGEXP_CONTAINS(LOWER(campaign),'mvideo|eldorado') AND NOT REGEXP_CONTAINS(LOWER(campaign),'flight')
            THEN IF(source_groupping = 'placement','Hybrid','rtg')
        -- '2023-10-26' добавили плейсмент
    WHEN LOWER(source) = 'turbotarget' AND medium = 'cpc'
            THEN IF(source_groupping = 'placement','Turbotarget','rtg')
    WHEN LOWER(source) = 'mtsdspdynrem' AND medium = 'cpm'
            THEN IF(source_groupping = 'placement','MTS','rtg')
    WHEN LOWER(source) = 'simb-ad' AND medium = 'rs'
            THEN IF(source_groupping = 'placement','SimbAd','rtg')
    WHEN LOWER(source) = 'getintentdynrem' AND medium = 'cpc'
            THEN IF(source_groupping = 'placement','Getintent','rtg')
        
    ### Prices
    WHEN REGEXP_CONTAINS(LOWER(source),r'price') AND medium = 'cpc'
            THEN IF(source_groupping = 'placement','PriceRu','prices')

    WHEN REGEXP_CONTAINS(LOWER(source),r'blizko') AND medium = 'cpc'
            THEN IF(source_groupping = 'placement','Blizko','prices')

    WHEN REGEXP_CONTAINS(LOWER(source),r'pulscen') AND medium = 'cpc'
            THEN IF(source_groupping = 'placement','Пульс Цен','prices')

    WHEN REGEXP_CONTAINS(LOWER(source),r'regmarket') AND medium = 'cpc'
            THEN IF(source_groupping = 'placement','RegmarketsRu','prices')

    ### Geoservices
    WHEN LOWER(source) = 'yandex_maps' 
            THEN IF(source_groupping = 'placement','Яндекс Карты','geoservices')

    WHEN LOWER(source) = '2gis'
            THEN IF(source_groupping = 'placement','2ГИС','geoservices')

    ### Telegram
    WHEN LOWER(source) = 'telegram' AND LOWER(medium) = 'cpc' 
            THEN IF(source_groupping = 'placement','Telegram','telegram')

    ### CPA
    WHEN REGEXP_CONTAINS(LOWER(source),r'advcake') AND medium = 'cpa'
            THEN IF(source_groupping = 'placement','Adv.Cake','cpa')
    WHEN REGEXP_CONTAINS(LOWER(source),r'tinkoff') AND medium = 'cpa'
            THEN IF(source_groupping = 'placement','Tinkoff','cpa')

    ELSE IF(source_groupping = 'placement',CONCAT(source,' / ',medium),'other')

  END