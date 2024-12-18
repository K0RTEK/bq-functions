### cook_procedures.get_verify_itog(tags)
          CASE
            WHEN REGEXP_CONTAINS(LOWER(tags),r'целевой') 
              AND NOT REGEXP_CONTAINS(LOWER(tags),r'нецелевой|не целевой') 
              THEN true
            ELSE false
          END