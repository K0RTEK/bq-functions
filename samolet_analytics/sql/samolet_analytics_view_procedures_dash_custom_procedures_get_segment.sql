### dash_custom.get_segment(ad_name)
  CASE
    WHEN REGEXP_CONTAINS(LOWER(ad_name),r'mktr-|maketrue|-mktr') THEN 'Мейктру'
    WHEN REGEXP_CONTAINS(LOWER(ad_name),r'dinrem-prs') THEN 'Проспектинг'
    WHEN REGEXP_CONTAINS(LOWER(ad_name),r'lal') THEN 'LAL'
    WHEN REGEXP_CONTAINS(LOWER(ad_name),r'keys') AND NOT REGEXP_CONTAINS(LOWER(ad_name),r'supergeo|naruzh') THEN 'Ключи'
    WHEN REGEXP_CONTAINS(LOWER(ad_name),r'supergeo|naruzh') AND NOT REGEXP_CONTAINS(LOWER(ad_name),r'keys') THEN 'Cупергео'
    WHEN REGEXP_CONTAINS(LOWER(ad_name),r'keys') AND REGEXP_CONTAINS(LOWER(ad_name),r'supergeo|naruzh') THEN 'Ключи+Супергео'
    WHEN REGEXP_CONTAINS(LOWER(ad_name),r'ret') THEN 'Статрет'
    WHEN REGEXP_CONTAINS(LOWER(ad_name),r'dinrem') THEN 'Динрем'
    WHEN REGEXP_CONTAINS(LOWER(ad_name),r'amdt') THEN 'Амбердата'
    WHEN REGEXP_CONTAINS(LOWER(ad_name),r'dmp') THEN 'ДМП сегмент'
    WHEN REGEXP_CONTAINS(LOWER(ad_name),r'sub') THEN 'Подписчики'
    -- Интересы
    WHEN REGEXP_CONTAINS(LOWER(ad_name),r'socdem|pars|new-built|finance|ipoteka|family|education|arndv|arndrealty|avto|repair|izhs') AND NOT REGEXP_CONTAINS(LOWER(ad_name),r'keys') THEN 'Интересы'
    
    ELSE 'Интересы'
  END