CASE

### agg_procedures.get_cpa_cost_coeff(date , project, utm_source, utm_medium, utm_campaign, utm_content, utm_term)

    ### advcake 
    
    ### mvideo 
    WHEN project = 'mvideo' THEN
        CASE
            WHEN REGEXP_CONTAINS(LOWER(utm_source),r'advcake|tinkoff') AND utm_medium = 'cpa'
                AND date < '2023-07-01'
                THEN 0.55*0.047/1.2
            WHEN REGEXP_CONTAINS(LOWER(utm_source),r'advcake|tinkoff') AND utm_medium = 'cpa'
                AND date >= '2023-07-01'
                THEN 0.04*0.7/1.2
        ELSE 1
    END

    ### eldorado 
    WHEN project = 'eldorado' THEN
        CASE
            WHEN REGEXP_CONTAINS(LOWER(utm_source),r'advcake|tinkoff') AND utm_medium = 'cpa'
                AND date < '2023-07-01'
                THEN 0.55*0.047/1.2
            WHEN REGEXP_CONTAINS(LOWER(utm_source),r'advcake|tinkoff') AND utm_medium = 'cpa'
                AND date >= '2023-07-01'
                THEN 0.04*0.65/1.2
        ELSE 1
    END
    
    ELSE 1

END