### raw_placements.get_traffic_type(parameter)
  CASE		
    WHEN REGEXP_CONTAINS(parameter,r'traf') THEN 'Traffic'
    WHEN REGEXP_CONTAINS(parameter,r'lead') THEN 'LeadAds'
    WHEN REGEXP_CONTAINS(parameter,r'reach') THEN 'Reach'
    ELSE '-'
  END