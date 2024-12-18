IFNULL(
      -- `raw_procedures.cut_url`(utm, "utm_source") AS utm_source,
      -- `raw_procedures.cut_url`(utm, "utm_medium") AS utm_medium,
      -- `raw_procedures.cut_url`(utm, "utm_campaign") AS utm_campaign,
      -- `raw_procedures.cut_url`(utm, "utm_content") AS utm_content,
      -- `raw_procedures.cut_url`(utm, "utm_term") AS utm_term,
        REGEXP_EXTRACT(
          REGEXP_REPLACE(
            REGEXP_REPLACE(
              LOWER(TRIM(url)),
              r'($|&|=)', -- Точно зафиксировать разделители
              'S'), 
            'utm_sourceSS|utm_mediumSS|utm_campaignSS|utm_contentSS|utm_termSS', -- Убрать пустые строки
            ''
          ),
          CONCAT(part,"S(.+?)S")
        ),
        "None"
      )