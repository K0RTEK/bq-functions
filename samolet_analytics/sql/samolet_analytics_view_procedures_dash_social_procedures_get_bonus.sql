CASE
### dash_social.get_bonus(date,parameter,account_name,cost)
  ### cost
  WHEN parameter = 'get_cost' AND NOT REGEXP_CONTAINS(LOWER(account_name),r'bonus') THEN cost*1.2*0.9865
  WHEN parameter = 'get_cost' AND REGEXP_CONTAINS(LOWER(account_name),r'bonus') THEN cost*1.2*0.9865*0.1
  ### bonus
  WHEN parameter = 'get_bonus' AND NOT REGEXP_CONTAINS(LOWER(account_name),r'bonus') THEN cost*0
  WHEN parameter = 'get_bonus' AND REGEXP_CONTAINS(LOWER(account_name),r'bonus') THEN cost*0.9
  
  ELSE NULL
END