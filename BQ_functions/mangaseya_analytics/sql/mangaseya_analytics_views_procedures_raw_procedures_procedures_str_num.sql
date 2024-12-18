### `agg_procedures.str_num`(numer) as numer,
        -- Используется при экспортах из шитов.
          PARSE_NUMERIC(
            REPLACE(
              IF(TRIM(numer) IN UNNEST(['', '0', ',0', ',00','0,00','0,0','.0', '.00','0.00','0.0']),NULL,TRIM(numer)),
            ",",".")
          )