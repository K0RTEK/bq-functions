### cook_procedures.get_placement(parameter)

          CASE
          ### Контекст
            WHEN REGEXP_CONTAINS(LOWER(parameter), r'yandex|яндекс') AND NOT REGEXP_CONTAINS(LOWER(parameter), r'realty|недвижимость') THEN 'Яндекс Директ'
            
          ### Базы недвижимости 
            WHEN REGEXP_CONTAINS(LOWER(parameter), r'avito|авито') THEN 'Авито'
            WHEN REGEXP_CONTAINS(LOWER(parameter), r'cian|циан') THEN 'Циан'
            WHEN REGEXP_CONTAINS(LOWER(parameter), r'realty.*yandex|яндекс.*недвижимость') THEN 'Яндекс Недвижимость'
            WHEN REGEXP_CONTAINS(LOWER(parameter), r'jcat') THEN 'JCAT'
            WHEN REGEXP_CONTAINS(LOWER(parameter), r'svetvokne') THEN 'Svetvokne'
            WHEN REGEXP_CONTAINS(LOWER(parameter), r'm2|м2') THEN 'М2'
            WHEN REGEXP_CONTAINS(LOWER(parameter), r'domclick|домклик') THEN 'Домклик'
            WHEN REGEXP_CONTAINS(LOWER(parameter), r'novostroy-m') THEN 'Новострой-М'
            WHEN REGEXP_CONTAINS(LOWER(parameter), r'avaho|авахо') THEN 'Авахо'
            WHEN REGEXP_CONTAINS(LOWER(parameter), r'move') THEN 'Move.ru'
            WHEN REGEXP_CONTAINS(LOWER(parameter), r'мирквартир') THEN 'МирКвартир'

          ### Соцсети 
            WHEN REGEXP_CONTAINS(LOWER(parameter),r'vkr|vk reklama|vk ads|vkads') THEN 'ВКР'
            WHEN REGEXP_CONTAINS(LOWER(parameter),r'	vk | vk$| vk | вк | вк$|fb.*vk|вконтакте| вк ') THEN 'Вконтакте'
            WHEN REGEXP_CONTAINS(LOWER(parameter),r' mt$|fb.*mt| мт$| мт |mt|mytarget|target.mail| mail ') THEN 'MyTarget'
            WHEN REGEXP_CONTAINS(LOWER(parameter),r'facebook| fb | fb$|insta|fb.inst') THEN 'Facebook'
            WHEN REGEXP_CONTAINS(LOWER(parameter),r'telegram') THEN 'Telegram'
            WHEN REGEXP_CONTAINS(LOWER(parameter),r'tenchat') THEN 'TenChat'
            WHEN REGEXP_CONTAINS(LOWER(parameter),r'tiktok|tik-tok') THEN 'Tik-tok'

            ELSE 'Не определено'
          END