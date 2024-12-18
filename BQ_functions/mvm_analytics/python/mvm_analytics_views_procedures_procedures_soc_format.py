import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def soc_format(campaign):
    campaign = is_none(campaign)
    if not re.search(r'mg_', campaign):
        return 'Докаты'
    elif re.search(r'_flight', campaign):
        return 'Flight'
    elif re.search(r'_mlt|_multi', campaign):
        return 'Мульти'
    elif re.search(r'_crsl', campaign):
        return 'Карусель'
    elif re.search(r'_bnr', campaign):
        return 'Баннер'
    elif re.search(r'_rs|mg_pf_vk_alw_dir_kw_playstation_rf_approved', campaign):
        return 'Реклама сайта'
    elif re.search(r'_dro', campaign):
        return 'Динамическая подборка товаров из фида (не ретаргетинг)'
    else:
        return 'NaN - ' + campaign