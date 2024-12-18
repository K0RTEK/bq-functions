### agg_procedures.get_channel`(date,ct_source,ct_medium,crm_advertising_source,utm_source,utm_medium,utm_campaign,utm_content,utm_term)
  CASE
    WHEN LOWER(ct_source) = '(direct)' OR LOWER(ct_medium) IN ('organic','referral') OR LOWER(crm_advertising_source) = 'сайт %'
      THEN 'Органик'

    WHEN LOWER(utm_medium) = 'cpc' AND REGEXP_CONTAINS(LOWER(utm_source),r'yandex|google') 
      THEN 'Контекстная реклама'

    WHEN LOWER(utm_medium) = 'calls' AND REGEXP_CONTAINS(LOWER(utm_source),r'context_yandex_google') 
      THEN 'Контекстная реклама'

    WHEN LOWER(utm_medium) = 'cpa' OR REGEXP_CONTAINS(LOWER(utm_source),r'_lead') OR REGEXP_CONTAINS(LOWER(crm_advertising_source),r' лид') 
      THEN 'Лидогенераторы'

    WHEN REGEXP_CONTAINS(LOWER(crm_advertising_source),r'mediapronet|аквариус') OR REGEXP_CONTAINS(LOWER(utm_source),r'mediapronet|aquarius') 
      THEN 'Базы'

    WHEN LOWER(utm_medium) = 'cpm' AND REGEXP_CONTAINS(LOWER(utm_source),r'hybrid|premium_id_investors|smart_data_premium') 
      THEN 'Программатик'

    ### Охватные ресурсы
    WHEN REGEXP_CONTAINS(LOWER(utm_source),r'2gis') AND LOWER(utm_medium) IN ('calls','statika') THEN 'Охватные ресурсы'
    WHEN LOWER(crm_advertising_source) = '2gis' THEN 'Охватные ресурсы'
    WHEN REGEXP_CONTAINS(LOWER(utm_source),r'yandex.maps|navigator|yandex.ru_karty_navigator|yandex_geoservice') AND LOWER(utm_medium) IN ('calls','statika','kartochka','cpm') THEN 'Охватные ресурсы'
    WHEN LOWER(crm_advertising_source) = 'yandex.ru карты и навигатор' THEN 'Охватные ресурсы'
    WHEN REGEXP_CONTAINS(LOWER(utm_source),r'realty.yandex|yandex.ru_spravochnik') AND LOWER(utm_medium) IN ('calls','cpm') THEN 'Охватные ресурсы'
    WHEN LOWER(crm_advertising_source) = 'yandex.ru справочник' THEN 'Охватные ресурсы'
    WHEN REGEXP_CONTAINS(LOWER(utm_source),r'google.maps|google.com_karty') AND LOWER(utm_medium) IN ('calls','kartochka') THEN 'Охватные ресурсы'
    WHEN LOWER(crm_advertising_source) = 'google.com карты' THEN 'Охватные ресурсы'
    WHEN REGEXP_CONTAINS(LOWER(utm_source),r'afisha') AND LOWER(utm_medium) = 'cpm' THEN 'Охватные ресурсы'
    WHEN REGEXP_CONTAINS(LOWER(utm_source),r'bfm') AND LOWER(utm_medium) = 'cpm' THEN 'Охватные ресурсы'
    WHEN REGEXP_CONTAINS(LOWER(utm_source),r'cian') AND LOWER(utm_medium) = 'cpm' THEN 'Охватные ресурсы'
    WHEN REGEXP_CONTAINS(LOWER(utm_source),r'forbes') AND LOWER(utm_medium) = 'cpm' THEN 'Охватные ресурсы'
    WHEN REGEXP_CONTAINS(LOWER(utm_source),r'megafon') AND LOWER(utm_medium) = 'push' THEN 'Охватные ресурсы'
    WHEN REGEXP_CONTAINS(LOWER(utm_source),r'interpool') AND LOWER(utm_medium) IN ('push','cpm') THEN 'Охватные ресурсы'
    WHEN REGEXP_CONTAINS(LOWER(utm_source),r'kommersant') AND LOWER(utm_medium) = 'cpm' THEN 'Охватные ресурсы'
    WHEN REGEXP_CONTAINS(LOWER(utm_source),r'lenta') AND LOWER(utm_medium) = 'cpm' THEN 'Охватные ресурсы'
    WHEN REGEXP_CONTAINS(LOWER(utm_source),r'mts') AND LOWER(utm_medium) = 'push' THEN 'Охватные ресурсы'
    WHEN REGEXP_CONTAINS(LOWER(utm_source),r'one_target') AND LOWER(utm_medium) = 'cpm' THEN 'Охватные ресурсы'
    WHEN REGEXP_CONTAINS(LOWER(utm_source),r'rbc') AND LOWER(utm_medium) = 'cpm' THEN 'Охватные ресурсы'
    WHEN LOWER(crm_advertising_source) = 'rbc.ru баннер' THEN 'Охватные ресурсы'
    WHEN REGEXP_CONTAINS(LOWER(utm_source),r'timeout') AND LOWER(utm_medium) = 'cpm' THEN 'Охватные ресурсы'
    WHEN REGEXP_CONTAINS(LOWER(utm_source),r'vc_desktop|vc_mobile|vc.ru') AND LOWER(utm_medium) = 'cpm' THEN 'Охватные ресурсы'
    WHEN REGEXP_CONTAINS(LOWER(utm_source),r'vedomosti') AND LOWER(utm_medium) = 'cpm' THEN 'Охватные ресурсы'
    WHEN REGEXP_CONTAINS(LOWER(utm_source),r'incrussia') AND LOWER(utm_medium) = 'push' THEN 'Охватные ресурсы'

    ### Тематические площадки
    WHEN REGEXP_CONTAINS(LOWER(utm_source),r'101novostroyka') AND LOWER(utm_medium) IN ('calls','statika') THEN 'Тематические площадки'
    WHEN LOWER(crm_advertising_source) = '101novostroyka.ru тгб' THEN 'Тематические площадки'
    WHEN REGEXP_CONTAINS(LOWER(utm_source),r'1dom') AND LOWER(utm_medium) = 'statika' THEN 'Тематические площадки'
    WHEN REGEXP_CONTAINS(LOWER(utm_source),r'aurumrealty') AND LOWER(utm_medium) IN ('calls','statika') THEN 'Тематические площадки'
    WHEN LOWER(crm_advertising_source) = 'aurumrealty.ru тгб' THEN 'Тематические площадки'
    WHEN REGEXP_CONTAINS(LOWER(utm_source),r'avaho') AND LOWER(utm_medium) IN ('calls','statika') THEN 'Тематические площадки'
    WHEN LOWER(crm_advertising_source) = 'avaho.ru тгб' THEN 'Тематические площадки'
    WHEN REGEXP_CONTAINS(LOWER(utm_source),r'businessclass.moscow') AND LOWER(utm_medium) IN ('calls','statika') THEN 'Тематические площадки'
    WHEN LOWER(crm_advertising_source) IN ('businessclass.moscow баннер','businessclass.moscow тгб') THEN 'Тематические площадки'
    WHEN REGEXP_CONTAINS(LOWER(utm_source),r'dommsk') AND LOWER(utm_medium) IN ('calls','statika','cpm') THEN 'Тематические площадки'
    WHEN LOWER(crm_advertising_source) = 'dommsk.ru тгб' THEN 'Тематические площадки'
    WHEN REGEXP_CONTAINS(LOWER(utm_source),r'gogethome') AND LOWER(utm_medium) IN ('cpm','statika') THEN 'Тематические площадки'
    WHEN LOWER(crm_advertising_source) = 'gogethome.ru баннер' THEN 'Тематические площадки'
    WHEN REGEXP_CONTAINS(LOWER(utm_source),r'kdo') AND LOWER(utm_medium) = 'statika' THEN 'Тематические площадки'
    WHEN REGEXP_CONTAINS(LOWER(utm_source),r'kvartyroom') AND LOWER(utm_medium) IN ('cpm','calls','statika') THEN 'Тематические площадки'
    WHEN LOWER(crm_advertising_source) = 'kvartyroom.ru тгб' THEN 'Тематические площадки'
    WHEN REGEXP_CONTAINS(LOWER(utm_source),r'lifedeluxe') AND LOWER(utm_medium) IN ('cpm','calls','statika') THEN 'Тематические площадки'
    WHEN LOWER(crm_advertising_source) = 'lifedeluxe.ru тгб' THEN 'Тематические площадки'
    WHEN REGEXP_CONTAINS(LOWER(utm_source),r'mosdom') AND LOWER(utm_medium) IN ('cpm','statika') THEN 'Тематические площадки'
    WHEN LOWER(crm_advertising_source) = 'mosdom.ru тгб' THEN 'Тематические площадки'
    WHEN REGEXP_CONTAINS(LOWER(utm_source),r'move') AND LOWER(utm_medium) IN ('cpm','calls','statika') THEN 'Тематические площадки'
    WHEN LOWER(crm_advertising_source) = 'move.ru спецпроект' THEN 'Тематические площадки'
    WHEN REGEXP_CONTAINS(LOWER(utm_source),r'msk-novostroyki') AND LOWER(utm_medium) IN ('cpm','calls','statika') THEN 'Тематические площадки'
    WHEN LOWER(crm_advertising_source) = 'msk-novostroyki.ru тгб' THEN 'Тематические площадки'
    WHEN REGEXP_CONTAINS(LOWER(utm_source),r'myburg.su') AND LOWER(utm_medium) = 'cpm' THEN 'Тематические площадки'
    WHEN REGEXP_CONTAINS(LOWER(utm_source),r'myburg') AND LOWER(utm_medium) IN ('cpm','calls','statika') THEN 'Тематические площадки'
    WHEN LOWER(crm_advertising_source) = 'myburg.ru тгб' THEN 'Тематические площадки'
    WHEN REGEXP_CONTAINS(LOWER(utm_source),r'novomoscow') AND LOWER(utm_medium) IN ('calls','statika') THEN 'Тематические площадки'
    WHEN LOWER(crm_advertising_source) = 'novomoscow.ru тгб' THEN 'Тематические площадки'
    WHEN REGEXP_CONTAINS(LOWER(utm_source),r'novostroev') AND LOWER(utm_medium) IN ('cpm','calls','statika') THEN 'Тематические площадки'
    WHEN LOWER(crm_advertising_source) = 'novostroev.ru баннер' THEN 'Тематические площадки'
    WHEN REGEXP_CONTAINS(LOWER(utm_source),r'novostroy-gid') AND LOWER(utm_medium) = 'statika' THEN 'Тематические площадки'
    WHEN REGEXP_CONTAINS(LOWER(utm_source),r'novostroy-m') AND LOWER(utm_medium) IN ('calls','statika') THEN 'Тематические площадки'
    WHEN LOWER(crm_advertising_source) IN ('novostroy-m.ru спецпроект','novostroy-m.ru спецпредложение') THEN 'Тематические площадки'
    WHEN REGEXP_CONTAINS(LOWER(utm_source),r'novostroycity') AND LOWER(utm_medium) IN ('cpm','statika') THEN 'Тематические площадки'
    WHEN LOWER(crm_advertising_source) = 'novostroycity.ru тгб' THEN 'Тематические площадки'
    WHEN REGEXP_CONTAINS(LOWER(utm_source),r'poisk-novostroyki') AND LOWER(utm_medium) IN ('cpm','calls','statika') THEN 'Тематические площадки'
    WHEN LOWER(crm_advertising_source) = 'poisk-novostroyki.ru тгб' THEN 'Тематические площадки'
    WHEN REGEXP_CONTAINS(LOWER(utm_source),r'novostroy') AND LOWER(utm_medium) = 'cpm' THEN 'Тематические площадки'
    WHEN REGEXP_CONTAINS(LOWER(utm_source),r'realestate') AND LOWER(utm_medium) IN ('cpm','calls','statika') THEN 'Тематические площадки'
    WHEN LOWER(crm_advertising_source) = 'realestate.ru тгб' THEN 'Тематические площадки'
    WHEN REGEXP_CONTAINS(LOWER(utm_source),r'realtymag') AND LOWER(utm_medium) IN ('cpm','calls','statika') THEN 'Тематические площадки'
    WHEN LOWER(crm_advertising_source) = 'realtymag.ru тгб' THEN 'Тематические площадки'
    WHEN REGEXP_CONTAINS(LOWER(utm_source),r'realtystreet') AND LOWER(utm_medium) = 'statika' THEN 'Тематические площадки'
    WHEN REGEXP_CONTAINS(LOWER(utm_source),r'russianrealty') AND LOWER(utm_medium) IN ('calls','statika') THEN 'Тематические площадки'
    WHEN LOWER(crm_advertising_source) = 'russianrealty.ru тгб' THEN 'Тематические площадки'
    WHEN REGEXP_CONTAINS(LOWER(utm_source),r'2realty') AND LOWER(utm_medium) = 'statika' THEN 'Тематические площадки'
    WHEN REGEXP_CONTAINS(LOWER(utm_source),r'realty') AND LOWER(utm_medium) IN ('cpm','calls','statika') THEN 'Тематические площадки'
    WHEN LOWER(crm_advertising_source) = 'realty.ru баннер' THEN 'Тематические площадки'
    WHEN REGEXP_CONTAINS(LOWER(utm_source),r'reforum') AND LOWER(utm_medium) = 'statika' THEN 'Тематические площадки'
    WHEN LOWER(crm_advertising_source) = 'reforum.ru тгб' THEN 'Тематические площадки'
    WHEN REGEXP_CONTAINS(LOWER(utm_source),r'rendv') AND LOWER(utm_medium) IN ('cpm','calls','statika') THEN 'Тематические площадки'
    WHEN LOWER(crm_advertising_source) = 'rendv.ru тгб' THEN 'Тематические площадки'
    WHEN REGEXP_CONTAINS(LOWER(utm_source),r'restate') AND LOWER(utm_medium) IN ('calls','statika') THEN 'Тематические площадки'
    WHEN LOWER(crm_advertising_source) = 'restate.ru спецпроект' THEN 'Тематические площадки'
    WHEN REGEXP_CONTAINS(LOWER(utm_source),r'stroynov') AND LOWER(utm_medium) IN ('cpm','calls','statika') THEN 'Тематические площадки'
    WHEN LOWER(crm_advertising_source) = 'stroynov спецпроект' THEN 'Тематические площадки'
    WHEN REGEXP_CONTAINS(LOWER(utm_source),r'topnovostroek') AND LOWER(utm_medium) IN ('calls','statika') THEN 'Тематические площадки'
    WHEN LOWER(crm_advertising_source) = 'topnovostroek.ru тгб' THEN 'Тематические площадки'
    WHEN REGEXP_CONTAINS(LOWER(utm_source),r'vsenovostroyki') AND LOWER(utm_medium) = 'cpm' THEN 'Тематические площадки'
    WHEN REGEXP_CONTAINS(LOWER(utm_source),r'irn_metrinfo_realsearch') AND LOWER(utm_medium) = 'statika' THEN 'Тематические площадки'
    WHEN REGEXP_CONTAINS(LOWER(utm_source),r'kvartirny-control') AND LOWER(utm_medium) = 'statika' THEN 'Тематические площадки'
    WHEN REGEXP_CONTAINS(LOWER(utm_source),r'mskguru') AND LOWER(utm_medium) = 'statika' THEN 'Тематические площадки'
    WHEN REGEXP_CONTAINS(LOWER(utm_source),r'naydikvartiru') AND LOWER(utm_medium) = 'statika' THEN 'Тематические площадки'
    WHEN REGEXP_CONTAINS(LOWER(utm_source),r'elitnoe') AND LOWER(utm_medium) = 'statika' THEN 'Тематические площадки'
    WHEN REGEXP_CONTAINS(LOWER(utm_source),r'mirkvartir') AND LOWER(utm_medium) = 'statika' THEN 'Тематические площадки'
    WHEN REGEXP_CONTAINS(LOWER(utm_source),r'eip') AND LOWER(utm_medium) = 'statika' THEN 'Тематические площадки'
    WHEN REGEXP_CONTAINS(LOWER(utm_source),r'gdeetotdom') AND LOWER(utm_medium) = 'statika' THEN 'Тематические площадки'
    WHEN REGEXP_CONTAINS(LOWER(utm_source),r'novostroy-rf') AND LOWER(utm_medium) = 'statika' THEN 'Тематические площадки'
    WHEN REGEXP_CONTAINS(LOWER(utm_source),r'novostroyki.pro') AND LOWER(utm_medium) IN ('cpm','statika') THEN 'Тематические площадки'

    WHEN crm_advertising_source IN (
      'Наружная Реклама',
      'Не определено',
      'Обзвон холодных',
      'Обзвон купивших \\ бизнес',
      'Обзвон купивших \\ премиум',
      'VKontakte лидген магазина',
      'ВТБ Сотрудники',
      'КРОК Сотрудники',
      'Оформление объектов',
      'Регионы ЭТАЖИ агентство',
      'Телеграмм для сотрудников',
      'Whatsup чат интеллект',
      'АльфаСтрахование',
      'Аквариус Na100Pro машиноместа',
      'Буклеты офис',
      'ВТБ Private banking',
      'Зарплатные клиенты/ Привилегии ВТБ',
      'Знакомые / друзья',
      'Лидогенерация Whatsapp',
      'МТС private premium',
      'РБК Дэйли газета',
      'Регионы М2 агентство',
      'Ситибанк Сотрудники',
      'Тинькофф',
      'ЦФТ сотрудники',
      'Яндекс сотрудники',
      'x5 retail group Сотрудники'
    )
      THEN 'Ненужное'
    ELSE 'Другое'
  END