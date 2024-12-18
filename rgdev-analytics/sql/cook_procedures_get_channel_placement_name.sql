### data_group: channel, placement, campaign_agency, utm_source, utm_medium, client_name
          ### cook_procedures.get_channel_placement_name(channel_name, placement_name, data_group)

            CASE
              WHEN data_group = 'client_name' THEN 'Клиент'
            
          ### Контекстаная реклама
              WHEN channel_name = 'Контекст' THEN
                CASE 
                  WHEN data_group = 'channel' THEN 'Контекстная реклама'
                  WHEN data_group = 'campaign_agency' THEN 'MGCom'
                  WHEN data_group = 'utm_medium' THEN 'cpc'
                  WHEN data_group = 'placement' THEN
                    CASE 
                      WHEN placement_name = 'Яндекс Директ' THEN 'Яндекс Директ'
                      WHEN placement_name = 'Google Ads' THEN 'Google Ads'
                    END
                  WHEN data_group = 'utm_source' THEN
                    CASE 
                      WHEN placement_name = 'Яндекс Директ' THEN 'yandex'
                      WHEN placement_name = 'Google Ads' THEN 'google'
                    END
                  ELSE 'Контекст' 
                END 
                
          ### CPA
              WHEN channel_name = 'Лидогенерация' THEN
                CASE 
                  WHEN data_group = 'channel' THEN 'Лидогенерация'
                  WHEN data_group = 'campaign_agency' THEN 'MGCom'
                  WHEN data_group = 'utm_medium' THEN 'cpa'
                  ELSE 'Лидогенерация' 
                END 
                
          ### Прайсы
              WHEN channel_name = 'Базы недвижимости' THEN
                CASE 
                  WHEN data_group = 'channel' THEN 'Базы недвижимости'
                  WHEN data_group = 'campaign_agency' THEN 'MGCom'
                  WHEN data_group = 'placement' THEN
                    CASE 
                      WHEN placement_name = 'Циан' THEN 'Циан'
                      WHEN placement_name = 'Авито' THEN 'Авито'
                      WHEN placement_name = 'Яндекс Недвижимость' THEN 'Яндекс Недвижимость'
                    END
                  ELSE 'Базы недвижимости' 
                END 

          ### Соцсети
              WHEN channel_name = 'Соцсети' THEN
                CASE 
                  WHEN data_group = 'channel' THEN 'Реклама в соц.сетях'
                  WHEN data_group = 'campaign_agency' THEN 'MGCom'
                  WHEN data_group = 'utm_medium' THEN 'cpc'
                  WHEN data_group = 'placement' THEN
                    CASE 
                      WHEN placement_name = 'Вконтакте' THEN 'Вконтакте'
                      WHEN placement_name = 'ВКР' THEN 'ВКР'
                      WHEN placement_name = 'Mytarget' THEN 'Mytarget'
                    END
                  WHEN data_group = 'utm_source' THEN
                    CASE 
                      WHEN placement_name = 'Вконтакте' THEN 'vkontakte'
                      WHEN placement_name = 'ВКР' THEN 'vkr'
                      WHEN placement_name = 'Mytarget' THEN 'mt'
                    END
                  ELSE 'Соцсети' 
                END 

          ### Медийка
              WHEN channel_name = 'Медийная реклама' THEN
                CASE 
                  WHEN data_group = 'channel' THEN 'Медийная реклама'
                  WHEN data_group = 'campaign_agency' THEN 'MGCom'
                  ELSE 'Медийная реклама'
                END

          ### Программатик
              WHEN channel_name = 'Программатик' THEN
                CASE 
                  WHEN data_group = 'channel' THEN 'Программатик'
                  WHEN data_group = 'campaign_agency' THEN 'MGCom'
                  WHEN data_group = 'placement' THEN
                    CASE 
                      WHEN placement_name = 'Soloway' THEN 'Soloway'
                      WHEN placement_name = 'Hybrid' THEN 'Hybrid'
                    END
                  WHEN data_group = 'utm_source' THEN
                    CASE 
                      WHEN placement_name = 'Soloway' THEN 'soloway'
                      WHEN placement_name = 'Hybrid' THEN 'hybrid'
                    END
                  WHEN data_group = 'utm_medium' THEN
                    CASE 
                      WHEN placement_name = 'Soloway' THEN 'cpc'
                      WHEN placement_name = 'Hybrid' THEN 'cpc'
                    END
                  ELSE 'Программатик' 
                END

            END