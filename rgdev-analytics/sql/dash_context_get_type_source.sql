### dash_procedures.get_type_source(date,campaign_name) as type_source
CASE
  WHEN REGEXP_CONTAINS(campaign_name,r'_s_') THEN 'Поиск'
  WHEN REGEXP_CONTAINS(campaign_name,r'_n_|_epk_') THEN 'Сеть'
  WHEN REGEXP_CONTAINS(campaign_name,r'_mk_') THEN 'Мастер_кампаний'
  WHEN REGEXP_CONTAINS(campaign_name,r'_tk_') THEN 'ТК'
  WHEN REGEXP_CONTAINS(campaign_name,r'_tg_') THEN 'ТГ'
  WHEN REGEXP_CONTAINS(campaign_name,r'_s_|_n_') THEN 'Поиск/Сеть'
END