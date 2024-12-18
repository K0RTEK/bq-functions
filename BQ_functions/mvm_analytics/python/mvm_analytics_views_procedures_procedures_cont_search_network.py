import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def cont_search_network(campaign):
    campaign = is_none(campaign)
    if re.search(r'_tk_|_epk_|_united_', campaign):
        return '  '
    elif not re.search(r'mg_', campaign):
        return ' '
    elif re.search(r'_p_|search|_dsa|yandex_shopping|yandexmarket', campaign):
        return ' '
    elif re.search(r'_s_|rsya', campaign):
        return ' '
    else:
        return 'NaN - ' + campaign