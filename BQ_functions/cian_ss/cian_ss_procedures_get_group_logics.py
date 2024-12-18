import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_group_logics(campaign_name):
    campaign_name_lower = is_none(campaign_name)

    if re.search(r'_socdem_', campaign_name_lower):
        return 'Соцдем'
    elif re.search(r'_key_', campaign_name_lower):
        return 'Ключи'
    elif re.search(r'_interest_', campaign_name_lower):
        return 'Интересы'
    elif re.search(r'_drtg_', campaign_name_lower):
        return 'Динрем'
    elif re.search(r'_srtg_', campaign_name_lower):
        return 'Статрем'
    elif re.search(r'_lal_', campaign_name_lower):
        return 'Look-a-like'
    elif re.search(r'_group_', campaign_name_lower):
        return 'Группы'
    else:
        return f"NaN - {campaign_name}"