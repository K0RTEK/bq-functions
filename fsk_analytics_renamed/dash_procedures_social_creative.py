import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def social_creative(parameter_name, ad_name):
    ad_name = is_none(ad_name)
    parameter_name = is_none(parameter_name)

    if parameter_name == 'creative':
        return re.sub(r'_([0-9-]{5,})', '', ad_name)
    elif parameter_name == 'ad_object':
        if len(re.sub(r'[^_]', '', ad_name)) == 5:
            return re.search(r'([^_]+)_.*_.*_.*_.*_.*', ad_name).group(1)
        return re.search(r'([^_]+)_.*_.*_.*_.*', ad_name).group(1)
    elif parameter_name == 'ad_logic':
        if len(re.sub(r'[^_]', '', ad_name)) == 5:
            return re.search(r'.*_([^_]+)_.*_.*_.*_.*', ad_name).group(1)
        return re.search(r'.*_([^_]+)_.*_.*_.*', ad_name).group(1)
    elif parameter_name == 'ad_format':
        if len(re.sub(r'[^_]', '', ad_name)) == 5:
            return re.search(r'.*_.*_([^_]+)_.*_.*_.*', ad_name).group(1)
        return re.search(r'.*_.*_([^_]+)_.*_.*', ad_name).group(1)
    elif parameter_name == 'ad_render':
        if len(re.sub(r'[^_]', '', ad_name)) == 5:
            return re.search(r'.*_.*_.*_([^_]+)_.*_.*', ad_name).group(1)
        return re.search(r'.*_.*_([^_]+)_.*_.*', ad_name).group(1)
    elif parameter_name == 'ad_utp':
        if len(re.sub(r'[^_]', '', ad_name)) == 5:
            return re.search(r'.*_.*_.*_.*_([^_]+)_.*', ad_name).group(1)
        return re.search(r'.*_.*_.*_.*_([^_]+)', ad_name).group(1)
    elif parameter_name == 'ad_month_year':
        return re.search(r'.*_.*_.*_.*_.*_([0-9-]+)', ad_name).group(1)
    elif parameter_name == 'ad_month':
        return re.search(r'.*_.*_.*_.*_.*_([0-9]+)', ad_name).group(1)[:2]
    elif parameter_name == 'ad_year' and len(re.search(r'.*_.*_.*_.*_.*_.*-([0-9]+)', ad_name).group(1)) == 2:
        return '20' + re.search(r'.*_.*_.*_.*_.*_.*-([0-9]+)', ad_name).group(1)
    return None