### dash_procedures.get_eldo_mp_groupping(data_group,date,source,medium,campaign,content,term)
### data_group: channel, placement, placement_pf, total_paid, total_site, total_tops, flight
  CASE
    ### _non-dsh_
        WHEN REGEXP_CONTAINS(LOWER(campaign),r'_non-dsh_')
          THEN CASE
            WHEN data_group IN ('total_site','total_tops') THEN 'OTHER'
            WHEN data_group = 'placement' THEN 'non-dsh'
            WHEN data_group = 'flight' THEN 'alwayson'
            ELSE 'Other_data' END

    ### Mobile исключение
        WHEN REGEXP_CONTAINS(LOWER(campaign),r'_ios|_aos_')
          THEN CASE
            WHEN data_group IN ('total_site','total_tops') THEN 'OTHER'
            WHEN data_group = 'placement' THEN 'non-dsh'
            WHEN data_group = 'flight' THEN 'alwayson'
            ELSE 'Other_data' END
            
    ### Вендорские флайты
      ### Вендорский бюджет Контекст
        WHEN source = 'yandex' AND medium = 'cpc' AND REGEXP_CONTAINS(LOWER(campaign),r'flight') AND REGEXP_CONTAINS(LOWER(campaign),r'mg_') AND NOT REGEXP_CONTAINS(LOWER(campaign),r'fed')
          THEN CASE
            WHEN data_group IN ('channel','total_paid') THEN 'Флайты Венд. бюджет'
            WHEN data_group IN ('total_site','total_tops') THEN 'PAID'
            WHEN data_group = 'flight' THEN 'Контекст'
            ELSE 'Контекст Венд. бюджет' END
      ### Вендорский бюджет Соцсети
        WHEN source IN ('mt','vk','vkontakte','vkr') AND medium IN ('cpc','cpm') AND REGEXP_CONTAINS(LOWER(campaign),r'flight') AND REGEXP_CONTAINS(LOWER(campaign),r'mg_') AND NOT REGEXP_CONTAINS(LOWER(campaign),r'fed')
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
         AND REGEXP_CONTAINS(LOWER(campaign),r'mg_') 
        THEN CASE
            WHEN data_group IN ('channel','total_paid') THEN 'Контекст'
            WHEN data_group IN ('total_site','total_tops') THEN 'PAID'
            WHEN data_group = 'flight' THEN 'Контекст'
            ELSE 'Эльдорадо | Фед. бюджет' END
      ### Докаты (iProspect) Бренд
        WHEN source = 'yandex' AND medium = 'cpc' AND REGEXP_CONTAINS(LOWER(campaign),r'ipr_') AND REGEXP_CONTAINS(LOWER(campaign),r'_image_name') 
          THEN CASE
            WHEN data_group IN ('channel','total_paid') THEN 'Докаты' 
            WHEN data_group = 'placement' THEN 'Докаты (iProspect)'
            WHEN data_group IN ('total_site','total_tops') THEN 'PAID'
            WHEN data_group = 'flight' THEN 'alwayson'
            ELSE 'Докаты IProspect (Бренд)' END
      ### Докаты (iProspect) НЕ Бренд
        WHEN source = 'yandex' AND medium = 'cpc' AND REGEXP_CONTAINS(LOWER(campaign),r'ipr') AND NOT REGEXP_CONTAINS(LOWER(campaign),r'_image_name') 
          THEN CASE
            WHEN data_group IN ('channel','total_paid') THEN 'Докаты' 
            WHEN data_group = 'placement' THEN 'Докаты (iProspect)'
            WHEN data_group IN ('total_site','total_tops') THEN 'PAID'
            WHEN data_group = 'flight' THEN 'alwayson'
            ELSE 'Докаты IProspect (Небренд)' END
      ### Докаты Другое 
        WHEN source = 'yandex' AND medium = 'cpc' AND NOT REGEXP_CONTAINS(LOWER(campaign),r'mg_')  
          THEN CASE 
            WHEN data_group IN ('total_site','total_tops') THEN 'PAID'  
            WHEN data_group = 'flight' THEN 'alwayson'  
            ELSE 'Докаты' END

      ###### ПОСЛЕ 2023-10-01
      ### Эльдорадо | РСЯ
        WHEN date >= '2023-10-01' AND source = 'yandex' AND medium = 'cpc' AND REGEXP_CONTAINS(LOWER(campaign),r'_s_') AND NOT REGEXP_CONTAINS(LOWER(campaign),r'smartbanners|_rem') 
        THEN CASE
            WHEN data_group IN ('channel','total_paid') THEN 'Контекст'
            WHEN data_group = 'placement' THEN 'Яндекс Директ Небренд'
            WHEN data_group IN ('total_site','total_tops') THEN 'PAID'
            WHEN data_group = 'flight' THEN 'alwayson'
            ELSE 'Эльдорадо | РСЯ' END
      ### Эльдорадо | Бренд
        WHEN date >= '2023-10-01' AND source = 'yandex' AND medium = 'cpc' AND REGEXP_CONTAINS(LOWER(campaign),r'_image_') AND REGEXP_CONTAINS(LOWER(campaign),r'_p_')
          THEN CASE
            WHEN data_group IN ('channel','total_paid') THEN 'Контекст' 
            WHEN data_group = 'placement' THEN 'Яндекс Директ Бренд'
            WHEN data_group IN ('total_site','total_tops') THEN 'PAID'
            WHEN data_group = 'flight' THEN 'alwayson'
            ELSE 'Эльдорадо | Бренд' END
      ### Эльдорадо | Автотаргетинг+МК
        WHEN date >= '2023-10-01' AND source = 'yandex' AND medium = 'cpc' AND REGEXP_CONTAINS(LOWER(campaign),r'_autotarget_|_mc_') 
          THEN CASE
            WHEN data_group IN ('channel','total_paid') THEN 'Контекст' 
            WHEN data_group = 'placement' THEN 'Яндекс Директ Небренд'
            WHEN data_group IN ('total_site','total_tops') THEN 'PAID'
            WHEN data_group = 'flight' THEN 'alwayson'
            ELSE 'Эльдорадо | Автотаргетинг+МК' END
      ### Эльдорадо | DSA
        WHEN date >= '2023-10-01' AND source = 'yandex' AND medium = 'cpc' AND REGEXP_CONTAINS(LOWER(campaign),r'_dsa|shopping') 
          THEN CASE
            WHEN data_group IN ('channel','total_paid') THEN 'Контекст' 
            WHEN data_group = 'placement' THEN 'Яндекс Директ Небренд'
            WHEN data_group IN ('total_site','total_tops') THEN 'PAID'
            WHEN data_group = 'flight' THEN 'alwayson'
            ELSE 'Эльдорадо | DSA' END
      ### Эльдорадо | Смарт-баннеры + Ремаркетинг
      ### Исключили _competitors_ 26.12
        WHEN date >= '2023-10-01' AND source = 'yandex' AND medium = 'cpc' AND REGEXP_CONTAINS(LOWER(campaign),r'smartbanner|_rem') AND NOT REGEXP_CONTAINS(LOWER(campaign),r'_competitors_')
          THEN CASE
            WHEN data_group IN ('channel','total_paid') THEN 'Контекст' 
            WHEN data_group = 'placement' THEN 'Яндекс Директ Небренд'
            WHEN data_group IN ('total_site','total_tops') THEN 'PAID'
            WHEN data_group = 'flight' THEN 'alwayson'
            ELSE 'Эльдорадо | Смарт-баннеры + Ремаркетинг' END
      ### Эльдорадо | Товарная РК
        WHEN date >= '2023-10-01' AND source = 'yandex' AND medium = 'cpc' AND REGEXP_CONTAINS(LOWER(campaign),r'_tk_') 
          THEN CASE
            WHEN data_group IN ('channel','total_paid') THEN 'Контекст' 
            WHEN data_group = 'placement' THEN 'Яндекс Директ Небренд'
            WHEN data_group IN ('total_site','total_tops') THEN 'PAID'
            WHEN data_group = 'flight' THEN 'alwayson'
            ELSE 'Эльдорадо | Товарная РК' END
      ### Эльдорадо | API (К50)
        WHEN date >= '2023-10-01' AND source = 'yandex' AND medium = 'cpc' AND REGEXP_CONTAINS(LOWER(campaign),r'_api_') 
          THEN CASE
            WHEN data_group IN ('channel','total_paid') THEN 'Контекст' 
            WHEN data_group = 'placement' THEN 'Яндекс Директ Небренд'
            WHEN data_group IN ('total_site','total_tops') THEN 'PAID'
            WHEN data_group = 'flight' THEN 'alwayson'
            ELSE 'Эльдорадо | API (К50)' END
      ### Эльдорадо | Категорийные + Кат-вендорные
        WHEN date >= '2023-10-01' AND source = 'yandex' AND medium = 'cpc' AND REGEXP_CONTAINS(LOWER(campaign),r'category|cat-ven') 
          THEN CASE
            WHEN data_group IN ('channel','total_paid') THEN 'Контекст' 
            WHEN data_group = 'placement' THEN 'Яндекс Директ Небренд'
            WHEN data_group IN ('total_site','total_tops') THEN 'PAID'
            WHEN data_group = 'flight' THEN 'alwayson'
            ELSE 'Эльдорадо | Категорийные + Кат-вендорные' END
      ### Эльдорадо | Конкуренты
        WHEN date >= '2023-10-01' AND source = 'yandex' AND medium = 'cpc' AND REGEXP_CONTAINS(LOWER(campaign),r'competitors') 
          THEN CASE
            WHEN data_group IN ('channel','total_paid') THEN 'Контекст' 
            WHEN data_group = 'placement' THEN 'Яндекс Директ Небренд'
            WHEN data_group IN ('total_site','total_tops') THEN 'PAID'
            WHEN data_group = 'flight' THEN 'alwayson'
            ELSE 'Эльдорадо | Конкуренты' END
      ### Эльдорадо | Модельные ручные
      ### model_hand заменили на model_h
        WHEN date >= '2023-10-01' AND source = 'yandex' AND medium = 'cpc' AND REGEXP_CONTAINS(LOWER(campaign),r'model_h|model_p') 
          THEN CASE
            WHEN data_group IN ('channel','total_paid') THEN 'Контекст' 
            WHEN data_group = 'placement' THEN 'Яндекс Директ Небренд'
            WHEN data_group IN ('total_site','total_tops') THEN 'PAID'
            WHEN data_group = 'flight' THEN 'alwayson'
            ELSE 'Эльдорадо | Модельные ручные' END
      ### Эльдорадо | ЕПК
        WHEN date >= '2023-10-01' AND source = 'yandex' AND medium = 'cpc' AND REGEXP_CONTAINS(LOWER(campaign),r'_united_|_epk_') 
          THEN CASE
            WHEN data_group IN ('channel','total_paid') THEN 'Контекст' 
            WHEN data_group = 'placement' THEN 'Яндекс Директ Небренд'
            WHEN data_group IN ('total_site','total_tops') THEN 'PAID'
            WHEN data_group = 'flight' THEN 'alwayson'
            ELSE 'Эльдорадо | ЕПК' END

      ###### ДО 2023-10-01
      ### Яндекс Директ Бренд
        WHEN date < '2023-10-01' AND source = 'yandex' AND medium = 'cpc' AND REGEXP_CONTAINS(LOWER(campaign),r'_image_') 
          THEN CASE
            WHEN data_group IN ('channel','total_paid') THEN 'Контекст' 
            WHEN data_group = 'placement' THEN 'Яндекс Директ Бренд'
            WHEN data_group IN ('total_site','total_tops') THEN 'PAID'
            WHEN data_group = 'flight' THEN 'alwayson'
            ELSE 'Яндекс Бренд' END
      ### Яндекс Автотаргетинг
        WHEN date < '2023-10-01' AND source = 'yandex' AND medium = 'cpc' AND REGEXP_CONTAINS(LOWER(campaign),r'_autotarget_') 
          THEN CASE
            WHEN data_group IN ('channel','total_paid') THEN 'Контекст' 
            WHEN data_group = 'placement' THEN 'Яндекс Директ Небренд'
            WHEN data_group IN ('total_site','total_tops') THEN 'PAID'
            WHEN data_group = 'flight' THEN 'alwayson'
            ELSE 'Яндекс Автотаргетинг' END
      ### Яндекс DSA
        WHEN date < '2023-10-01' AND source = 'yandex' AND medium = 'cpc' AND REGEXP_CONTAINS(LOWER(campaign),r'_dsa|_dsa-|shopping') 
          THEN CASE
            WHEN data_group IN ('channel','total_paid') THEN 'Контекст' 
            WHEN data_group = 'placement' THEN 'Яндекс Директ Небренд'
            WHEN data_group IN ('total_site','total_tops') THEN 'PAID'
            WHEN data_group = 'flight' THEN 'alwayson'
            ELSE 'Яндекс DSA' END
      ### Яндекс Смарт-баннеры
        WHEN date < '2023-10-01' AND source = 'yandex' AND medium = 'cpc' AND REGEXP_CONTAINS(LOWER(campaign),r'smartbanner') 
          THEN CASE
            WHEN data_group IN ('channel','total_paid') THEN 'Контекст' 
            WHEN data_group = 'placement' THEN 'Яндекс Директ Небренд'
            WHEN data_group IN ('total_site','total_tops') THEN 'PAID'
            WHEN data_group = 'flight' THEN 'alwayson'
            ELSE 'Яндекс Смартбаннеры' END
      ### Яндекс Товарная РК
        WHEN date < '2023-10-01' AND source = 'yandex' AND medium = 'cpc' AND REGEXP_CONTAINS(LOWER(campaign),r'_tk_') 
          THEN CASE
            WHEN data_group IN ('channel','total_paid') THEN 'Контекст' 
            WHEN data_group = 'placement' THEN 'Яндекс Директ Небренд'
            WHEN data_group IN ('total_site','total_tops') THEN 'PAID'
            WHEN data_group = 'flight' THEN 'alwayson'
            ELSE 'Яндекс Товарная РК' END
      ### Яндекс РСЯ (Категорийная + Конкуренты)
        WHEN date < '2023-10-01' AND source = 'yandex' AND medium = 'cpc' AND NOT REGEXP_CONTAINS(LOWER(campaign),r'_smartbanners_|_rem_|_rem-') 
          AND REGEXP_CONTAINS(LOWER(campaign),r'_rsya_s_') 
          THEN CASE
            WHEN data_group IN ('channel','total_paid') THEN 'Контекст' 
            WHEN data_group = 'placement' THEN 'Яндекс Директ Небренд'
            WHEN data_group IN ('total_site','total_tops') THEN 'PAID'
            WHEN data_group = 'flight' THEN 'alwayson'
            ELSE 'Яндекс РСЯ (Категорийная + Конкуренты)' END
      ### Яндекс Ремаркетинг
        WHEN date < '2023-10-01' AND source = 'yandex' AND medium = 'cpc' AND REGEXP_CONTAINS(LOWER(campaign),r'rem_|_rem-') 
          THEN CASE
            WHEN data_group IN ('channel','total_paid') THEN 'Контекст' 
            WHEN data_group = 'placement' THEN 'Яндекс Директ Небренд'
            WHEN data_group IN ('total_site','total_tops') THEN 'PAID'
            WHEN data_group = 'flight' THEN 'alwayson'
            ELSE 'Яндекс Ремаркетинг' END
      ### Яндекс API (К50) + Модельные ручные
        WHEN date < '2023-10-01' AND source = 'yandex' AND medium = 'cpc' AND REGEXP_CONTAINS(LOWER(campaign),r'_model_|_api_') 
          THEN CASE
            WHEN data_group IN ('channel','total_paid') THEN 'Контекст' 
            WHEN data_group = 'placement' THEN 'Яндекс Директ Небренд'
            WHEN data_group IN ('total_site','total_tops') THEN 'PAID'
            WHEN data_group = 'flight' THEN 'alwayson'
            ELSE 'Яндекс API (К50) + Модельные ручные' END
      ### Яндекс Категорийные + Катвендорные + Конкуренты
        WHEN date < '2023-10-01' AND source = 'yandex' AND medium = 'cpc' AND REGEXP_CONTAINS(LOWER(campaign),r'_category_|_cat-ven_|competitors|_mc_') 
          THEN CASE
            WHEN data_group IN ('channel','total_paid') THEN 'Контекст' 
            WHEN data_group = 'placement' THEN 'Яндекс Директ Небренд'
            WHEN data_group IN ('total_site','total_tops') THEN 'PAID'
            WHEN data_group = 'flight' THEN 'alwayson'
            ELSE 'Яндекс Категорийные + Катвендорные + Конукренты' END
      ### Эльдорадо Остальное
        WHEN source = 'yandex' AND medium = 'cpc'
          THEN CASE
            WHEN data_group IN ('channel','total_paid') THEN 'Контекст' 
            WHEN data_group = 'placement' THEN 'Яндекс Директ Небренд'
            WHEN data_group IN ('total_site','total_tops') THEN 'PAID'
            WHEN data_group = 'flight' THEN 'alwayson'
            ELSE 'Эльдорадо | Остальное' END

    ### Соцсети
      ### Исключение leadads
        WHEN source IN ('mt','vk','vkontakte','vkr') AND medium IN ('cpc','cpm') AND REGEXP_CONTAINS(LOWER(campaign),r'leadads') 
          THEN CASE
            WHEN data_group IN ('total_site','total_tops') THEN 'OTHER'
            WHEN data_group = 'placement' THEN 'Вакансии'
            WHEN data_group = 'flight' THEN 'alwayson'
            ELSE 'Other_data' END
      ### Федеральный бюджет
        WHEN source IN ('mt','vk','vkontakte','vkr') AND medium  IN ('cpc','cpm') AND REGEXP_CONTAINS(LOWER(campaign),r'flight') AND REGEXP_CONTAINS(LOWER(campaign),r'fed') 
        THEN CASE
            WHEN data_group IN ('channel','total_paid') THEN 'Соцсети'
            WHEN data_group IN ('total_site','total_tops') THEN 'PAID'
            WHEN data_group = 'flight' THEN 'Соцсети'
            ELSE 'Соцсети Фед. бюджет' END
      ### Соцсети Media
        WHEN source IN ('mt','vk','vkontakte','vkr') AND medium IN ('cpc','cpm') AND REGEXP_CONTAINS(LOWER(campaign),r'cpm_ny-23_')
          THEN CASE
            WHEN data_group IN ('channel','total_paid') THEN 'Соцсети'
            WHEN data_group = 'placement' THEN 'VK Reklama'
            WHEN data_group IN ('total_site','total_tops') THEN 'PAID'
            WHEN data_group = 'flight' THEN 'alwayson'
            ELSE 'Соцсети Media' END
      ### Докаты
        WHEN source IN ('mt','vk','vkontakte','vkr') AND medium IN ('cpc','cpm') AND NOT REGEXP_CONTAINS(LOWER(campaign),r'^mg|leadads|se_2023|iphone_15|ultra_2|series_9')
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
      -- ### Докаты
      --   WHEN (
      --       ((source ='soloway' AND medium = 'rs') OR source = 'adriver.ru')
      --       OR (LOWER(source) = 'hybrid' AND medium IN ('cpc','cpm'))
      --       )
      --     AND NOT REGEXP_CONTAINS(LOWER(campaign),r'^mg|^mvideo$')
      --     AND NOT REGEXP_CONTAINS(LOWER(campaign),'flight')
      --       THEN CASE
      --         WHEN data_group IN ('total_site','total_tops') THEN 'PAID'
      --         ELSE 'Докаты' END
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
      ### Turbotarget
        WHEN LOWER(source) ='turbotarget' AND medium = 'cpc'
          THEN CASE
            WHEN data_group IN ('channel','total_paid') THEN 'Ретаргетинг'
            WHEN data_group IN ('total_site','total_tops') THEN 'PAID'
            WHEN data_group = 'flight' THEN 'alwayson'
            ELSE 'Turbotarget (ретаргетинг)' END
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
            WHEN data_group = 'flight' THEN 'alwayson'
            WHEN data_group = 'total_tops' THEN 'PAID'
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

      ### Тесты и резерв
        WHEN LOWER(source) = 'adsource'
          THEN CASE
            WHEN data_group IN ('channel','total_paid') THEN 'Тесты и резерв'
            WHEN data_group IN ('total_site','total_tops') THEN 'PAID'
            WHEN data_group = 'flight' THEN 'alwayson'
            ELSE 'Тесты и резерв' END

      ### T-Shopping
        WHEN LOWER(source) = 't_shopping'AND medium = 'cpc'
          THEN CASE
            WHEN data_group IN ('channel','total_paid') THEN 'T-Shopping'
            WHEN data_group IN ('total_site','total_tops') THEN 'PAID'
            WHEN data_group = 'flight' THEN 'alwayson'
            ELSE 'T-Shopping' END

### Докаты ОСТАЛЬНОЕ PAID   
        WHEN REGEXP_CONTAINS(LOWER(medium),r'cpc') AND REGEXP_CONTAINS(LOWER(source),r'ipr_|rtg_|vk_ads|yandex|soloway|segmento|rsya|rtb|pulse_mail|mytarget|instagram|hybrid|edadeal|criteo|google|facebook|vk|mediasniper|getintent') AND NOT REGEXP_CONTAINS(LOWER(campaign),r'^mg') AND NOT REGEXP_CONTAINS(LOWER(source),r'yandexmarket')    
          THEN CASE   
            WHEN data_group IN ('total_site','total_tops') THEN 'PAID'  
            WHEN data_group = 'flight' THEN 'alwayson'  
            ELSE 'Докаты' END

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