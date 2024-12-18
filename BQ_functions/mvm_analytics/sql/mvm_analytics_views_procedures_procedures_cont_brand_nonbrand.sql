### procedures.cont_brand_nonbrand(campaign)
  CASE
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_image_name.*(_p_|search)') THEN 'Бренд'
    ELSE 'Не Бренд'
  END