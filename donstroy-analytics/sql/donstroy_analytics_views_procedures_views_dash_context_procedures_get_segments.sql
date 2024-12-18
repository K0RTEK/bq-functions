CASE
  /*
  `dash_context.get_segments`('segment_mp',campaign_name, campaign_object, event_object) as segment_mp,
  `dash_context.get_segments`('type_campaign',campaign_name, campaign_object, event_object) as type_campaign,
  `dash_context.get_segments`('type_segment',campaign_name, campaign_object, event_object) as type_segment,
  `dash_context.get_segments`('quiz_type',campaign_name, campaign_object, event_object) as quiz_type,
  */

  WHEN parameter='segment_mp' THEN
    CASE
      WHEN campaign_object = event_object AND 
        REGEXP_CONTAINS(LOWER(TRIM(campaign_name)),"_s_") AND REGEXP_CONTAINS(LOWER(TRIM(campaign_name)),"brand")
        THEN "Бренд поиск"
      WHEN campaign_object = event_object AND 
         REGEXP_CONTAINS(LOWER(TRIM(campaign_name)),"_s_") 
        THEN "Небренд поиск"
      WHEN campaign_object = event_object AND 
         REGEXP_CONTAINS(LOWER(TRIM(campaign_name)),"_n_") AND REGEXP_CONTAINS(LOWER(TRIM(campaign_name)),"quiz|квиз")
        THEN "Квиз"
      WHEN campaign_object = event_object AND 
         REGEXP_CONTAINS(LOWER(TRIM(campaign_name)),"_n_") AND REGEXP_CONTAINS(LOWER(TRIM(campaign_name)),"master")
        THEN "Мастер кампаний"
      WHEN campaign_object = event_object AND 
         REGEXP_CONTAINS(LOWER(TRIM(campaign_name)),"_n_") AND REGEXP_CONTAINS(LOWER(TRIM(campaign_name)),"katalog")
        THEN "Каталоговые объявления"
      WHEN campaign_object = event_object AND 
         REGEXP_CONTAINS(LOWER(TRIM(campaign_name)),"_n_") 
        THEN "РСЯ"
      WHEN campaign_object = event_object
        THEN "Прочее"
      WHEN NOT campaign_object = event_object
        THEN "РК других проектов"
      ELSE 'Прочее'
    END

  WHEN parameter='type_segment' THEN
    CASE
      WHEN REGEXP_CONTAINS(campaign_name,r'compet') THEN 'Конкуренты'
      WHEN REGEXP_CONTAINS(campaign_name,r'brand') THEN 'Бренд'
      WHEN REGEXP_CONTAINS(campaign_name,r'geo') THEN 'Гео'
      WHEN REGEXP_CONTAINS(campaign_name,r'ipoteka|otdelka|planirovki|obshie|video|obshiasecond|autotargeting|semant|katalog') THEN 'Общие'
      WHEN REGEXP_CONTAINS(campaign_name,r'performance') THEN 'ЕПК'
      WHEN REGEXP_CONTAINS(campaign_name,r'klass|class|luxury') THEN 'Категорийные'
      WHEN REGEXP_CONTAINS(campaign_name,r'audience|lal|lalall|y_r_lal_') THEN 'LAL'
      WHEN REGEXP_CONTAINS(campaign_name,r'master') THEN 'МК'
      WHEN REGEXP_CONTAINS(campaign_name,r'smart') THEN 'Смартбаннеры'
      WHEN REGEXP_CONTAINS(campaign_name,r'interest|y_r_interest|audience|dzen|audiencemin1|media|amberdata') THEN 'Аудитории'
      WHEN REGEXP_CONTAINS(campaign_name,r'_y_r_') THEN 'Ретаргетинг'
      ELSE 'Прочее'
    END

  WHEN parameter = 'quiz_type' THEN
    CASE
      WHEN REGEXP_CONTAINS(LOWER(TRIM(campaign_name)),"quiz.pages") THEN "Квиз Pages"
      WHEN REGEXP_CONTAINS(LOWER(TRIM(campaign_name)),"quiz") THEN "Квиз"
      ELSE "Не квиз"
    END
    
  ELSE 'Прочее'
END