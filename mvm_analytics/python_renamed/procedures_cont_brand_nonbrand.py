import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def cont_brand_nonbrand(campaign):
    campaign = is_none(campaign)
    if re.search(r'_image_name.*(_p_|search)', campaign):
        return 'Бренд'
    else:
        return 'Не Бренд'