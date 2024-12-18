import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()


import re


def get_channel(date, ct_source, ct_medium, crm_advertising_source, utm_source, utm_medium, utm_campaign, utm_content,
                utm_term):

    ct_source = is_none(ct_source)
    ct_medium = is_none(ct_medium)
    crm_advertising_source = is_none(crm_advertising_source)
    utm_source = is_none(utm_source)
    utm_medium = is_none(utm_medium)
    utm_campaign = is_none(utm_campaign)
    utm_content = is_none(utm_content)
    utm_term = is_none(utm_term)

    patterns = {
        'context_yandex_google': re.compile(r'yandex|google'),
        'context_yandex_google_calls': re.compile(r'context_yandex_google'),
        '_lead': re.compile(r'_lead'),
        'mediapronet_aquarius': re.compile(r'mediapronet|аквариус'),
        'hybrid_premium_id_investors_smart_data_premium': re.compile(r'hybrid|premium_id_investors|smart_data_premium'),
        '2gis': re.compile(r'2gis'),
        'yandex_maps': re.compile(r'yandex.maps|navigator|yandex.ru_karty_navigator|yandex_geoservice'),
        'yandex_ru_karty_i_navigator': re.compile(r'yandex.ru карты и навигатор'),
        'realty_yandex': re.compile(r'realty.yandex|yandex.ru_spravochnik'),
        'google_maps': re.compile(r'google.maps|google.com_karty'),
        'afisha': re.compile(r'afisha'),
        'bfm': re.compile(r'bfm'),
        'cian': re.compile(r'cian'),
        'forbes': re.compile(r'forbes'),
        'megafon': re.compile(r'megafon'),
        'interpool': re.compile(r'interpool'),
        'kommersant': re.compile(r'kommersant'),
        'lenta': re.compile(r'lenta'),
        'mts': re.compile(r'mts'),
        'one_target': re.compile(r'one_target'),
        'rbc': re.compile(r'rbc'),
        'timeout': re.compile(r'timeout'),
        'vc_desktop_vc_mobile_vc_ru': re.compile(r'vc_desktop|vc_mobile|vc.ru'),
        'vedomosti': re.compile(r'vedomosti'),
        'incrussia': re.compile(r'incrussia'),
        '101novostroyka': re.compile(r'101novostroyka'),
        '1dom': re.compile(r'1dom'),
        'aurumrealty': re.compile(r'aurumrealty'),
        'avaho': re.compile(r'avaho'),
        'businessclass_moscow': re.compile(r'businessclass.moscow'),
        'dommsk': re.compile(r'dommsk'),
        'gogethome': re.compile(r'gogethome'),
        'kdo': re.compile(r'kdo'),
        'kvartyroom': re.compile(r'kvartyroom'),
        'lifedeluxe': re.compile(r'lifedeluxe'),
        'mosdom': re.compile(r'mosdom'),
        'move': re.compile(r'move'),
        'msk_novostroyki': re.compile(r'msk-novostroyki'),
        'myburg_su': re.compile(r'myburg.su'),
        'myburg': re.compile(r'myburg'),
        'novomoscow': re.compile(r'novomoscow'),
        'novostroev': re.compile(r'novostroev'),
        'novostroy_gid': re.compile(r'novostroy-gid'),
        'novostroy_m': re.compile(r'novostroy-m'),
        'novostroycity': re.compile(r'novostroycity'),
        'poisk_novostroyki': re.compile(r'poisk-novostroyki'),
        'novostroy': re.compile(r'novostroy'),
        'realestate': re.compile(r'realestate'),
        'realtymag': re.compile(r'realtymag'),
        'realtystreet': re.compile(r'realtystreet'),
        'russianrealty': re.compile(r'russianrealty'),
        '2realty': re.compile(r'2realty'),
        'realty': re.compile(r'realty'),
        'reforum': re.compile(r'reforum'),
        'rendv': re.compile(r'rendv'),
        'restate': re.compile(r'restate'),
        'stroynov': re.compile(r'stroynov'),
        'topnovostroek': re.compile(r'topnovostroek'),
        'vsenovostroyki': re.compile(r'vsenovostroyki'),
        'irn_metrinfo_realsearch': re.compile(r'irn_metrinfo_realsearch'),
        'kvartirny_control': re.compile(r'kvartirny-control'),
        'mskguru': re.compile(r'mskguru'),
        'naydikvartiru': re.compile(r'naydikvartiru'),
        'elitnoe': re.compile(r'elitnoe'),
        'mirkvartir': re.compile(r'mirkvartir'),
        'eip': re.compile(r'eip'),
        'gdeetotdom': re.compile(r'gdeetotdom'),
        'novostroy_rf': re.compile(r'novostroy-rf'),
        'novostroyki_pro': re.compile(r'novostroyki.pro')
    }

    if (ct_source == '(direct)' or ct_medium in ('organic', 'referral') or
            crm_advertising_source.startswith('сайт')):
        return 'Органик'
    elif utm_medium == 'cpc' and patterns['context_yandex_google'].search(utm_source):
        return 'Контекстная реклама'
    elif utm_medium == 'calls' and patterns['context_yandex_google_calls'].search(utm_source):
        return 'Контекстная реклама'
    elif (utm_medium == 'cpa' or patterns['_lead'].search(utm_source) or
            patterns['_lead'].search(crm_advertising_source)):
        return 'Лидогенераторы'
    elif (patterns['mediapronet_aquarius'].search(crm_advertising_source) or
            patterns['mediapronet_aquarius'].search(utm_source)):
        return 'Базы'
    elif utm_medium == 'cpm' and patterns['hybrid_premium_id_investors_smart_data_premium'].search(utm_source):
        return 'Программатик'

    # Охватные ресурсы
    if (patterns['2gis'].search(utm_source) and utm_medium in ('calls', 'statika')) or \
            crm_advertising_source == '2gis' or \
            patterns['yandex_maps'].search(utm_source) and utm_medium in ('calls', 'statika', 'kartochka', 'cpm') or \
            crm_advertising_source == 'yandex.ru карты и навигатор' or \
            patterns['realty_yandex'].search(utm_source) and utm_medium in ('calls', 'cpm') or \
            crm_advertising_source == 'yandex.ru справочник' or \
            patterns['google_maps'].search(utm_source) and utm_medium in ('calls', 'kartochka') or \
            crm_advertising_source == 'google.com карты' or \
            patterns['afisha'].search(utm_source) and utm_medium == 'cpm' or \
            patterns['bfm'].search(utm_source) and utm_medium == 'cpm' or \
            patterns['cian'].search(utm_source) and utm_medium == 'cpm' or \
            patterns['forbes'].search(utm_source) and utm_medium == 'cpm' or \
            patterns['megafon'].search(utm_source) and utm_medium == 'push' or \
            patterns['interpool'].search(utm_source) and utm_medium in ('push', 'cpm') or \
            patterns['kommersant'].search(utm_source) and utm_medium == 'cpm' or \
            patterns['lenta'].search(utm_source) and utm_medium == 'cpm' or \
            patterns['mts'].search(utm_source) and utm_medium == 'push' or \
            patterns['one_target'].search(utm_source) and utm_medium == 'cpm' or \
            patterns['rbc'].search(utm_source) and utm_medium == 'cpm' or \
            crm_advertising_source == 'rbc.ru баннер' or \
            patterns['timeout'].search(utm_source) and utm_medium == 'cpm' or \
            patterns['vc_desktop_vc_mobile_vc_ru'].search(utm_source) and utm_medium == 'cpm' or \
            patterns['vedomosti'].search(utm_source) and utm_medium == 'cpm' or \
            patterns['incrussia'].search(utm_source) and utm_medium == 'push':
        return 'Охватные ресурсы'


    elif (patterns['101novostroyka'].search(utm_source) and utm_medium in ('calls', 'statika')) or \
            crm_advertising_source == '101novostroyka' or \
            patterns['1dom'].search(utm_source) and utm_medium in ('calls', 'statika') or \
            crm_advertising_source == '1dom' or \
            patterns['aurumrealty'].search(utm_source) and utm_medium in ('calls', 'statika') or \
            crm_advertising_source == 'aurumrealty' or \
            patterns['avaho'].search(utm_source) and utm_medium in ('calls', 'statika') or \
            crm_advertising_source == 'avaho' or \
            patterns['businessclass_moscow'].search(utm_source) and utm_medium in ('calls', 'statika') or \
            crm_advertising_source == 'businessclass.moscow' or \
            patterns['dommsk'].search(utm_source) and utm_medium in ('calls', 'statika') or \
            crm_advertising_source == 'dommsk' or \
            patterns['gogethome'].search(utm_source) and utm_medium in ('calls', 'statika') or \
            crm_advertising_source == 'gogethome' or \
            patterns['kdo'].search(utm_source) and utm_medium in ('calls', 'statika') or \
            crm_advertising_source == 'kdo' or \
            patterns['kvartyroom'].search(utm_source) and utm_medium in ('calls', 'statika') or \
            crm_advertising_source == 'kvartyroom' or \
            patterns['lifedeluxe'].search(utm_source) and utm_medium in ('calls', 'statika') or \
            crm_advertising_source == 'lifedeluxe' or \
            patterns['mosdom'].search(utm_source) and utm_medium in ('calls', 'statika') or \
            crm_advertising_source == 'mosdom' or \
            patterns['move'].search(utm_source) and utm_medium in ('calls', 'statika') or \
            crm_advertising_source == 'move' or \
            patterns['msk_novostroyki'].search(utm_source) and utm_medium in ('calls', 'statika') or \
            crm_advertising_source == 'msk-novostroyki' or \
            patterns['myburg_su'].search(utm_source) and utm_medium in ('calls', 'statika') or \
            crm_advertising_source == 'myburg.su' or \
            patterns['myburg'].search(utm_source) and utm_medium in ('calls', 'statika') or \
            crm_advertising_source == 'myburg' or \
            patterns['novomoscow'].search(utm_source) and utm_medium in ('calls', 'statika') or \
            crm_advertising_source == 'novomoscow' or \
            patterns['novostroev'].search(utm_source) and utm_medium in ('calls', 'statika') or \
            crm_advertising_source == 'novostroev' or \
            patterns['novostroy_gid'].search(utm_source) and utm_medium in ('calls', 'statika') or \
            crm_advertising_source == 'novostroy-gid' or \
            patterns['novostroy_m'].search(utm_source) and utm_medium in ('calls', 'statika') or \
            crm_advertising_source == 'novostroy-m' or \
            patterns['novostroycity'].search(utm_source) and utm_medium in ('calls', 'statika') or \
            crm_advertising_source == 'novostroycity' or \
            patterns['poisk_novostroyki'].search(utm_source) and utm_medium in ('calls', 'statika') or \
            crm_advertising_source == 'poisk-novostroyki' or \
            patterns['novostroy'].search(utm_source) and utm_medium in ('calls', 'statika') or \
            crm_advertising_source == 'novostroy' or \
            patterns['realestate'].search(utm_source) and utm_medium in ('calls', 'statika') or \
            crm_advertising_source == 'realestate' or \
            patterns['realtymag'].search(utm_source) and utm_medium in ('calls', 'statika') or \
            crm_advertising_source == 'realtymag' or \
            patterns['realtystreet'].search(utm_source) and utm_medium in ('calls', 'statika') or \
            crm_advertising_source == 'realtystreet' or \
            patterns['russianrealty'].search(utm_source) and utm_medium in ('calls', 'statika') or \
            crm_advertising_source == 'russianrealty' or \
            patterns['2realty'].search(utm_source) and utm_medium in ('calls', 'statika') or \
            crm_advertising_source == '2realty' or \
            patterns['realty'].search(utm_source) and utm_medium in ('calls', 'statika') or \
            crm_advertising_source == 'realty' or \
            patterns['reforum'].search(utm_source) and utm_medium in ('calls', 'statika') or \
            crm_advertising_source == 'reforum' or \
            patterns['rendv'].search(utm_source) and utm_medium in ('calls', 'statika') or \
            crm_advertising_source == 'rendv' or \
            patterns['restate'].search(utm_source) and utm_medium in ('calls', 'statika') or \
            crm_advertising_source == 'restate' or \
            patterns['stroynov'].search(utm_source) and utm_medium in ('calls', 'statika') or \
            crm_advertising_source == 'stroynov' or \
            patterns['topnovostroek'].search(utm_source) and utm_medium in ('calls', 'statika') or \
            crm_advertising_source == 'topnovostroek' or \
            patterns['vsenovostroyki'].search(utm_source) and utm_medium in ('calls', 'statika') or \
            crm_advertising_source == 'vsenovostroyki' or \
            patterns['irn_metrinfo_realsearch'].search(utm_source) and utm_medium in ('calls', 'statika') or \
            crm_advertising_source == 'irn_metrinfo_realsearch' or \
            patterns['kvartirny_control'].search(utm_source) and utm_medium in ('calls', 'statika') or \
            crm_advertising_source == 'kvartirny-control' or \
            patterns['mskguru'].search(utm_source) and utm_medium in ('calls', 'statika') or \
            crm_advertising_source == 'mskguru' or \
            patterns['naydikvartiru'].search(utm_source) and utm_medium in ('calls', 'statika') or \
            crm_advertising_source == 'naydikvartiru' or \
            patterns['elitnoe'].search(utm_source) and utm_medium in ('calls', 'statika') or \
            crm_advertising_source == 'elitnoe' or \
            patterns['mirkvartir'].search(utm_source) and utm_medium in ('calls', 'statika') or \
            crm_advertising_source == 'mirkvartir' or \
            patterns['eip'].search(utm_source) and utm_medium in ('calls', 'statika') or \
            crm_advertising_source == 'eip' or \
            patterns['gdeetotdom'].search(utm_source) and utm_medium in ('calls', 'statika') or \
            crm_advertising_source == 'gdeetotdom' or \
            patterns['novostroy_rf'].search(utm_source) and utm_medium in ('calls', 'statika') or \
            crm_advertising_source == 'novostroy-rf' or \
            patterns['novostroyki_pro'].search(utm_source) and utm_medium in ('calls', 'statika'):
        return 'Тематические площадки'


    return 'Unknown'
