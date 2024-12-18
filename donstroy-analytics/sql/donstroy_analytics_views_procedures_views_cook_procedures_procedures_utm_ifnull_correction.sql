### cook_procedures.utm_ifnull_correction(utm)

    CASE 
        WHEN utm = 'None' THEN ''
        WHEN utm IS NULL THEN ''
        ELSE LOWER(TRIM(utm))
    END