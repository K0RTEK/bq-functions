### procedures.cont_fl_ecounit(campaign)
  CASE
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_e-p_') THEN 'Развлечения и Фото-Видео'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_kt_') THEN 'Кухня'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_mb_') THEN 'Мобильная техника'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_h-o_') THEN 'Домашний офис'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_c-s_|_c_s_') THEN 'Кино и Звук'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_h-c_') THEN 'Дом и забота о себе'
    ELSE CONCAT('NaN')
  END