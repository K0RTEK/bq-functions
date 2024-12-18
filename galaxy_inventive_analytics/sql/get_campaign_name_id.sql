### data_group: campaign_name, campaign_id
### procedures.get_campaign_name_id(data_group, campaign)

  CASE

### campaign_name

    WHEN data_group = 'campaign_name' THEN 
    CASE
      WHEN NOT REGEXP_CONTAINS(campaign,r'[a-zа-я]') THEN NULL
      WHEN REGEXP_CONTAINS(LOWER(campaign),r'cn%[0-9]+') THEN REGEXP_EXTRACT(LOWER(campaign),r'cn%.*3a(.*)') 
      ELSE REGEXP_REPLACE(REGEXP_REPLACE(	
    REGEXP_REPLACE(REGEXP_REPLACE(LOWER(campaign),'с','c'),r'.*(cn(:|%))',''), 	
    r'[0-9.]{6,}', ''), r'\|.*','') 
    END
      
### campaign_id
    WHEN data_group = 'campaign_id' THEN 
    CASE
        WHEN REGEXP_CONTAINS(LOWER(campaign),r'cid:{campaign_id}') THEN NULL
        WHEN REGEXP_CONTAINS(LOWER(campaign),r'cid:') THEN REGEXP_EXTRACT(LOWER(campaign),r'cid:([0-9]+)')
        WHEN REGEXP_CONTAINS(LOWER(campaign),r'cid%') THEN REGEXP_EXTRACT(LOWER(campaign),r'([0-9]+)_cn')
        WHEN REGEXP_CONTAINS(LOWER(campaign),r'[0-9]{6,}') THEN REGEXP_EXTRACT(LOWER(campaign),r'[0-9]{6,}')
        WHEN NOT REGEXP_CONTAINS(LOWER(campaign),r'(cid|сid)(:|%)') THEN NULL
    END
  
  END