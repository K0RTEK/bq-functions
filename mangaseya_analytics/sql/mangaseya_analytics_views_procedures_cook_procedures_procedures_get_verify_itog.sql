### cook_procedures.get_verify_itog(tags,attributes)
          CASE
            WHEN REGEXP_CONTAINS(LOWER(tags),r'"уцо"|"уцо_мангазея|уцо_mgcom"') 
              THEN true
            ELSE false
          END