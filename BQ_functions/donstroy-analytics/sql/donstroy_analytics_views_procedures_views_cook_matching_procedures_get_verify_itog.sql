### cook_matching.get_verify_itog(stage)

CASE
  WHEN stage IS NULL THEN FALSE
  WHEN LOWER(stage) = 'дисквалифицирован' THEN FALSE
  ELSE TRUE
END