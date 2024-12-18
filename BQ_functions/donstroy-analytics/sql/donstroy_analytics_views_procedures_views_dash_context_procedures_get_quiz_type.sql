CASE
  WHEN REGEXP_CONTAINS(LOWER(TRIM(campaign_name)),"quiz.pages") THEN "Квиз Pages"
  WHEN REGEXP_CONTAINS(LOWER(TRIM(campaign_name)),"quiz") THEN "Квиз"
END