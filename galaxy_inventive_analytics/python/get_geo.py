import re
import datetime as dt

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_geo(channel, campaign, date):
    channel = is_none(channel)
    campaign = is_none(campaign)

    if channel == 'контекст':
        if re.search(r'msk', campaign):
            return 'Москва и МО'
        elif re.search(r'spb', campaign):
            return 'Санкт-Петербург и ЛО'
        elif re.search(r'highcr', campaign):
            return 'Highcr'
        elif re.search(r'lowcr', campaign):
            return 'Lowcr'
        elif re.search(r'vpn', campaign):
            return 'ВПН'
        elif re.search(r'rf', campaign):
            return 'РФ'
        elif re.search(r'regions|ekb|smr|ufa', campaign):
            return 'Регионы'
        else:
            return 'NaN'
    elif channel == 'соцсети':
        if date <= dt.date(2022, 12, 31):
            if re.search(r'_msk', campaign):
                return 'Москва и МО'
            elif re.search(r'rf||pf_m_ret_dnmc_action', campaign):
                return 'РФ'
            elif re.search(r'_reg', campaign):
                return 'Регионы'
            else:
                return 'NaN'
        elif date > dt.date(2022, 12, 31):
            if re.search(r'_msk-spb', campaign):
                return 'Москва и СПб'
            elif re.search(r'_msk', campaign):
                return 'Москва и МО'
            elif re.search(r'_spb', campaign):
                return 'Санкт-Петербург и ЛО'
            elif re.search(r'_allrf|_rf|pf_m_ret_dnmc_action', campaign):
                return 'Вся РФ'
            elif re.search(r'_reg', campaign):
                return 'Регионы'
            else:
                return 'NaN'
    else:
        return 'NaN'