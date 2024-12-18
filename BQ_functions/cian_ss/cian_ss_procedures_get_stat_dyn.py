import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_stat_dyn(campaign_name, ad_name):
    campaign_name_lower = is_none(campaign_name)
    ad_name_lower = is_none(ad_name)

    if (re.search(r'_leadform|_multi|static', campaign_name_lower) or re.search(r'static',
                                                                                ad_name_lower)) and not re.search(
            r'_din', campaign_name_lower):
        return 'Статика'
    elif re.search(r'olv', campaign_name_lower):
        return 'Видео'
    else:
        return 'Динамика'
