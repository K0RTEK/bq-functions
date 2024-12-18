import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_group_geo(campaign_name):
    campaign_name_lower = is_none(campaign_name)

    if re.search(r'_msc_|_mobl_|_msk_|_mo_|_bmo_|_dmo_|_mskmo_|_mskbmo_', campaign_name_lower):
        return 'Москва'
    elif re.search(r'_spb_|_lo_|_spblo_', campaign_name_lower):
        return 'Питер'
    elif re.search(r'_novosibirsk_', campaign_name_lower):
        return 'Новосибирск'
    elif re.search(r'_ekb_', campaign_name_lower):
        return 'Екатеринбург'
    elif re.search(r'_omsk_', campaign_name_lower):
        return 'Омск'
    elif re.search(r'_krasnodar_', campaign_name_lower):
        return 'Краснодар'
    elif re.search(r'_[0-9]{1,2}reg|_extrareg|_reg|_omsk', campaign_name_lower):
        return 'Регионы'
    elif re.search(r'_rf_', campaign_name_lower):
        return 'РФ'
    else:
        return f"NaN - {campaign_name}"