import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_group_vertical(campaign_name):
    campaign_name_lower = is_none(campaign_name)

    if re.search(r'_nov_') and re.search(r'skidki', campaign_name_lower):
        return 'НВС Скидки'
    elif re.search(r'_nov_') and re.search(r'bf', campaign_name_lower):
        return 'НВС ЧП Тизер'
    elif re.search(r'_nov_') and re.search(r'blf', campaign_name_lower):
        return 'НВС ЧП'
    elif re.search(r'_nov_|_nov-', campaign_name_lower) and not re.search(r'skidki|_new-lp|_leadform|_quiz',
                                                                          campaign_name_lower):
        return 'Новостройки'
    elif re.search(r'_nov_|_nov-', campaign_name_lower) and re.search(r'_new-lp', campaign_name_lower):
        return 'Новостройки NEW LP'
    elif re.search(r'_nov.*_leadform', campaign_name_lower):
        return 'Новостройки лиды'
    elif re.search(r'_nov.*_quiz', campaign_name_lower):
        return 'Новостройки квизы'
    elif re.search(r'_iapcom_', campaign_name_lower):
        return 'ИАП'
    elif re.search(r'_secsale_|_salesec_', campaign_name_lower):
        return 'Вторичка-Продажа'
    elif re.search(r'_rentsec', campaign_name_lower):
        return 'Вторичка-Аренда'
    elif re.search(r'_salesub_', campaign_name_lower):
        return 'Загородка-Продажа'
    elif re.search(r'_rentsub_', campaign_name_lower):
        return 'Загородка-Аренда'
    elif re.search(r'_own_', campaign_name_lower):
        return 'Собственники'
    elif re.search(r'_com_|_officecom_|_skladcom_|_psncom_|_cwrkcom_|_psnskladcom_|_officecwrkcom_|_gbcom_',
                   campaign_name_lower) and not re.search(r'_iapcom_', campaign_name_lower):
        return 'Коммерческая'
    elif re.search(r'_rieltor_', campaign_name_lower):
        return 'Риелторы'
    elif re.search(r'pf_ipoteka_', campaign_name_lower):
        return 'Ипотека'
    elif re.search(r'_sdelka_', campaign_name_lower):
        return 'Сделка'
    else:
        return f"NaN - {campaign_name}"