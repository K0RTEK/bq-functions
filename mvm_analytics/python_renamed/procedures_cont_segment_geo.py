import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def cont_segment_geo(campaign):
    campaign = is_none(campaign)
    if re.search(r'_mo$|_mo_', campaign):
        return 'МО'
    elif re.search(r'_msk', campaign):
        return 'Москва'
    elif re.search(r'_spb', campaign):
        return 'СПБ'
    elif re.search(r'_novosibirsk', campaign):
        return 'Новосибирск'
    elif re.search(r'_ekaterinburg', campaign):
        return 'Екатеринбург'
    elif re.search(r'_nn', campaign):
        return 'Нижний Новгород'
    elif re.search(r'_rostov', campaign):
        return 'Ростов'
    elif re.search(r'_kazan', campaign):
        return 'Казань'
    elif re.search(r'_krasnodar', campaign):
        return 'Краснодар'
    elif re.search(r'_chelyabinsk', campaign):
        return 'Челябинск'
    elif re.search(r'_spbo', campaign):
        return 'СПБо'
    elif re.search(r'_samara', campaign):
        return 'Самара'
    elif re.search(r'_krasnoyarsk', campaign):
        return 'Красноярск'
    elif re.search(r'_irkutsk', campaign):
        return 'Иркутск'
    elif re.search(r'_all-rf', campaign):
        return 'РФ'
    elif re.search(r'armavir', campaign):
        return 'Армавир'
    elif re.search(r'kamyshin', campaign):
        return 'Камышин'
    elif re.search(r'maykop', campaign):
        return 'Майкоп'
    else:
        return 'NaN'