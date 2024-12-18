import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def utm_decode(parameter, utm_content):
    parameter = is_none(parameter)
    utm_content = is_none(utm_content)

    # Приводим utm_content к нижнему регистру, удаляем пробелы и заменяем разделители
    cleaned_content = re.sub(r'(^|$| |\||%7|:)', 'S', utm_content.strip())

    if parameter == 'campaign_id':
        return re.search(r'ScS*(.+?)S', cleaned_content).group(1) if re.search(r'ScS*(.+?)S', cleaned_content) else None
    elif parameter == 'ad_group_id':
        return re.search(r'SgS*(.+?)S', cleaned_content).group(1) if re.search(r'SgS*(.+?)S', cleaned_content) else None
    elif parameter == 'ad_id':
        return re.search(r'SaS*(.+?)S', cleaned_content).group(1) if re.search(r'SaS*(.+?)S', cleaned_content) else None
    elif parameter == 'criterion_id':
        return re.search(r'SpidS*(.+?)S', cleaned_content).group(1) if re.search(r'SpidS*(.+?)S',
                                                                                 cleaned_content) else None
    elif parameter == 'device':
        return re.search(r'SdevS*(.+?)S', cleaned_content).group(1) if re.search(r'SdevS*(.+?)S',
                                                                                 cleaned_content) else None
    elif parameter == 'direct_placement':
        return re.search(r'SsS*(.+?)S', cleaned_content).group(1) if re.search(r'SsS*(.+?)S', cleaned_content) else None
    elif parameter == 'region_id':
        return re.search(r'SgeoidS*(.+?)S', cleaned_content).group(1) if re.search(r'SgeoidS*(.+?)S',
                                                                                   cleaned_content) else None
    elif parameter == 'banner_id':
        return re.search(r'SbS*(.+?)S', cleaned_content).group(1) if re.search(r'SbS*(.+?)S', cleaned_content) else None
    elif parameter == 'position':
        return re.search(r'SpS*(.+?)S', cleaned_content).group(1) if re.search(r'SpS*(.+?)S', cleaned_content) else None
    elif parameter == 'position_type':
        return re.search(r'SptS*(.+?)S', cleaned_content).group(1) if re.search(r'SptS*(.+?)S',
                                                                                cleaned_content) else None
    elif parameter == 'retargeting_id':
        return re.search(r'SreS*(.+?)S', cleaned_content).group(1) if re.search(r'SreS*(.+?)S',
                                                                                cleaned_content) else None
    elif parameter == 'source_type':
        return re.search(r'SsrcS*(.+?)S', cleaned_content).group(1) if re.search(r'SsrcS*(.+?)S',
                                                                                 cleaned_content) else None
    else:
        return None


utm_content = "some_utm_content_example_string"
result = utm_decode('campaign_id', utm_content)
print(result)
