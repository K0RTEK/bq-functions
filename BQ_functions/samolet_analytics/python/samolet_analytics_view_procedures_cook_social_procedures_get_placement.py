import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_placement(parameter):
    parameter = is_none(parameter)
    if re.search(r'vk/cpc|vka/cpc|vka/cpm|vk/lead| вкр ', parameter):
        return 'VK Ads'
    elif re.search(r'mt/cpc| мт ', parameter):
        return 'MT'
    else:
        return ''