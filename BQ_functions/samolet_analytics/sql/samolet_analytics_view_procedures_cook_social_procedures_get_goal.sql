-- cook_social.get_goal(type,goal)
CASE
  ### И живи-ка
  WHEN REGEXP_CONTAINS(LOWER(goal),r'309324554') 
    THEN CASE
        WHEN type = 'col_name' THEN 'izhivika_goal309324554'
        WHEN type = 'project' THEN 'И живи-ка'
        ELSE 'Успешное бронирование'
      END
  WHEN REGEXP_CONTAINS(LOWER(goal),r'308760363') 
    THEN CASE
        WHEN type = 'col_name' THEN 'izhivika_goal308760363'
        WHEN type = 'project' THEN 'И живи-ка'
        ELSE 'Клик на Закажите консультацию'
      END
  WHEN REGEXP_CONTAINS(LOWER(goal),r'326313875') 
    THEN CASE
        WHEN type = 'col_name' THEN 'izhivika_goal326313875'
        WHEN type = 'project' THEN 'И живи-ка'
        ELSE 'Выбрать квартиру (шаг 1)'
      END
  WHEN REGEXP_CONTAINS(LOWER(goal),r'326313876') 
    THEN CASE
        WHEN type = 'col_name' THEN 'izhivika_goa326313876'
        WHEN type = 'project' THEN 'И живи-ка'
        ELSE 'Выбор квартиры. Бронирование: Шаг 2 - Клик на кнопку “Забронировать”'
      END
  WHEN REGEXP_CONTAINS(LOWER(goal),r'326313877') 
    THEN CASE
        WHEN type = 'col_name' THEN 'izhivika_goal326313877'
        WHEN type = 'project' THEN 'И живи-ка'
        ELSE 'Выбор квартиры. Бронирование: Шаг 3 - Клик на кнопку “Начать бронирование”'
      END
  WHEN REGEXP_CONTAINS(LOWER(goal),r'326313878') 
    THEN CASE
        WHEN type = 'col_name' THEN 'izhivika_goal326313878'
        WHEN type = 'project' THEN 'И живи-ка'
        ELSE 'Успешное бронирование (шаг 4)'
      END
  WHEN REGEXP_CONTAINS(LOWER(goal),r'326190310') 
    THEN CASE
        WHEN type = 'col_name' THEN 'izhivika_goal326190310'
        WHEN type = 'project' THEN 'И живи-ка'
        ELSE 'Вереск Лист ожидания клик'
      END
  WHEN REGEXP_CONTAINS(LOWER(goal),r'326136175') 
    THEN CASE
        WHEN type = 'col_name' THEN 'izhivika_goal326136175'
        WHEN type = 'project' THEN 'И живи-ка'
        ELSE 'Вереск Лист ожидания'
      END
  WHEN REGEXP_CONTAINS(LOWER(goal),r'326982523') 
    THEN CASE
        WHEN type = 'col_name' THEN 'izhivika_goal326982523'
        WHEN type = 'project' THEN 'И живи-ка'
        ELSE 'Мята Лист ожидания клик'
      END
  WHEN REGEXP_CONTAINS(LOWER(goal),r'326982434') 
    THEN CASE
        WHEN type = 'col_name' THEN 'izhivika_goal326982434'
        WHEN type = 'project' THEN 'И живи-ка'
        ELSE 'Мята Лист ожидания'
      END
  ### Целепорт
  WHEN REGEXP_CONTAINS(LOWER(goal),r'316924482') 
    THEN CASE
        WHEN type = 'col_name' THEN 'izhivika_goal316924482'
        WHEN type = 'project' THEN 'Целепорт'
        ELSE 'Отправка формы и паспортных данных и ИНН (шаг 4)'
      END
  WHEN REGEXP_CONTAINS(LOWER(goal),r'316924334') 
    THEN CASE
        WHEN type = 'col_name' THEN 'izhivika_goal316924334'
        WHEN type = 'project' THEN 'Целепорт'
        ELSE 'Клик на Открыть Целепорт (шаг 1)'
      END
  WHEN REGEXP_CONTAINS(LOWER(goal),r'317614125') 
    THEN CASE
        WHEN type = 'col_name' THEN 'izhivika_goal317614125'
        WHEN type = 'project' THEN 'Целепорт'
        ELSE 'Отправка номера (шаг 2)'
      END
  WHEN REGEXP_CONTAINS(LOWER(goal),r'317614126') 
    THEN CASE
        WHEN type = 'col_name' THEN 'izhivika_goal317614126'
        WHEN type = 'project' THEN 'Целепорт'
        ELSE 'Клик на отправку формы (шаг 3)'
      END
  WHEN REGEXP_CONTAINS(LOWER(goal),r'317612819') 
    THEN CASE
        WHEN type = 'col_name' THEN 'izhivika_goal317612819'
        WHEN type = 'project' THEN 'Целепорт'
        ELSE 'Открыть Целепорт (шаг 1)'
      END
  WHEN REGEXP_CONTAINS(LOWER(goal),r'317612820') 
    THEN CASE
        WHEN type = 'col_name' THEN 'izhivika_goal317612820'
        WHEN type = 'project' THEN 'Целепорт'
        ELSE 'Отправка номера (шаг 2)'
      END
  WHEN REGEXP_CONTAINS(LOWER(goal),r'317612821') 
    THEN CASE
        WHEN type = 'col_name' THEN 'izhivika_goal317612821'
        WHEN type = 'project' THEN 'Целепорт'
        ELSE 'Отправка формы и паспортных данных и ИНН (шаг 3)'
      END
  ### Формула счастья
  WHEN REGEXP_CONTAINS(LOWER(goal),r'322894105') 
    THEN CASE
        WHEN type = 'col_name' THEN 'izhivika_goal322894105'
        WHEN type = 'project' THEN 'Формула счастья'
        ELSE 'Финишная страница, опрос завершен'
      END
  ### Самолетум
  WHEN REGEXP_CONTAINS(LOWER(goal),r'309413255') 
    THEN CASE
        WHEN type = 'col_name' THEN 'samoletum_goal309413255'
        WHEN type = 'project' THEN 'Самолетум'
        ELSE 'Отправка формы и паспортных данных и ИНН (шаг 4)'
      END
  WHEN REGEXP_CONTAINS(LOWER(goal),r'323715942') 
    THEN CASE
        WHEN type = 'col_name' THEN 'samoletum_goal323715942'
        WHEN type = 'project' THEN 'Самолетум'
        ELSE 'Клик на Открыть Целепорт (шаг 1)'
      END
  WHEN REGEXP_CONTAINS(LOWER(goal),r'329183103') 
    THEN CASE
        WHEN type = 'col_name' THEN 'samoletum_goal329183103'
        WHEN type = 'project' THEN 'Самолетум'
        ELSE 'Отправка номера (шаг 2)'
      END
  WHEN REGEXP_CONTAINS(LOWER(goal),r'326177868') 
    THEN CASE
        WHEN type = 'col_name' THEN 'samoletum_goal326177868'
        WHEN type = 'project' THEN 'Самолетум'
        ELSE 'Клик на отправку формы (шаг 3)'
      END
  ### Загород фест
  WHEN REGEXP_CONTAINS(LOWER(goal),r'336485646') 
    THEN CASE
        WHEN type = 'col_name' THEN 'zagorodfest_goal336485646' ### Лиды
        WHEN type = 'project' THEN 'Загород Fest'
        ELSE 'Клики по "Хочу на фестиваль" в шапке сайта'
      END
  WHEN REGEXP_CONTAINS(LOWER(goal),r'336486040') 
    THEN CASE
        WHEN type = 'col_name' THEN 'zagorodfest_goal336486040' ### Лиды
        WHEN type = 'project' THEN 'Загород Fest'
        ELSE 'Клик по кнопке "Хочу на фестиваль" в блоке с таймером'
      END
  WHEN REGEXP_CONTAINS(LOWER(goal),r'336486196') 
    THEN CASE
        WHEN type = 'col_name' THEN 'zagorodfest_goal336486196' ### Лиды
        WHEN type = 'project' THEN 'Загород Fest'
        ELSE 'Клик по кнопке "Хочу на фестиваль" в форме'
      END
  WHEN REGEXP_CONTAINS(LOWER(goal),r'336487337') 
    THEN CASE
        WHEN type = 'col_name' THEN 'zagorodfest_goal336487337' ### ПЦЗ
        WHEN type = 'project' THEN 'Загород Fest'
        ELSE 'Отправка форм c поддомена fest.samolet.ru'
      END
    ELSE CONCAT('NaN - ',goal)
END