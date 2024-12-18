### dash_procedures.get_pm_channel_mapping(date,data_group,channel,placement,placement_pf,total_paid,total_site,total_tops)
### data_group: channel, placement, placement_pf, total_paid, total_site, total_tops
    CASE
      WHEN channel IN ('Контекст','Соцсети','Ретаргетинг','Прайс-площадки','Докаты','Геосервисы','Telegram') OR LOWER(channel) LIKE '%докаты%'
        THEN CASE
          WHEN data_group = 'channel' THEN channel
          WHEN data_group = 'placement' THEN placement
          WHEN data_group = 'placement_pf' THEN placement_pf
          WHEN data_group = 'total_paid' THEN channel
          ELSE 'PAID' END

      -- WHEN channel = 'Геосервисы' 
      --   THEN CASE
      --     WHEN data_group = 'channel' THEN channel
      --     WHEN data_group = 'placement' THEN placement
      --     WHEN data_group = 'placement_pf' THEN placement_pf
      --     WHEN data_group = 'total_paid' THEN channel          
      --     WHEN data_group = 'total_tops' THEN 'GEO'
      --     ELSE 'PAID' END

      WHEN LOWER(total_site) IN ('organic yandex','organic google')
        THEN CASE
          WHEN data_group = 'total_site' THEN total_site
          WHEN data_group = 'total_tops' THEN 'ORGANIC'
          ELSE 'Other_data' END

      WHEN LOWER(total_site) = 'organic other'
        THEN CASE
          WHEN data_group = 'total_site' THEN 'OTHER'
          WHEN data_group = 'total_tops' THEN 'ORGANIC'
          ELSE 'Other_data' END

      WHEN total_site IN ('CPA','DIRECT','EMAIL','PAID','GEO')
        THEN CASE
          WHEN data_group IN ('total_tops','total_site') THEN total_site
          ELSE 'Other_data' END

      ELSE CASE
        WHEN data_group IN ('total_tops','total_site') THEN 'OTHER'
        ELSE 'Other_data' END
      
    END