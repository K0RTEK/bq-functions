### raw_procedures.get_metrika_goal_name(goal)
        CASE
          WHEN REGEXP_CONTAINS(LOWER(goal),r'111111111') THEN 'ЦЕЛЬ'
            ELSE CONCAT('NaN - ',goal)
        END