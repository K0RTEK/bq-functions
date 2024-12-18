import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()


import re


def get_placement(date, ct_source, ct_medium, crm_advertising_source, utm_source, utm_medium, utm_campaign, utm_content,
                  utm_term):
    utm_source = is_none(utm_source)
    utm_medium = is_none(utm_medium)
    crm_advertising_source = is_none(crm_advertising_source)
    utm_campaign = is_none(utm_campaign)
    utm_content = is_none(utm_content)
    utm_term = is_none(utm_term)
    ct_medium = is_none(ct_medium)
    ct_source = is_none(ct_source)

    def regex_contains(text, pattern):
        return re.search(pattern, text) is not None

    if regex_contains(utm_source, r'context_yandex_google') and utm_medium == 'calls':
        return 'Визитка'
    elif regex_contains(utm_source, r'yandex') and utm_medium == 'cpc':
        return 'Yandex'
    elif regex_contains(utm_source, r'google') and utm_medium == 'cpc':
        return 'Google Ads'

    elif regex_contains(utm_source, r'mediapronet-avito') and utm_medium == 'calls':
        return 'Авито/mediapronet'
    elif crm_advertising_source == 'mediapronet avito':
        return 'Авито/mediapronet'
    elif regex_contains(utm_source, r'aquarius-na100pro$') and utm_medium == 'calls':
        return 'Аквариум/NA100PRO'
    elif crm_advertising_source == 'аквариус na100pro':
        return 'Аквариум/NA100PRO'
    elif regex_contains(utm_source, r'mediapronet-cian') and utm_medium == 'calls':
        return 'Cian/mediapronet'
    elif crm_advertising_source == 'mediapronet cian':
        return 'Cian/mediapronet'
    elif regex_contains(utm_source, r'mediapronet-m2') and utm_medium == 'calls':
        return 'M2.RU/mediapronet'
    elif crm_advertising_source == 'mediapronet m2':
        return 'M2.RU/mediapronet'
    elif regex_contains(utm_source, r'mediapronet-yandex_realty.ru') and utm_medium == 'calls':
        return 'Yandex.Realty.Ru/mediapronet'
    elif crm_advertising_source == 'mediapronet яндекс недвиж':
        return 'Yandex.Realty.Ru/mediapronet'
    elif regex_contains(utm_source, r'basic_xml') and utm_medium in ('calls', 'cpl'):
        return 'Basic XML'
    elif crm_advertising_source == 'basic xml':
        return 'Basic XML'
    elif regex_contains(utm_source, r'aquarius') and utm_medium == 'calls':
        return 'Другое'
    elif regex_contains(crm_advertising_source, r'аквариус'):
        return 'Другое'

    elif regex_contains(utm_source, r'atommedia') and utm_medium in ('calls', 'cpa'):
        return 'Atommedia'
    elif crm_advertising_source == 'atommedia лид':
        return 'Atommedia'
    elif regex_contains(utm_source, r'call.of.leads|callofleads') and utm_medium in ('calls', 'cpa'):
        return 'Call of Leads'
    elif crm_advertising_source == 'call of leads лид':
        return 'Call of Leads'
    elif regex_contains(utm_source, r'callexchange') and utm_medium in ('calls', 'cpa'):
        return 'Callexchange'
    elif crm_advertising_source == 'callexchange':
        return 'Callexchange'
    elif regex_contains(utm_source, r'callrealty') and utm_medium in ('calls', 'cpa'):
        return 'CallRealty'
    elif crm_advertising_source == 'callrealty лид':
        return 'CallRealty'
    elif regex_contains(utm_source, r'calltact') and utm_medium in ('calls', 'cpa'):
        return 'CallTact'
    elif crm_advertising_source == 'calltact лид':
        return 'CallTact'
    elif regex_contains(utm_source, r'cpaexchange') and utm_medium in ('calls', 'cpa'):
        return 'CPAExchange'
    elif regex_contains(utm_source, r'datavision') and utm_medium in ('calls', 'cpa'):
        return 'DataVision'
    elif crm_advertising_source == 'datavision лид':
        return 'DataVision'
    elif regex_contains(utm_source, r'getflat') and utm_medium in ('calls', 'cpa'):
        return 'GetFlat'
    elif crm_advertising_source == 'getflat лид':
        return 'GetFlat'
    elif regex_contains(utm_source, r'like_estate|likeestate') and utm_medium in ('calls', 'cpa'):
        return 'LikeEstate'
    elif crm_advertising_source == 'like estate лид':
        return 'LikeEstate'
    elif regex_contains(utm_source, r'maketrue') and utm_medium in ('calls', 'cpa'):
        return 'MakeTrue'
    elif crm_advertising_source == 'maketrue лид':
        return 'MakeTrue'
    elif regex_contains(utm_source, r'marketcall') and utm_medium in ('calls', 'cpa'):
        return 'MarketCall'
    elif crm_advertising_source == 'maketrue лид':
        return 'MarketCall'
    elif regex_contains(utm_source, r'monkey') and utm_medium in ('calls', 'cpa'):
        return 'Monkey'
    elif regex_contains(utm_source, r'rocketad') and utm_medium in ('calls', 'cpa'):
        return 'Rocketad'
    elif crm_advertising_source == 'roketad лид':
        return 'Rocketad'
    elif regex_contains(utm_source, r'roombery|roomberry') and utm_medium in ('calls', 'cpa'):
        return 'Roomberry'
    elif crm_advertising_source == 'roombery лид':
        return 'Roomberry'

    elif regex_contains(utm_source, r'getflat') and utm_medium == 'cpm':
        return 'Getflat'
    elif regex_contains(utm_source, r'hybrid') and utm_medium == 'cpm':
        return 'Hybrid'
    elif regex_contains(utm_source, r'premium_id') and utm_medium == 'cpm':
        return 'Premium ID'
    elif regex_contains(utm_source, r'smart_data_premium') and utm_medium == 'cpm':
        return 'Smart Data Premium'
    elif crm_advertising_source == 'smartdata программатик премиум':
        return 'Smart Data Premium'

    elif regex_contains(utm_source, r'2gis') and utm_medium in ('calls', 'statika'):
        return '2gis.ru'
    elif crm_advertising_source == '2gis':
        return '2gis.ru'
    elif regex_contains(utm_source,
                        r'yandex.maps|navigator|yandex.ru_karty_navigator|yandex_geoservice') and utm_medium in (
    'calls', 'statika', 'kartochka', 'cpm'):
        return 'Яндекс Геосервисы'
    elif crm_advertising_source == 'yandex.ru карты и навигатор':
        return 'Яндекс Геосервисы'
    elif regex_contains(utm_source, r'realty.yandex|yandex.ru_spravochnik') and utm_medium in ('calls', 'cpm'):
        return 'Яндекс Недвижимость'
    elif crm_advertising_source == 'yandex.ru справочник':
        return 'Яндекс Недвижимость'
    elif regex_contains(utm_source, r'google.maps|google.com_karty') and utm_medium in ('calls', 'kartochka'):
        return 'google.com карты'
    elif crm_advertising_source == 'google.com карты':
        return 'google.com карты'
    elif regex_contains(utm_source, r'afisha') and utm_medium == 'cpm':
        return 'Afisha Daily'
    elif regex_contains(utm_source, r'bfm') and utm_medium == 'cpm':
        return 'BFM.ru'
    elif regex_contains(utm_source, r'cian') and utm_medium == 'cpm':
        return 'Cian.ru'
    elif regex_contains(utm_source, r'forbes') and utm_medium == 'cpm':
        return 'Forbes'
    elif regex_contains(utm_source, r'megafon') and utm_medium == 'push':
        return 'Megafon'
    elif regex_contains(utm_source, r'interpool') and utm_medium in ('push', 'cpm'):
        return 'Interpool'
    elif regex_contains(utm_source, r'kommersant') and utm_medium == 'cpm':
        return 'Kommersant'
    elif regex_contains(utm_source, r'lenta') and utm_medium == 'cpm':
        return 'Lenta'
    elif regex_contains(utm_source, r'mts') and utm_medium == 'push':
        return 'MTS'
    elif regex_contains(utm_source, r'one_target') and utm_medium == 'cpm':
        return 'One Target'
    elif regex_contains(utm_source, r'rbc') and utm_medium == 'cpm':
        return 'RBC'
    elif regex_contains(utm_source, r'tinkoff') and utm_medium == 'cpm':
        return 'Tinkoff'
    elif regex_contains(utm_source, r'yandex') and utm_medium == 'push':
        return 'Яндекс'
    elif regex_contains(utm_source, r'google') and utm_medium == 'push':
        return 'Google'

    return 'Not Found'
