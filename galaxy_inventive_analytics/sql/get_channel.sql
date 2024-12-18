-- procedures.get_channel(placement)

  CASE 
    WHEN placement IN ('Яндекс Директ', 'Google Ads') THEN 'Контекст' 
    WHEN placement IN ('Facebook', 'МТ', 'Вконтакте', 'ВКР') THEN 'Соцсети'
    WHEN placement = 'Прайс-площадки' THEN 'Прайс-площадки'
    WHEN placement IN ('Соловей', 'Медиаснайпер') THEN 'Ретаргетинг'
    ELSE 'NaN'
  END