### cook_procedures.get_object(parameter)

CASE
    WHEN REGEXP_CONTAINS(LOWER(TRIM(parameter)), r'на.речном|na.rechnom') THEN 'Мангазея на Речном'


    ELSE 'Не определено'
    END