### raw_procedures.get_metrika_goal_name(goal)
  CASE
    WHEN REGEXP_CONTAINS(LOWER(goal),r'329061850') THEN 'ym_scroll_100'
    WHEN REGEXP_CONTAINS(LOWER(goal),r'329062055') THEN 'ym_time_3_min'
    WHEN REGEXP_CONTAINS(LOWER(goal),r'329062356') THEN 'ym_telephone_click_header'
    WHEN REGEXP_CONTAINS(LOWER(goal),r'329062406') THEN 'ym_telephone_click_footer'
    ELSE CONCAT('NaN - ',IFNULL(goal,''))
  END