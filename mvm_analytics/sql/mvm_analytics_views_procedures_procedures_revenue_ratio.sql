-- procedures.revenue_ratio(mv_eldo_cpa)
-- mv_eldo_cpa: 
-- 'Эльдорадо' кроме CPA, 'М.Видео' кроме CPA, 'CPA' только М.Видео
CASE
      -- Эльдорадо
      WHEN mv_eldo_cpa = 'Эльдорадо' THEN 0.53
      -- М.Видео
      WHEN mv_eldo_cpa = 'М.Видео' THEN 1.2776
      -- CPA
      WHEN mv_eldo_cpa = 'CPA' THEN 1.79
END