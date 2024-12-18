import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_group_vertical_media(campaign_name):
    campaign_name_lower = is_none(campaign_name)

    if re.search(r'_all_', campaign_name_lower):
        return 'Общее размещение'
    elif re.search(r'_sub_', campaign_name_lower):
        return 'Загородка'
    elif re.search(r'_vtor_', campaign_name_lower):
        return 'Вторичка'
    elif re.search(r'_nov_', campaign_name_lower):
        return 'Новостройки'
    elif re.search(r'_own_', campaign_name_lower):
        return 'Собственники'
    elif re.search(r'_com_', campaign_name_lower):
        return 'Коммерческая'
    elif re.search(r'_rieltor_', campaign_name_lower):
        return 'Риелторы'
    elif re.search(r'_rent_', campaign_name_lower):
        return 'Вторичка-Аренда'
    else:
        return f"NaN - {campaign_name}"