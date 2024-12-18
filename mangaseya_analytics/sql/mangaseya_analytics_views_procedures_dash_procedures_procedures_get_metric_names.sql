### dash_procedures.get_metric_names(date,cluster_name,subcluster_name,campaign_name,attributes,tags,verify_itog,verify_itog_new)
            CASE
              WHEN cluster_name = 'cabinet' 
                  THEN 'cabinet'
              WHEN cluster_name IN ('calls','leads','requests') 
                  THEN IF(verify_itog,'vco','')
              WHEN cluster_name = 'crm'
                  THEN CASE
                      WHEN subcluster_name = 'naznachennye-pervichnye-vstrechi' 
                          THEN 'appointed_visit'
                      ELSE CONCAT("NaN - ",IFNULL(subcluster_name,''))
                    END
            END