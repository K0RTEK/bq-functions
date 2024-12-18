-- procedures.get_channel(placement)

  CASE 
    WHEN placement IN ('ЯндексДирект') THEN 'Контекст' 
    ELSE 'NaN'
  END