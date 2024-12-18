import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def cont_geo(campaign):
    campaign = is_none(campaign)
    if re.search(r'mg_', campaign):
        return 'Докаты'
    elif re.search(r'_msk', campaign):
        return 'МСК + МО'
    elif re.search(r'_spb', campaign):
        return 'СПБ + ЛО'
    elif re.search(r'_cfo', campaign):
        return 'Центральный ФО (без МСК и МО)'
    elif re.search(r'_szfo', campaign):
        return 'Северо-Западный ФО (без СПБ и ЛО)'
    elif re.search(r'_yufo', campaign):
        return 'Южный ФО'
    elif re.search(r'_dvfo', campaign):
        return 'Дальневосточный ФО'
    elif re.search(r'_sfo', campaign):
        return 'Сибирский ФО'
    elif re.search(r'_urfo', campaign):
        return 'Уральский ФО'
    elif re.search(r'_pfo', campaign):
        return 'Приволжский ФО'
    elif re.search(r'_skfo', campaign):
        return 'Северо-Кавказский ФО'
    elif re.search(r'_all-rf|_rf|joint.*_all', campaign):
        return 'Россия(Кроме крыма)'
    elif re.search(r'_top-regions', campaign):
        return 'Регионы сильные'
    elif re.search(r'_low-regions', campaign):
        return 'Регионы слабые'
    elif re.search(r'_region', campaign):
        return 'Регионы'
    elif re.search(r'ekat|_nn|novos|samara|_ufa|nizhnij novgorod|kazan|chelyab|belgorod|izhevsk|krasnodar|kursk|perm|tula|volgograd|yaroslavl|barnaul|irkutsk|khabarovsk|krasnoyarsk|murmansk|omsk|ryazan|saratov|sochi|stavropol|tyumen|vladivostok|voronezh', campaign):
        return 'Регионы сильные'
    elif re.search(r'rnd|chelny|ivanovo|kaluga|lipetsk|rostov|smolensk|vladimir', campaign):
        return 'Регионы слабые'
    else:
        return 'NaN - ' + campaign