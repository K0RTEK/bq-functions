-- procedures.fact_mediaplan_name(channel)

  CASE 
    WHEN channel = 'Контекст' THEN 'Контекст'
    WHEN channel = 'Соцсети' THEN 'Соцсети'
    WHEN channel = 'Прайс-площадки' THEN 'Прайс-площадки'
    WHEN channel = 'Ретаргетинг' THEN 'Ретаргетинг'
    WHEN channel = 'Флайт S24' THEN 'Флайт S24'
    ELSE 'NaN'
  END