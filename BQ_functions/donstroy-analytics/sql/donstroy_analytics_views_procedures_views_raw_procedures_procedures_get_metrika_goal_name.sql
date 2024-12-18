### raw_procedures.get_metrika_goal_name(goal)
CASE
  WHEN REGEXP_CONTAINS(LOWER(goal),r'140137726') THEN 'nan'
    ELSE CONCAT('NaN - ',goal)
END