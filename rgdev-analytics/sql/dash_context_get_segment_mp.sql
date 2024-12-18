### dash_procedures.get_segment_mp(date,campaign_name) as segment_mp
CASE
  WHEN REGEXP_CONTAINS(LOWER(campaign_name),r'quiz') THEN 'Квиз'
  WHEN REGEXP_CONTAINS(LOWER(campaign_name),r'_n_|_mk_|_epk_') THEN 'РСЯ и Мастер кампаний'
  WHEN REGEXP_CONTAINS(LOWER(campaign_name),r'_s_') THEN 'Поиск'
  WHEN REGEXP_CONTAINS(LOWER(campaign_name),r'_perfomance') THEN 'Тест ЕПК'
  WHEN REGEXP_CONTAINS(LOWER(campaign_name),r'_tg_') THEN 'Тест ТГ'
  WHEN REGEXP_CONTAINS(LOWER(campaign_name),r'_catalog') THEN 'Тест Каталоговые объявления'
END