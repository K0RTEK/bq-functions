### data_group: campaign_name, campaign_id
### procedures.get_campaign_name_id(data_group, campaign)

  CASE

### campaign_name

    WHEN data_group = 'campaign_name' THEN 
    CASE
      WHEN NOT REGEXP_CONTAINS(campaign,r'cn|сn') AND REGEXP_CONTAINS(campaign,r'cid|сid') THEN NULL
      ELSE REGEXP_REPLACE(REGEXP_REPLACE(	
    REGEXP_REPLACE(REGEXP_REPLACE(LOWER(campaign),'с','c'),r'.*(cn(:|%))',''), 	
    r'[0-9.]{6,}_', ''), r'\|.*','') 
    END
      
### campaign_id
  WHEN data_group = 'campaign_id' THEN 
    REGEXP_REPLACE(REGEXP_REPLACE(	
    REGEXP_REPLACE(REGEXP_REPLACE(LOWER(campaign),'с','c'),r'.*(cid(:|%))',''), 	
    r'[a-zа-я._]+', ''), r'\|.*','')

  END