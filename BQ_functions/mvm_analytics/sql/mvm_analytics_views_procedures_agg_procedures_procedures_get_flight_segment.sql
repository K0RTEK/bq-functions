### agg_procedures.get_flight_segment`(date,campaign)
    CASE
      WHEN REGEXP_CONTAINS(LOWER(campaign),r'_s[eе]_') THEN 'Сервисы'
      WHEN REGEXP_CONTAINS(LOWER(campaign),r'_[eе][pр]_|_[eе]-[pр]_') THEN 'Фото и видео'
      WHEN REGEXP_CONTAINS(LOWER(campaign),r'_[aа][cс]_|_[aа]-[cс]_') THEN 'Аксессуары МВ'
      WHEN REGEXP_CONTAINS(LOWER(campaign),r'_[hн][oо]_|_[hн]-[oо]_') THEN 'Домашний офис'
      WHEN REGEXP_CONTAINS(LOWER(campaign),r'_[cс]-[eе]_|_[cс][eе]_') THEN 'Аксессуары МВ'
      WHEN REGEXP_CONTAINS(LOWER(campaign),r'_[cс]-s_|_[cс]s_|_[cс]_s_') THEN 'Кино и звук'
      WHEN REGEXP_CONTAINS(LOWER(campaign),r'_[hн]-[cс]_|_[hн]_[cс]_ ') THEN 'Дом и забота о себе'
      WHEN REGEXP_CONTAINS(LOWER(campaign),r'_[kк][tт]_') THEN 'Кухня'
      WHEN REGEXP_CONTAINS(LOWER(campaign),r'_[mм][bв]_|_[mм]v_.*_[mм]v_|_eldo_.*_[mм]v_') THEN 'Телеком'
      ELSE 'NaN'
    END