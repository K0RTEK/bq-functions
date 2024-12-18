### dash_procedures.get_adv_owner(date,project,source,medium,campaign,content,term) 
    CASE 
      ### Контекст 
      WHEN  date >= '2024-01-01' AND project = 'mvideo' AND source = 'yandex' AND medium = 'cpc' AND NOT REGEXP_CONTAINS(LOWER(campaign),r'flight')  
        THEN 'non-MGCom' 
 
      WHEN date BETWEEN '2023-11-01' AND '2023-12-31' AND project = 'mvideo' AND source = 'yandex' AND medium = 'cpc' AND  
      ( 
        REGEXP_CONTAINS(LOWER(campaign),r'_api_') OR  
        (REGEXP_CONTAINS(LOWER(campaign),r'_image_name|_brand') AND NOT REGEXP_CONTAINS(LOWER(campaign),r'_s_')) OR  
        (REGEXP_CONTAINS(LOWER(campaign),r'_s_|brand_s') AND NOT REGEXP_CONTAINS(LOWER(campaign),r'smartbanners|_rem')) OR  
        (REGEXP_CONTAINS(LOWER(campaign),r'_p_') AND REGEXP_CONTAINS(LOWER(campaign),r'_cat-ven_|_cat_|_category_|_hand_|autotarget|keywords|compet')) 
      ) 
        THEN 'non-MGCom' 
      WHEN date BETWEEN '2023-02-01' AND '2023-11-01' AND project = 'mvideo' AND source = 'yandex' AND medium = 'cpc' AND NOT REGEXP_CONTAINS(LOWER(campaign),r'flight') AND REGEXP_CONTAINS(LOWER(campaign),r'image')  
        THEN 'non-MGCom' 
 
      WHEN date BETWEEN '2023-02-01' AND '2023-10-01' AND project = 'eldorado' AND source = 'yandex' AND medium = 'cpc' AND NOT REGEXP_CONTAINS(LOWER(campaign),r'flight') AND REGEXP_CONTAINS(LOWER(campaign),r'dsa|_tk_|_smartbanners_|image|_autotarget_|yandex_shopping_segmented_')  
        THEN 'non-MGCom' 
      WHEN date >= '2023-10-01' AND project = 'eldorado' AND source = 'yandex' AND medium = 'cpc' 
        THEN 'non-MGCom' 
 
      ### CPA 
      WHEN medium = 'cpa' 
        THEN 'non-MGCom' 
 
      ### Органик 
      WHEN (source LIKE '%yandex%' AND medium IN ('organic','referral')) OR (source LIKE '%google%' AND medium = 'organic') 
        THEN 'non-MGCom' 
 
###### Условия для План-Фактов 
      ### non-MGCom 
      WHEN date >= '2023-10-01' AND (project = 'eldorado' AND source = 'Контекст') 
       THEN 'non-MGCom' 
 
      WHEN date BETWEEN '2023-02-01' AND '2023-10-01' AND (project = 'eldorado' AND campaign IN ('Яндекс Бренд','Яндекс DSA','Яндекс Смартбаннеры','Яндекс Товарная РК')) 
        THEN 'non-MGCom' 
 
      WHEN date >= '2024-01-01' AND (project = 'mvideo' AND source = 'Контекст') 
        THEN 'non-MGCom'  
       
      WHEN date BETWEEN '2023-11-01' AND '2023-12-31' AND (project = 'mvideo' AND campaign IN ('Яндекс Бренд (общий)','Яндекс Api (к50)','Яндекс РСЯ (CPC)','Яндекс Категорийные РК (модельные+катвенд) + Автотаргет')) 
        THEN 'non-MGCom' 
 
      WHEN date BETWEEN '2023-02-01' AND '2023-11-01' AND (project = 'mvideo' AND campaign IN ('Яндекс Бренд (общий)')) 
        THEN 'non-MGCom' 
       
         
      ELSE 'MGCom' 
    END