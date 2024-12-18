import re
import datetime as dt

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()


def get_segment_mp(campaign_name, date):
    campaign_name = is_none(campaign_name)
    if re.search(r'quiz', campaign_name, re.IGNORECASE):
        return 'Квиз'
    elif re.search(r'_n_|_mk_|_epk_', campaign_name, re.IGNORECASE):
        return 'РСЯ и Мастер кампаний'
    elif re.search(r'_s_', campaign_name, re.IGNORECASE):
        return 'Поиск'
    elif re.search(r'_perfomance', campaign_name, re.IGNORECASE):
        return 'Тест ЕПК'
    elif re.search(r'_tg_', campaign_name, re.IGNORECASE):
        return 'Тест ТГ'
    elif re.search(r'_catalog', campaign_name, re.IGNORECASE):
        return 'Тест Каталоговые объявления'

    return None