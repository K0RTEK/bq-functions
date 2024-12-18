case
                  when (
                              regexp_contains(lower(utm_source), r'yd')
                              and regexp_contains(lower(utm_medium), r'cpc')
                          )
                      or (
                                  source_engine = 'Yandex: Direct'
                              and utm_source is null
                          )
                      or (
                          regexp_contains(lower(calltracking), r'директ|direct|квиз мих')
                          )
                      or (
                              regexp_contains(lower(calltracking), r'посетители без рекламной кампании|прямые заходы')
                              and regexp_contains(lower(utm_source), r'yd')
                          )
                      then 'Яндекс Директ'

                  when (
                              regexp_contains(lower(utm_source), r'google')
                              and regexp_contains(lower(utm_medium), r'cpc')
                          )
                  
                      or( 
                              regexp_contains(lower(calltracking), r'mg|sm')
                              and regexp_contains(lower(calltracking), r'google|гугл')
                        )
                      then 'Google Ads'

                  when traffic_source = 'Search engine traffic'
                      and utm_source is null
                      and utm_medium is null
                      then 'Поисковые системы'

                  when traffic_source = 'Link traffic'
                      and utm_source is null
                      and utm_medium is null
                      then 'Переходы по ссылкам'

                  when regexp_contains(lower(calltracking), r'like estate|likeestate|румбери|callexchange|лидогенерация')
                      and not regexp_contains(lower(calltracking), r'сian.ru Лидогенерация')
                      then 'CPA'
                      
                  WHEN (REGEXP_CONTAINS(LOWER(utm_source),r'vk_ads|vk_reklama') 
                      OR REGEXP_CONTAINS(LOWER(utm_source),r'_vk$|^vk$|^vk_')
                      OR REGEXP_CONTAINS(LOWER(utm_source),r'mytarget|_mt$')
                      OR REGEXP_CONTAINS(LOWER(utm_source),r'facebook|fb_ig|inst|_fb$')
                      OR REGEXP_CONTAINS(LOWER(utm_source),r'tiktok')
                      OR REGEXP_CONTAINS(LOWER(utm_source),r'telegram')
                      )
                      AND utm_medium IN ('cpc','cpm')
                      THEN 'Реклама в соц.сетях'

                  end