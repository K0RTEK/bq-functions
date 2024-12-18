### dash_social.get_parsing_creative(parameter_name,date,ad_name)
  ### parameter_name: project, direction, type, main_targeting, format, visual, utp, month_start
  CASE
    WHEN parameter_name = 'project'
        THEN REGEXP_EXTRACT(ad_name,r'([^_]+)_.*_.*_.*_.*_.*_.*_.*')
    WHEN parameter_name = 'direction'
        THEN REGEXP_EXTRACT(ad_name,r'.*_([^_]+)_.*_.*_.*_.*_.*_.*')
    WHEN parameter_name = 'type'
        THEN REGEXP_EXTRACT(ad_name,r'.*_.*_([^_]+)_.*_.*_.*_.*_.*')
    WHEN parameter_name = 'main_targeting'
        THEN REGEXP_EXTRACT(ad_name,r'.*_.*_.*_([^_]+)_.*_.*_.*_.*')
    WHEN parameter_name = 'format'
        THEN REGEXP_EXTRACT(ad_name,r'.*_.*_.*_.*_([^_]+)_.*_.*_.*')
    WHEN parameter_name = 'visual'
        THEN REGEXP_EXTRACT(ad_name,r'.*_.*_.*_.*_.*_([^_]+)_.*_.*')
    WHEN parameter_name = 'utp'
        THEN REGEXP_EXTRACT(ad_name,r'.*_.*_.*_.*_.*_.*_([^_]+)_.*')
    WHEN parameter_name = 'month_start'
        THEN REGEXP_EXTRACT(ad_name,r'.*_.*_.*_.*_.*_.*_.*_([^_]+)')
  END