### procedures.cont_fl_id(campaign)

  CASE
    WHEN REGEXP_EXTRACT(LOWER(campaign),r'..\...-..\...\..._([0-9]+)') IS NOT NULL # 00.00-00.00.00_
      THEN REGEXP_EXTRACT(LOWER(campaign),r'..\...-..\...\..._([0-9]+)')

    WHEN REGEXP_EXTRACT(LOWER(campaign),r'..\...-..\...\....._([0-9]+)') IS NOT NULL # 00.00-00.00.0000_
      THEN REGEXP_EXTRACT(LOWER(campaign),r'..\...-..\...\....._([0-9]+)')

    WHEN REGEXP_EXTRACT(LOWER(campaign),r'..\...\.....-..\...\....._([0-9]+)') IS NOT NULL # 00.00.000-00.00.0000_
      THEN REGEXP_EXTRACT(LOWER(campaign),r'..\...\.....-..\...\....._([0-9]+)')

    WHEN REGEXP_EXTRACT(LOWER(campaign),r'..\...-..\..._([0-9]+)') IS NOT NULL # 00.00-00.00_
      THEN REGEXP_EXTRACT(LOWER(campaign),r'..\...-..\..._([0-9]+)')

    WHEN REGEXP_EXTRACT(LOWER(campaign),r'..\..._..\..._([0-9]+)') IS NOT NULL # 00.00_00.00_
      THEN REGEXP_EXTRACT(LOWER(campaign),r'..\..._..\..._([0-9]+)')

    WHEN REGEXP_EXTRACT(LOWER(campaign),r'..\...-.\...\..._([0-9]+)') IS NOT NULL # 00.00-0.00.00_
      THEN REGEXP_EXTRACT(LOWER(campaign),r'..\...-.\...\..._([0-9]+)')


    WHEN REGEXP_EXTRACT(LOWER(campaign),r'..\...-..\...\....*_([0-9]+)') IS NOT NULL # 00.00-00.00.00.*_
      THEN REGEXP_EXTRACT(LOWER(campaign),r'..\...-..\...\....*_([0-9]+)')

    WHEN REGEXP_EXTRACT(LOWER(campaign),r'..\...-..\....*_([0-9]+)') IS NOT NULL # 00.00-00.00.*_
      THEN REGEXP_EXTRACT(LOWER(campaign),r'..\...-..\....*_([0-9]+)')

    WHEN REGEXP_EXTRACT(LOWER(campaign),r'..\...\.....-..\...\....*_([0-9]+)') IS NOT NULL # 00.00.0000-00.00.*_
      THEN REGEXP_EXTRACT(LOWER(campaign),r'..\...\.....-..\...\....*_([0-9]+)')

    WHEN REGEXP_EXTRACT(LOWER(campaign),r'..\...-.\...\....*_([0-9]+)') IS NOT NULL # 00.00-0.00.*_
      THEN REGEXP_EXTRACT(LOWER(campaign),r'..\...-.\...\....*_([0-9]+)')

    WHEN REGEXP_EXTRACT(LOWER(campaign),r'..\...\... - ..\...\..._([0-9]+)') IS NOT NULL # 00.00.00 - 00.00.00_
      THEN REGEXP_EXTRACT(LOWER(campaign),r'..\...\... - ..\...\..._([0-9]+)')

    WHEN REGEXP_EXTRACT(LOWER(campaign),r'..\... - ..\..._([0-9]+)') IS NOT NULL # 00.00 - 00.00_
      THEN REGEXP_EXTRACT(LOWER(campaign),r'..\... - ..\..._([0-9]+)')

    WHEN REGEXP_EXTRACT(LOWER(campaign),r'..\...\...-..\...\..._([0-9]+)') IS NOT NULL # 00.00.00-00.00.00_
      THEN REGEXP_EXTRACT(LOWER(campaign),r'..\...\...-..\...\..._([0-9]+)')

    WHEN REGEXP_EXTRACT(LOWER(campaign),r'..\...-.\..._([0-9]+)') IS NOT NULL # 00.00-0.00_
      THEN REGEXP_EXTRACT(LOWER(campaign),r'..\...-.\..._([0-9]+)')

    WHEN REGEXP_EXTRACT(LOWER(campaign),r'..\....-.\..._([0-9]+)') IS NOT NULL # 00.00.-0.00_
      THEN REGEXP_EXTRACT(LOWER(campaign),r'..\....-.\..._([0-9]+)')

    WHEN REGEXP_EXTRACT(LOWER(REGEXP_REPLACE(campaign,'%2520','')),r'..\...\...-..\...\..._([0-9]+)') IS NOT NULL # 00.00.00%2520-%252000.00.00_
      THEN REGEXP_EXTRACT(LOWER(campaign),r'..\...\...-..\...\..._([0-9]+)')

    WHEN REGEXP_EXTRACT(LOWER(campaign),r'[0-9]{6,6}_[0-9]{6,6}_([0-9]+)') IS NOT NULL # 000000_000000_
      THEN REGEXP_EXTRACT(LOWER(campaign),r'[0-9]{6,6}_[0-9]{6,6}_([0-9]+)')

    WHEN REGEXP_EXTRACT(LOWER(campaign),r'[0-9]{4,4}_[0-9]{4,4}_([0-9]+)') IS NOT NULL # 0000_0000_
      THEN REGEXP_EXTRACT(LOWER(campaign),r'[0-9]{4,4}_[0-9]{4,4}_([0-9]+)')
    ELSE 'NaN'
  END