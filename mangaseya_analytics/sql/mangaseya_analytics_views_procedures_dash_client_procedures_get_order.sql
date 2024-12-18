CASE 
  /*
  dash_client.get_order`('channel_order', channel, placement) as channel_order
  dash_client.get_order`('placement_order', channel, placement) as placement_order
  */
  WHEN order_type = 'channel_order' THEN
    CASE
    WHEN LOWER(TRIM(channel)) = 'базы недвижимости' THEN 1500
    WHEN LOWER(TRIM(channel)) = 'геосервисы' THEN 2700
    WHEN LOWER(TRIM(channel)) = 'контекстная реклама' THEN 300
    WHEN LOWER(TRIM(channel)) = 'медийная реклама' THEN 3300
    WHEN LOWER(TRIM(channel)) = 'социальные сети' THEN 2100
    WHEN LOWER(TRIM(channel)) = 'тематические порталы' THEN 900
    ELSE 9900
  END
  WHEN order_type = 'placement_order' THEN
    CASE
    WHEN LOWER(TRIM(placement)) = '1000novostroek' THEN 120
    WHEN LOWER(TRIM(placement)) = '2realty' THEN 110
    WHEN LOWER(TRIM(placement)) = 'adsmart duo client' THEN 290
    WHEN LOWER(TRIM(placement)) = 'avaho' THEN 30
    WHEN LOWER(TRIM(placement)) = 'cian' THEN 140
    WHEN LOWER(TRIM(placement)) = 'cian' THEN 270
    WHEN LOWER(TRIM(placement)) = 'dcreo' THEN 300
    WHEN LOWER(TRIM(placement)) = 'gdeetotdom' THEN 40
    WHEN LOWER(TRIM(placement)) = 'gogethome' THEN 90
    WHEN LOWER(TRIM(placement)) = 'kommersant' THEN 280
    WHEN LOWER(TRIM(placement)) = 'mskguru + novostroy-gid' THEN 100
    WHEN LOWER(TRIM(placement)) = 'novomoscow' THEN 80
    WHEN LOWER(TRIM(placement)) = 'novostroy-m' THEN 50
    WHEN LOWER(TRIM(placement)) = 'novostroycity' THEN 60
    WHEN LOWER(TRIM(placement)) = 'pronovostroyki' THEN 70
    WHEN LOWER(TRIM(placement)) = 'vedomosti' THEN 260
    WHEN LOWER(TRIM(placement)) = 'yandex (посевы в телеграм)' THEN 210
    WHEN LOWER(TRIM(placement)) = 'авито' THEN 160
    WHEN LOWER(TRIM(placement)) = 'домклик' THEN 170
    WHEN LOWER(TRIM(placement)) = 'новострой-м' THEN 180
    WHEN LOWER(TRIM(placement)) = 'промостраницы' THEN 310
    WHEN LOWER(TRIM(placement)) = 'социальные сети telegram ads | data мтс' THEN 200
    WHEN LOWER(TRIM(placement)) = 'я.карты' THEN 240
    WHEN LOWER(TRIM(placement)) = 'я.навигатор' THEN 230
    WHEN LOWER(TRIM(placement)) = 'яндекс.директ' THEN 10
    WHEN LOWER(TRIM(placement)) = 'яндекс.недвижимость' THEN 150
    ELSE 9900
  END
  ELSE 9900
END