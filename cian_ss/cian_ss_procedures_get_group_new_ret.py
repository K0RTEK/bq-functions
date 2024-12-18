import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_group_new_ret(campaign_name):
    campaign_name_lower = is_none(campaign_name)

    if re.search(r'_drtg_|_rtg_', campaign_name_lower):
        return 'Ретаргетинг'
    elif re.search(r'_new_', campaign_name_lower):
        return 'Новая'
    else:
        return f"NaN - {campaign_name}"