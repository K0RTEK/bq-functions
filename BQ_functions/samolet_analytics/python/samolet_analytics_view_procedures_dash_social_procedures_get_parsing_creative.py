import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_parsing_creative(parameter_name,date,ad_name):
    ad_name = is_none(ad_name)
    parameter_name = is_none(parameter_name)

    if parameter_name == 'project':
        return re.search(r'([^_]+)_.*_.*_.*_.*_.*_.*', ad_name).group(1)
    elif parameter_name == 'direction':
        return re.search(r'.*_([^_]+)_.*_.*_.*_.*_.*', ad_name).group(1)
    elif parameter_name == 'type':
        return re.search(r'.*_.*_([^_]+)_.*_.*_.*_.*', ad_name).group(1)
    elif parameter_name == 'main_targeting':
        return re.search(r'.*_.*_.*_([^_]+)_.*_.*_.*', ad_name).group(1)
    elif parameter_name == 'format':
        return re.search(r'.*_.*_.*_.*_([^_]+)_.*_.*', ad_name).group(1)
    elif parameter_name == 'visual':
        return re.search(r'.*_.*_.*_.*_.*_([^_]+)_.*', ad_name).group(1)
    elif parameter_name == 'utp':
        return re.search(r'.*_.*_.*_.*_.*_.*_([^_]+)_.*', ad_name).group(1)
    elif parameter_name == 'month_start':
        return re.search(r'.*_.*_.*_.*_.*_.*_.*_([^_]+)', ad_name).group(1)