import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()


def get_network_source(date,utm_source,utm_medium,utm_campaign,utm_content,utm_term):
    date,utm_source,utm_medium,utm_campaign,utm_content,utm_term = map(is_none,[date,utm_source,utm_medium,utm_campaign,utm_content,utm_term])
    if utm_source == 'yandex' and utm_medium == 'cpc':
        match = re.search(r'\|s:([^|]+)', utm_content)
        if match:
            return match.group(1)
    return 'NaN'