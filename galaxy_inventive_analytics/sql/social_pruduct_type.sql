-- procedures.social_pruduct_type(campaign, date)

CASE

  WHEN date <= '2022-12-31' THEN 'NaN'

  WHEN date > '2022-12-31' THEN 
    CASE 
      WHEN REGEXP_CONTAINS(LOWER(campaign), r'iphone_') THEN 'iPhone' 
      WHEN REGEXP_CONTAINS(LOWER(campaign), r'macbook_') THEN 'macbook'
      WHEN REGEXP_CONTAINS(LOWER(campaign), r'ipad_') THEN 'iPad'
      WHEN REGEXP_CONTAINS(LOWER(campaign), r's22') THEN 's22'
      WHEN REGEXP_CONTAINS(LOWER(campaign), r's23') THEN 's23'
      WHEN REGEXP_CONTAINS(LOWER(campaign), r'flip4') THEN 'Flip4'
      WHEN REGEXP_CONTAINS(LOWER(campaign), r'fold') THEN 'Fold'
      WHEN REGEXP_CONTAINS(LOWER(campaign), r'all_|pf_m_dir_dnmc|pf_m_ret_dnmc') THEN 'все товары'
      ELSE 'NaN'
    END

END