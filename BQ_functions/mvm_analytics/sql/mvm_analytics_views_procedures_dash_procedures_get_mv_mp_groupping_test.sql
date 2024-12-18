### dash_procedures.get_mv_mp_groupping(data_group,date,source,medium,campaign,content,term)
### data_group: channel, placement, placement_pf, total_paid, total_site, total_tops, flight
  CASE
    ### _non-dsh_
        WHEN REGEXP_CONTAINS(LOWER(campaign),r'_non-dsh_')
          THEN CASE
            WHEN data_group IN ('total_site','total_tops') THEN 'OTHER'
            WHEN data_group = 'placement' THEN 'non-dsh'
            WHEN data_group = 'flight' THEN 'alwayson'
            ELSE 'Other_data' END

    ### Вендорские флайты 
      ### Вендорский бюджет Контекст
        WHEN source = 'yandex' AND medium = 'cpc' AND REGEXP_CONTAINS(LOWER(campaign),r'flight') AND NOT REGEXP_CONTAINS(LOWER(campaign),r'fed') 
          THEN CASE
            WHEN data_group IN ('channel','total_paid') THEN 'Флайты Венд. бюджет'
            WHEN data_group IN ('total_site','total_tops') THEN 'PAID'
            WHEN data_group = 'flight' THEN 'Контекст'
            ELSE 'Контекст Венд. бюджет' END
      ### Вендорский бюджет Соцсети
        WHEN source IN ('mt','vk','vkontakte','vkr') AND medium IN ('cpc','cpm') AND REGEXP_CONTAINS(LOWER(campaign),r'flight') AND NOT REGEXP_CONTAINS(LOWER(campaign),r'fed')
          THEN CASE
            WHEN data_group IN ('channel','total_paid') THEN 'Флайты Венд. бюджет'
            WHEN data_group IN ('total_site','total_tops') THEN 'PAID'
            WHEN data_group = 'flight' THEN 'Соцсети'
            ELSE 'Соцсети Венд. бюджет' END

    ### Нерезиденты
        WHEN source IN ('mt','vkr') AND medium = 'cpc' AND REGEXP_CONTAINS(LOWER(campaign),r'rezedent')
          THEN CASE
            WHEN data_group IN ('total_site','total_tops') THEN 'OTHER'
            WHEN data_group = 'placement' THEN 'Нерезиденты'
            WHEN data_group = 'flight' THEN 'alwayson'
            ELSE 'Other_data' END
          
    ### Контекст
      ### Исключение _vacansii_
        WHEN source = 'yandex' AND medium = 'cpc' AND REGEXP_CONTAINS(LOWER(campaign),r'_vacansii_') 
          THEN CASE
            WHEN data_group IN ('total_site','total_tops') THEN 'OTHER'
            WHEN data_group = 'placement' THEN 'Вакансии'
            WHEN data_group = 'flight' THEN 'alwayson'
            ELSE 'Other_data' END
      ### Федеральный бюджет
        WHEN source = 'yandex' AND medium = 'cpc' AND REGEXP_CONTAINS(LOWER(campaign),r'flight') AND REGEXP_CONTAINS(LOWER(campaign),r'fed') 
          THEN CASE
            WHEN data_group IN ('channel','total_paid') THEN 'Контекст'
            WHEN data_group IN ('total_site','total_tops') THEN 'PAID'
            WHEN data_group = 'flight' THEN 'Контекст'
            ELSE 'Яндекс Директ Фед. бюджет' END
      ### Докаты IProspect (Бренд)
        WHEN source = 'yandex' AND medium = 'cpc' AND NOT REGEXP_CONTAINS(LOWER(campaign),r'mg_') AND REGEXP_CONTAINS(LOWER(campaign),r'_image_name') 
          THEN CASE
            WHEN data_group IN ('channel','total_paid') THEN 'Докаты' 
            WHEN data_group = 'placement' THEN 'Докаты (iProspect)'
            WHEN data_group IN ('total_site','total_tops') THEN 'PAID'
            WHEN data_group = 'flight' THEN 'alwayson'
            ELSE 'Докаты IProspect (Бренд)' END
      ### Докаты IProspect (Небренд)
        WHEN source = 'yandex' AND medium = 'cpc' AND NOT REGEXP_CONTAINS(LOWER(campaign),r'mg_') AND NOT REGEXP_CONTAINS(LOWER(campaign),r'_image_name') 
          THEN CASE
            WHEN data_group IN ('channel','total_paid') THEN 'Докаты' 
            WHEN data_group = 'placement' THEN 'Докаты (iProspect)'
            WHEN data_group IN ('total_site','total_tops') THEN 'PAID'
            WHEN data_group = 'flight' THEN 'alwayson'
            ELSE 'Докаты IProspect (Небренд)' END
            
######### Новая группировка План-Факт с 1 января 2024
###### ПОСЛЕ 2024-01-01
 ### 'М.Видео | РСЯ'
 WHEN source = 'yandex' AND medium = 'cpc' AND REGEXP_CONTAINS(LOWER(campaign),r'_s_|brand_s') AND NOT REGEXP_CONTAINS(LOWER(campaign),r'smartbanners|_rem')
 THEN CASE
 WHEN data_group IN ('channel','total_paid') THEN 'Контекст'
 WHEN data_group = 'placement' THEN 'Яндекс Директ Небренд'
 WHEN data_group IN ('total_site','total_tops') THEN 'PAID'
 WHEN data_group = 'flight' THEN 'alwayson'
 ELSE 'М.Видео | РСЯ' END
 ### 'М.Видео | Бренд'
 WHEN source = 'yandex' AND medium = 'cpc' AND REGEXP_CONTAINS(LOWER(campaign),r'_image_name|_brand') AND NOT REGEXP_CONTAINS(LOWER(campaign),r'_s_')
 THEN CASE
 WHEN data_group IN ('channel','total_paid') THEN 'Контекст'
 WHEN data_group = 'placement' THEN 'Яндекс Директ Бренд'
 WHEN data_group IN ('total_site','total_tops') THEN 'PAID'
 WHEN data_group = 'flight' THEN 'alwayson'
 ELSE 'М.Видео | Бренд' END
 ### 'М.Видео | DSA'
 WHEN source = 'yandex' AND medium = 'cpc' AND REGEXP_CONTAINS(LOWER(campaign),r'_dsa|_dsa-|shopping')
 THEN CASE
 WHEN data_group IN ('channel','total_paid') THEN 'Контекст'
 WHEN data_group = 'placement' THEN 'Яндекс Директ Небренд'
 WHEN data_group IN ('total_site','total_tops') THEN 'PAID'
 WHEN data_group = 'flight' THEN 'alwayson'
 ELSE 'М.Видео | DSA' END
 ### 'М.Видео | API (K50)'
 WHEN source = 'yandex' AND medium = 'cpc' AND REGEXP_CONTAINS(LOWER(campaign),r'_api_')
 THEN CASE
 WHEN data_group IN ('channel','total_paid') THEN 'Контекст'
 WHEN data_group = 'placement' THEN 'Яндекс Директ Небренд'
 WHEN data_group IN ('total_site','total_tops') THEN 'PAID'
 WHEN data_group = 'flight' THEN 'alwayson'
 ELSE 'М.Видео | API (K50)' END
 ### 'М.Видео | Смарт баннеры + Ремаркетинг'
 WHEN source = 'yandex' AND medium = 'cpc' AND REGEXP_CONTAINS(LOWER(campaign),r'smartbanner|_rem')
 THEN CASE
 WHEN data_group IN ('channel','total_paid') THEN 'Контекст'
 WHEN data_group = 'placement' THEN 'Яндекс Директ Небренд'
 WHEN data_group IN ('total_site','total_tops') THEN 'PAID'
 WHEN data_group = 'flight' THEN 'alwayson'
 ELSE 'М.Видео | Смарт баннеры + Ремаркетинг' END
 ### 'М.Видео | Товарные кампании'
 WHEN source = 'yandex' AND medium = 'cpc' AND REGEXP_CONTAINS(LOWER(campaign),r'_tk_')
 THEN CASE
 WHEN data_group IN ('channel','total_paid') THEN 'Контекст'
 WHEN data_group = 'placement' THEN 'Яндекс Директ Небренд'
 WHEN data_group IN ('total_site','total_tops') THEN 'PAID'
 WHEN data_group = 'flight' THEN 'alwayson'
 ELSE 'М.Видео | Товарные кампании' END
 ### 'М.Видео | Категорийные + Кат-вендорные'
 WHEN source = 'yandex' AND medium = 'cpc' AND REGEXP_CONTAINS(LOWER(campaign),r'_p_') AND REGEXP_CONTAINS(LOWER(campaign),r'_cat-ven_|_cat_|_category_|_hand_|autotarget|keywords|compet')
 THEN CASE
 WHEN data_group IN ('channel','total_paid') THEN 'Контекст'
 WHEN data_group = 'placement' THEN 'Яндекс Директ Небренд'
 WHEN data_group IN ('total_site','total_tops') THEN 'PAID'
 WHEN data_group = 'flight' THEN 'alwayson'
 ELSE 'Яндекс Категорийные РК (модельные+катвенд) + Автотаргет' END
 ### 'М.Видео | Остальное'
 WHEN source = 'yandex' AND medium = 'cpc'
 THEN CASE
 WHEN data_group IN ('channel','total_paid') THEN 'Контекст'
 WHEN data_group = 'placement' THEN 'Яндекс Директ Небренд'
 WHEN data_group IN ('total_site','total_tops') THEN 'PAID'
 WHEN data_group = 'flight' THEN 'alwayson'
 ELSE 'М.Видео | Остальное' END

    ### Соцсети
      ### Исключение leadads
        WHEN source IN ('mt','vk','vkontakte','vkr') AND medium IN ('cpc','cpm') AND REGEXP_CONTAINS(LOWER(campaign),r'leadads') 
          THEN CASE
            WHEN data_group IN ('total_site','total_tops') THEN 'OTHER'
            WHEN data_group = 'placement' THEN 'Вакансии'
            WHEN data_group = 'flight' THEN 'alwayson'
            ELSE 'Other_data' END
      ### Федеральный бюджет
        WHEN source IN ('mt','vk','vkontakte','vkr') AND medium IN ('cpc','cpm') AND REGEXP_CONTAINS(LOWER(campaign),r'flight') AND REGEXP_CONTAINS(LOWER(campaign),r'fed') 
        THEN CASE
            WHEN data_group IN ('channel','total_paid') THEN 'Соцсети'
            WHEN data_group IN ('total_site','total_tops') THEN 'PAID'
            WHEN data_group = 'flight' THEN 'Соцсети'
            ELSE 'Соцсети Фед. бюджет' END
      ### Соцсети Media
        WHEN source IN ('mt','vk','vkontakte','vkr') AND medium IN ('cpc','cpm') AND REGEXP_CONTAINS(LOWER(campaign),r'_cpm_ny-sale23')
          THEN CASE
            WHEN data_group IN ('channel','total_paid') THEN 'Соцсети'
            WHEN data_group = 'placement' THEN 'VK Reklama'
            WHEN data_group IN ('total_site','total_tops') THEN 'PAID'
            WHEN data_group = 'flight' THEN 'alwayson'
            ELSE 'Соцсети Media' END
      ### Докаты
        WHEN source IN ('mt','vk','vkontakte','vkr') AND medium IN ('cpc','cpm') AND NOT REGEXP_CONTAINS(LOWER(campaign),r'^mg|leadads')
          THEN CASE
            WHEN data_group IN ('total_site','total_tops') THEN 'PAID'
            WHEN data_group = 'flight' THEN 'alwayson'
            ELSE 'Докаты' END
      ### MyTarget
        WHEN source = 'mt' AND medium IN ('cpc','cpm') AND NOT REGEXP_CONTAINS(LOWER(campaign),r'leadads')
          THEN CASE
            WHEN data_group IN ('channel','total_paid') THEN 'Соцсети'
            WHEN data_group IN ('total_site','total_tops') THEN 'PAID'
            WHEN data_group = 'flight' THEN 'alwayson'
            ELSE 'MyTarget' END
      ### Vkontakte
        WHEN source IN ('vk','vkontakte') AND medium IN ('cpc','cpm') AND NOT REGEXP_CONTAINS(LOWER(campaign),r'leadads')
          THEN CASE
            WHEN data_group IN ('channel','total_paid') THEN 'Соцсети'
            WHEN data_group IN ('total_site','total_tops') THEN 'PAID'
            WHEN data_group = 'flight' THEN 'alwayson'
            ELSE 'Vkontakte' END
      ### VK Reklama
        WHEN source = 'vkr' AND medium IN ('cpc','cpm') AND NOT REGEXP_CONTAINS(LOWER(campaign),r'leadads')
          THEN CASE
            WHEN data_group IN ('channel','total_paid') THEN 'Соцсети'
            WHEN data_group IN ('total_site','total_tops') THEN 'PAID'
            WHEN data_group = 'flight' THEN 'alwayson'
            ELSE 'VK Reklama' END
        WHEN source = 'vk_ads' AND medium = 'cpc' AND NOT REGEXP_CONTAINS(LOWER(campaign),r'leadads') AND date BETWEEN '2023-08-23' AND '2023-08-29'
          THEN CASE
            WHEN data_group IN ('channel','total_paid') THEN 'Соцсети'
            WHEN data_group IN ('total_site','total_tops') THEN 'PAID'
            WHEN data_group = 'flight' THEN 'alwayson'
            ELSE 'VK Reklama' END

    ### Ретаргетинг
      ### Докаты
        -- WHEN (
        --     ((REGEXP_CONTAINS(LOWER(source),r'soloway') AND medium = 'rs') OR REGEXP_CONTAINS(LOWER(source),r'adriver.ru'))
        --     OR (LOWER(source) = 'hybrid' AND medium IN ('cpc','cpm'))
        --     )
        --   AND NOT REGEXP_CONTAINS(LOWER(campaign),r'flight')
        --     THEN CASE
        --       WHEN data_group IN ('total_site','total_tops') THEN 'PAID'
        --       ELSE 'Докаты' END
      ### Soloway
        WHEN (REGEXP_CONTAINS(LOWER(source),r'soloway') AND medium = 'rs') OR REGEXP_CONTAINS(LOWER(source),r'adriver.ru')
          THEN CASE
            WHEN data_group IN ('channel','total_paid') THEN 'Ретаргетинг'
            WHEN data_group IN ('total_site','total_tops') THEN 'PAID'
            WHEN data_group = 'flight' THEN 'alwayson'
            ELSE 'Soloway' END
      ### Hybrid
      WHEN ((date BETWEEN '2023-04-01' AND '2023-08-09') OR date >= '2023-08-24') 
        AND LOWER(source) = 'hybrid' AND medium = 'cpc'
        AND NOT REGEXP_CONTAINS(LOWER(campaign),'flight') 
          THEN CASE
            WHEN data_group IN ('channel','total_paid') THEN 'Ретаргетинг'
            WHEN data_group IN ('total_site','total_tops') THEN 'PAID'
            WHEN data_group = 'flight' THEN 'alwayson'
            ELSE 'Hybrid' END
      WHEN date BETWEEN '2023-08-10' AND '2023-08-23'
        AND LOWER(source) = 'hybrid' AND medium = 'cpm'
        AND REGEXP_CONTAINS(LOWER(campaign),'mvideo')
        AND NOT REGEXP_CONTAINS(LOWER(campaign),'flight') 
          THEN CASE
            WHEN data_group IN ('channel','total_paid') THEN 'Ретаргетинг'
            WHEN data_group IN ('total_site','total_tops') THEN 'PAID'
            WHEN data_group = 'flight' THEN 'alwayson'
            ELSE 'Hybrid' END
      ### МТС
        WHEN (REGEXP_CONTAINS(LOWER(source),r'mtsdspdynrem') AND medium = 'cpm')
          THEN CASE
            WHEN data_group IN ('channel','total_paid') THEN 'Ретаргетинг'
            WHEN data_group IN ('total_site','total_tops') THEN 'PAID'
            WHEN data_group = 'flight' THEN 'alwayson'
            ELSE 'МТС' END
      ### SimbAd
        WHEN LOWER(source) = 'simb-ad' AND medium = 'rs'
          THEN CASE
            WHEN data_group IN ('channel','total_paid') THEN 'Ретаргетинг'
            WHEN data_group IN ('total_site','total_tops') THEN 'PAID'
            WHEN data_group = 'flight' THEN 'alwayson'
            ELSE 'SimbAd' END
          
    ### Прайс-площадки
      ### Докаты
        WHEN REGEXP_CONTAINS(LOWER(source),r'price|blizko|pulscen|regmarket') AND medium = 'cpc' AND NOT REGEXP_CONTAINS(LOWER(campaign),r'^mg')
          THEN CASE
            WHEN data_group IN ('total_site','total_tops') THEN 'PAID'
            WHEN data_group = 'flight' THEN 'alwayson'
            ELSE 'Докаты' END
      ### PriceRu
        WHEN REGEXP_CONTAINS(LOWER(source),r'price') AND medium = 'cpc'
          THEN CASE
            WHEN data_group IN ('channel','total_paid') THEN 'Прайс-площадки'
            WHEN data_group IN ('total_site','total_tops') THEN 'PAID'
            WHEN data_group = 'flight' THEN 'alwayson'
            ELSE 'PriceRu' END
      ### Blizko
        WHEN REGEXP_CONTAINS(LOWER(source),r'blizko') AND medium = 'cpc'
          THEN CASE
            WHEN data_group IN ('channel','total_paid') THEN 'Прайс-площадки'
            WHEN data_group IN ('total_site','total_tops') THEN 'PAID'
            WHEN data_group = 'flight' THEN 'alwayson'
            ELSE 'Blizko' END
      ### Пульс Цен
        WHEN REGEXP_CONTAINS(LOWER(source),r'pulscen') AND medium = 'cpc'
          THEN CASE
            WHEN data_group IN ('channel','total_paid') THEN 'Прайс-площадки'
            WHEN data_group IN ('total_site','total_tops') THEN 'PAID'
            WHEN data_group = 'flight' THEN 'alwayson'
            ELSE 'Пульс Цен' END
      ### RegmarketsRu
        WHEN REGEXP_CONTAINS(LOWER(source),r'regmarket') AND medium = 'cpc'
          THEN CASE
            WHEN data_group IN ('channel','total_paid') THEN 'Прайс-площадки'
            WHEN data_group IN ('total_site','total_tops') THEN 'PAID'
            WHEN data_group = 'flight' THEN 'alwayson'
            ELSE 'RegmarketsRu' END

    ### Геосервисы
      ### Докаты
        WHEN LOWER(source) IN ('yandex_maps','2gis') AND medium IN ('cpc','cpm') AND NOT REGEXP_CONTAINS(LOWER(campaign),r'^mg')
          THEN CASE
            WHEN data_group IN ('total_site','total_tops') THEN 'PAID'
            WHEN data_group = 'total_tops' THEN 'PAID'
            WHEN data_group = 'flight' THEN 'alwayson'
            ELSE 'Докаты' END
      ### Яндекс Карты
        WHEN LOWER(source) = 'yandex_maps' 
          THEN CASE
            WHEN data_group IN ('channel','total_paid') THEN 'Геосервисы'
            WHEN data_group = 'total_site' THEN 'PAID'
            WHEN data_group = 'total_tops' THEN 'PAID'
            WHEN data_group = 'flight' THEN 'alwayson'
            ELSE 'Яндекс Карты' END
      ### 2ГИС
        WHEN LOWER(source) = '2gis'
          THEN CASE
            WHEN data_group IN ('channel','total_paid') THEN 'Геосервисы'
            WHEN data_group = 'total_site' THEN 'PAID'
            WHEN data_group = 'total_tops' THEN 'PAID'
            WHEN data_group = 'flight' THEN 'alwayson'
            ELSE '2ГИС' END

    ### Telegram
      ### Telegram
        WHEN LOWER(source) = 'telegram' AND LOWER(medium) = 'cpc' 
          THEN CASE
            WHEN data_group IN ('channel','total_paid') THEN 'Telegram'
            WHEN data_group IN ('total_site','total_tops') THEN 'PAID'
            WHEN data_group = 'flight' THEN 'alwayson'
            ELSE 'Telegram' END

    ### CPA
      ### Advcake
        WHEN REGEXP_CONTAINS(LOWER(source),r'advcake') AND medium = 'cpa'
          THEN CASE
            WHEN data_group IN ('channel','placement_pf','total_paid') THEN 'Other_data'
            WHEN data_group = 'placement' THEN 'Advcake'
            WHEN data_group = 'flight' THEN 'alwayson'
            ELSE 'CPA' END
      ### Tinkoff
        WHEN REGEXP_CONTAINS(LOWER(source),r'tinkoff') AND medium = 'cpa'
          THEN CASE
            WHEN data_group IN ('channel','placement_pf','total_paid') THEN 'Other_data'
            WHEN data_group = 'placement' THEN 'Tinkoff'
            WHEN data_group = 'flight' THEN 'alwayson'
            ELSE 'CPA' END

    ### Organic  
      ### Organic Yandex 
        WHEN source LIKE '%yandex%' AND TRIM(medium) IN ('organic','referral') 
          THEN CASE
            WHEN data_group IN ('channel','placement_pf','total_paid') THEN 'Other_data'
            WHEN data_group = 'total_tops' THEN 'ORGANIC'
            WHEN data_group = 'flight' THEN 'alwayson'
            ELSE 'Organic Yandex' END
      ### Organic Google
        WHEN source LIKE '%google%' AND TRIM(medium) IN ('organic') 
          THEN CASE
            WHEN data_group IN ('channel','placement_pf','total_paid') THEN 'Other_data'
            WHEN data_group = 'total_tops' THEN 'ORGANIC'
            WHEN data_group = 'flight' THEN 'alwayson'
            ELSE 'Organic Google' END
      
    ### Direct
        WHEN source LIKE '%direct%' AND medium LIKE '%none%' 
          THEN CASE
            WHEN data_group IN ('channel','placement_pf','placement','total_paid') THEN 'Other_data'
            WHEN data_group = 'flight' THEN 'alwayson'
            ELSE 'DIRECT' END

    ### Email
        WHEN LOWER(medium) LIKE '%email%' 
          THEN CASE
            WHEN data_group IN ('channel','placement_pf','placement','total_paid') THEN 'Other_data'
            WHEN data_group = 'flight' THEN 'alwayson'
            ELSE 'EMAIL' END

    ELSE CASE
            WHEN data_group IN ('total_tops','total_site') THEN 'OTHER'
            WHEN data_group = 'flight' THEN 'alwayson'
            ELSE 'Other_data' END

  END