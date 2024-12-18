### procedures.cont_vendor(campaign)

-- сегменты только для Эльдорадо, условия прописаны в задаче https://pf.mgcom.ru/task/1086081 

  CASE
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_lg_') THEN 'LG'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'philips') THEN 'philips'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'samsung') THEN 'samsung'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'sony') THEN 'sony'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'apple') THEN 'apple'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'honor') THEN 'honor'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'huawei') THEN 'huawei'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'other') THEN 'other'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'realme') THEN 'realme'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'xiaomi') THEN 'xiaomi'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'acer') THEN 'acer'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'lenovo') THEN 'lenovo'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'artel') THEN 'artel'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'grundig') THEN 'grundig'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'haier') THEN 'haier'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_hec_') THEN 'HEC'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_hi_') THEN 'HI'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'hisense') THEN 'hisense'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'novex') THEN 'novex'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'sber') THEN 'sber'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'sharp') THEN 'sharp'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'telefunken') THEN 'telefunken'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'toshiba') THEN 'toshiba'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'v-home') THEN 'v-home'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'vitjaz') THEN 'vitjaz'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'poco') THEN 'poco'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'tecno') THEN 'tecno'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'vivo') THEN 'vivo'

    ELSE 'NaN'
  END