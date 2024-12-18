### dash_procedures.get_flight_segments(segment,campaign)
### segment: budget, ecounit, flight_id, jira_id, period, category
  CASE

  ### Тип бюджета
    WHEN segment = 'budget' AND REGEXP_CONTAINS(LOWER(campaign),r'_kd_') 
        THEN 'Вендорский'
    WHEN segment = 'budget' AND  REGEXP_CONTAINS(LOWER(campaign),r'_fed_') 
        THEN 'МВМ'

  ### Экоюнит
    WHEN segment = 'ecounit' AND REGEXP_CONTAINS(LOWER(campaign),r'_e-p_') 
        THEN 'Развлечения и Фото-Видео'
    WHEN segment = 'ecounit' AND REGEXP_CONTAINS(LOWER(campaign),r'_kt_') 
        THEN 'Кухня'
    WHEN segment = 'ecounit' AND REGEXP_CONTAINS(LOWER(campaign),r'_mb_') 
        THEN 'Мобильная техника'
    WHEN segment = 'ecounit' AND REGEXP_CONTAINS(LOWER(campaign),r'_h-o_') 
        THEN 'Домашний офис'
    WHEN segment = 'ecounit' AND REGEXP_CONTAINS(LOWER(campaign),r'_c-s_|_c_s_') 
        THEN 'Кино и Звук'
    WHEN segment = 'ecounit' AND REGEXP_CONTAINS(LOWER(campaign),r'_h-c_') 
        THEN 'Дом и забота о себе'

  ### Флайт id
    WHEN segment = 'flight_id' AND REGEXP_EXTRACT(LOWER(campaign),r'..\...-..\...\..._([0-9]+)') IS NOT NULL # 00.00-00.00.00_
        THEN REGEXP_EXTRACT(LOWER(campaign),r'..\...-..\...\..._([0-9]+)')
    WHEN segment = 'flight_id' AND REGEXP_EXTRACT(LOWER(campaign),r'..\...-..\...\....._([0-9]+)') IS NOT NULL # 00.00-00.00.0000_
        THEN REGEXP_EXTRACT(LOWER(campaign),r'..\...-..\...\....._([0-9]+)')
    WHEN segment = 'flight_id' AND REGEXP_EXTRACT(LOWER(campaign),r'..\...\.....-..\...\....._([0-9]+)') IS NOT NULL # 00.00.000-00.00.0000_
        THEN REGEXP_EXTRACT(LOWER(campaign),r'..\...\.....-..\...\....._([0-9]+)')
    WHEN segment = 'flight_id' AND REGEXP_EXTRACT(LOWER(campaign),r'..\...-..\..._([0-9]+)') IS NOT NULL # 00.00-00.00_
        THEN REGEXP_EXTRACT(LOWER(campaign),r'..\...-..\..._([0-9]+)')
    WHEN segment = 'flight_id' AND REGEXP_EXTRACT(LOWER(campaign),r'..\..._..\..._([0-9]+)') IS NOT NULL # 00.00_00.00_
        THEN REGEXP_EXTRACT(LOWER(campaign),r'..\..._..\..._([0-9]+)')
    WHEN segment = 'flight_id' AND REGEXP_EXTRACT(LOWER(campaign),r'..\...-.\...\..._([0-9]+)') IS NOT NULL # 00.00-0.00.00_
        THEN REGEXP_EXTRACT(LOWER(campaign),r'..\...-.\...\..._([0-9]+)')
    WHEN segment = 'flight_id' AND REGEXP_EXTRACT(LOWER(campaign),r'..\...-..\...\....*_([0-9]+)') IS NOT NULL # 00.00-00.00.00.*_
        THEN REGEXP_EXTRACT(LOWER(campaign),r'..\...-..\...\....*_([0-9]+)')
    WHEN segment = 'flight_id' AND REGEXP_EXTRACT(LOWER(campaign),r'..\...-..\....*_([0-9]+)') IS NOT NULL # 00.00-00.00.*_
        THEN REGEXP_EXTRACT(LOWER(campaign),r'..\...-..\....*_([0-9]+)')
    WHEN segment = 'flight_id' AND REGEXP_EXTRACT(LOWER(campaign),r'..\...\.....-..\...\....*_([0-9]+)') IS NOT NULL # 00.00.0000-00.00.*_
        THEN REGEXP_EXTRACT(LOWER(campaign),r'..\...\.....-..\...\....*_([0-9]+)')
    WHEN segment = 'flight_id' AND REGEXP_EXTRACT(LOWER(campaign),r'..\...-.\...\....*_([0-9]+)') IS NOT NULL # 00.00-0.00.*_
        THEN REGEXP_EXTRACT(LOWER(campaign),r'..\...-.\...\....*_([0-9]+)')
    WHEN segment = 'flight_id' AND REGEXP_EXTRACT(LOWER(campaign),r'..\...\... - ..\...\..._([0-9]+)') IS NOT NULL # 00.00.00 - 00.00.00_
        THEN REGEXP_EXTRACT(LOWER(campaign),r'..\...\... - ..\...\..._([0-9]+)')
    WHEN segment = 'flight_id' AND REGEXP_EXTRACT(LOWER(campaign),r'..\... - ..\..._([0-9]+)') IS NOT NULL # 00.00 - 00.00_
        THEN REGEXP_EXTRACT(LOWER(campaign),r'..\... - ..\..._([0-9]+)')
    WHEN segment = 'flight_id' AND REGEXP_EXTRACT(LOWER(campaign),r'..\...\...-..\...\..._([0-9]+)') IS NOT NULL # 00.00.00-00.00.00_
        THEN REGEXP_EXTRACT(LOWER(campaign),r'..\...\...-..\...\..._([0-9]+)')
    WHEN segment = 'flight_id' AND REGEXP_EXTRACT(LOWER(campaign),r'..\...-.\..._([0-9]+)') IS NOT NULL # 00.00-0.00_
        THEN REGEXP_EXTRACT(LOWER(campaign),r'..\...-.\..._([0-9]+)')
    WHEN segment = 'flight_id' AND REGEXP_EXTRACT(LOWER(campaign),r'..\....-.\..._([0-9]+)') IS NOT NULL # 00.00.-0.00_
        THEN REGEXP_EXTRACT(LOWER(campaign),r'..\....-.\..._([0-9]+)')
    WHEN segment = 'flight_id' AND REGEXP_EXTRACT(LOWER(REGEXP_REPLACE(campaign,'%2520','')),r'..\...\...-..\...\..._([0-9]+)') IS NOT NULL # 00.00.00%2520-%252000.00.00_
        THEN REGEXP_EXTRACT(LOWER(campaign),r'..\...\...-..\...\..._([0-9]+)')
    WHEN segment = 'flight_id' AND REGEXP_EXTRACT(LOWER(campaign),r'[0-9]{6,6}_[0-9]{6,6}_([0-9]+)') IS NOT NULL # 000000_000000_
        THEN REGEXP_EXTRACT(LOWER(campaign),r'[0-9]{6,6}_[0-9]{6,6}_([0-9]+)')
    WHEN segment = 'flight_id' AND REGEXP_EXTRACT(LOWER(campaign),r'[0-9]{4,4}_[0-9]{4,4}_([0-9]+)') IS NOT NULL # 0000_0000_
        THEN REGEXP_EXTRACT(LOWER(campaign),r'[0-9]{4,4}_[0-9]{4,4}_([0-9]+)')

  ### Jira id
    WHEN segment = 'jira_id' AND REGEXP_EXTRACT(LOWER(campaign),r'_([0-9]+)_.*\...-..\...\...') IS NOT NULL
        THEN REGEXP_EXTRACT(LOWER(campaign),r'_([0-9]+)_.*\...-..\...\...')
    WHEN segment = 'jira_id' AND REGEXP_EXTRACT(LOWER(campaign),r'_([0-9]+)_.*\...-.\...\...') IS NOT NULL
        THEN REGEXP_EXTRACT(LOWER(campaign),r'_([0-9]+)_.*\...-.\...\...')
    WHEN segment = 'jira_id' AND REGEXP_EXTRACT(LOWER(campaign),r'_([0-9]+)_.*-.*') IS NOT NULL
        THEN REGEXP_EXTRACT(LOWER(campaign),r'_([0-9]+)_.*-.*')

  ### Период флайта
    WHEN segment = 'period' AND REGEXP_EXTRACT(LOWER(campaign),r'(..\...-..\...\...)') IS NOT NULL
        THEN REGEXP_EXTRACT(LOWER(campaign),r'(..\...-..\...\...)')
    WHEN segment = 'period' AND REGEXP_EXTRACT(LOWER(campaign),r'(..\...\.....-..\...\.....)') IS NOT NULL
        THEN REGEXP_EXTRACT(LOWER(campaign),r'(..\...\.....-..\...\.....)')
    WHEN segment = 'period' AND REGEXP_EXTRACT(LOWER(campaign),r'(..\...-..\...)') IS NOT NULL
        THEN REGEXP_EXTRACT(LOWER(campaign),r'(..\...-..\...)')
    WHEN segment = 'period' AND REGEXP_EXTRACT(LOWER(campaign),r'(..\...-.\...\...)') IS NOT NULL
        THEN REGEXP_EXTRACT(LOWER(campaign),r'(..\...-.\...\...)')

  ### Категория
    WHEN segment = 'category' AND REGEXP_CONTAINS(LOWER(campaign),r'(mv|eldo).*(_se_)')
        THEN 'Сервисы'
    WHEN segment = 'category' AND REGEXP_CONTAINS(LOWER(campaign),r'(mv|eldo).*(_ер_|_е-р_|_ep_|_e-p_)')
        THEN 'Фото и видео'
    WHEN segment = 'category' AND REGEXP_CONTAINS(LOWER(campaign),r'(mv|eldo).*(_ас_|_а-с_|_ac_|_a-c_)')
        THEN 'Аксессуары МВ'
    WHEN segment = 'category' AND REGEXP_CONTAINS(LOWER(campaign),r'(mv|eldo).*(_но_|_н-о_|_ho_|_h-o_)')
        THEN 'Домашний офис'
    WHEN segment = 'category' AND REGEXP_CONTAINS(LOWER(campaign),r'(mv|eldo).*(_с-е_|_се_|_c-e_|_ce_)')
        THEN 'Аксессуары'
    WHEN segment = 'category' AND REGEXP_CONTAINS(LOWER(campaign),r'(mv|eldo).*(_c-s_|_cs_|_c_s_)')
        THEN 'Кино и звук'
    WHEN segment = 'category' AND REGEXP_CONTAINS(LOWER(campaign),r'(mv|eldo).*(_н-с_|_h-c_|_h_c_|_н_с_)')
        THEN 'Дом и забота о себе'
    WHEN segment = 'category' AND REGEXP_CONTAINS(LOWER(campaign),r'(mv|eldo).*(_kt_|_кт_)')
        THEN 'Кухня'
    WHEN segment = 'category' AND REGEXP_CONTAINS(LOWER(campaign),r'(mv|eldo).*(_мв_|_mb_|_мb_|_mв_|_mv_)')
        THEN 'Телеком'


    ELSE CONCAT('NaN - ', campaign)
  END