-- procedures.month_ru(date)

  CASE 
    WHEN EXTRACT(month FROM date) = 1 THEN 'январь' 
    WHEN EXTRACT(month FROM date) = 2 THEN 'февраль' 
    WHEN EXTRACT(month FROM date) = 3 THEN 'март'
    WHEN EXTRACT(month FROM date) = 4 THEN 'апрель'
    WHEN EXTRACT(month FROM date) = 5 THEN 'май'
    WHEN EXTRACT(month FROM date) = 6 THEN 'июнь'
    WHEN EXTRACT(month FROM date) = 7 THEN 'июль'
    WHEN EXTRACT(month FROM date) = 8 THEN 'август'
    WHEN EXTRACT(month FROM date) = 9 THEN 'сентябрь'
    WHEN EXTRACT(month FROM date) = 10 THEN 'октябрь'
    WHEN EXTRACT(month FROM date) = 11 THEN 'ноябрь'
    WHEN EXTRACT(month FROM date) = 12 THEN 'декабрь'
    ELSE 'NaN'
  END