-- procedures.social_logic(campaign, date)

CASE

  WHEN date <= '2022-12-31' THEN 
      CASE 
        WHEN REGEXP_CONTAINS(LOWER(campaign), r'_dir') THEN 'Прямая логика' 
        WHEN REGEXP_CONTAINS(LOWER(campaign), r'_kw|keys') THEN 'Ключи'
        WHEN REGEXP_CONTAINS(LOWER(campaign), r'_int') THEN 'Интересы'
        WHEN REGEXP_CONTAINS(LOWER(campaign), r'_ret_dnmc') THEN 'Дин.рем'
        WHEN REGEXP_CONTAINS(LOWER(campaign), r'_ret_') AND NOT REGEXP_CONTAINS(LOWER(campaign), r'dnmc') THEN 'Ретаргетинг'
        ELSE 'NaN'
      END

    WHEN date > '2022-12-31' THEN 
      CASE 
          WHEN REGEXP_CONTAINS(LOWER(campaign), r'ret_') THEN 'ретаргет' 
          WHEN REGEXP_CONTAINS(LOWER(campaign), r'dir_') THEN 'прямая'
          ELSE 'NaN'
      END

END