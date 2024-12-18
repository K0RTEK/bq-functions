### procedures.soc_logic(campaign)
  CASE
    WHEN NOT REGEXP_CONTAINS(LOWER(campaign),r'mg_') THEN 'Докаты'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_int') THEN 'Интересы'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_lal') THEN 'Look-alike'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_grps') THEN 'Подписчики групп'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_kw') THEN 'Ключевые запросы'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_eng') THEN 'Заинтересованная аудитория (ВК)'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_socdem') THEN 'Ограничения по возрасту и полу'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_cart|_сart') THEN 'Добавили в корзину но не купили'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_view') THEN 'Просмотры товаров'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_checkout') THEN 'Начало оформления заказа'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_purch') THEN 'Покупатели'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_all') THEN 'Все взаимодействия с фидом'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_comp') THEN 'Конкуренты (ключи, группы)'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_base') THEN 'База, спиосок клиентов CRM'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_pix') THEN 'Пиксель (для ретаргетинга, LAL)'
    WHEN REGEXP_CONTAINS(LOWER(campaign),r'_wide') THEN 'Привлечение потенциальных клиентов (площадка сама подбирает аудиторию)'
    ELSE CONCAT('NaN - ',campaign)
  END