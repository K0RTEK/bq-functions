### raw_procedures.string_normalization(string)
          CASE
            WHEN LOWER(TRIM(str_field)) IN ('','-',NULL) THEN NULL
            -- WHEN LENGTH(LOWER(TRIM(str_field)))<2 THEN NULL -- Может стоит ещё и это условие прописать
            ELSE LOWER(TRIM(str_field))
          END