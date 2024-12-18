import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_flight_segment(date, campaign):
    campaign = is_none(campaign)
    date = is_none(date)
    if re.search(r'_s[eе]_', campaign):
        return 'Сервисы'
    elif re.search(r'_[eе][pр]_|_[eе]-[pр]_', campaign):
        return 'Фото и видео'
    elif re.search(r'_[aа][cс]_|_[aа]-[cс]_', campaign):
        return 'Аксессуары МВ'
    elif re.search(r'_[hн][oо]_|_[hн]-[oо]_', campaign):
        return 'Домашний офис'
    elif re.search(r'_[cс]-[eе]_|_[cс][eе]_', campaign):
        return 'Аксессуары МВ'
    elif re.search(r'_[cс]-s_|_[cс]s_|_[cс]_s_', campaign):
        return 'Кино и звук'
    elif re.search(r'_[hн]-[cс]_|_[hн]_[cс]_ ', campaign):
        return 'Дом и забота о себе'
    elif re.search(r'_[kк][tт]_', campaign):
        return 'Кухня'
    elif re.search(r'_[mм][bв]_|_[mм]v_.*_[mм]v_|_eldo_.*_[mм]v_', campaign):
        return 'Телеком'
    else:
        return 'NaN'