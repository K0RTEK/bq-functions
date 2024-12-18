import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()


def get_flight_segments(segment, campaign):
    segment = is_none(segment)
    campaign = is_none(campaign).lower()



    if segment == 'budget':
        if re.search(r'_kd_', campaign):
            return 'Вендорский'
        elif re.search(r'_fed_', campaign):
            return 'МВМ'


    elif segment == 'ecounit':
        if re.search(r'_e-p_', campaign):
            return 'Развлечения и Фото-Видео'
        elif re.search(r'_kt_', campaign):
            return 'Кухня'
        elif re.search(r'_mb_', campaign):
            return 'Мобильная техника'
        elif re.search(r'_h-o_', campaign):
            return 'Домашний офис'
        elif re.search(r'_c-s_|_c_s_', campaign):
            return 'Кино и Звук'
        elif re.search(r'_h-c_', campaign):
            return 'Дом и забота о себе'


    elif segment == 'flight_id':
        match = re.search(r'..\...-..\...\..._([0-9]+)', campaign) or \
                re.search(r'..\...-..\...\....._([0-9]+)', campaign) or \
                re.search(r'..\...\.....-..\...\....._([0-9]+)', campaign) or \
                re.search(r'..\...-..\..._([0-9]+)', campaign) or \
                re.search(r'..\..._..\..._([0-9]+)', campaign) or \
                re.search(r'..\...-.\...\..._([0-9]+)', campaign) or \
                re.search(r'..\...-..\...\....*_([0-9]+)', campaign) or \
                re.search(r'..\...-..\....*_([0-9]+)', campaign) or \
                re.search(r'..\...\.....-..\...\....*_([0-9]+)', campaign) or \
                re.search(r'..\...-.\...\....*_([0-9]+)', campaign) or \
                re.search(r'..\...\... - ..\...\..._([0-9]+)', campaign) or \
                re.search(r'..\... - ..\..._([0-9]+)', campaign) or \
                re.search(r'..\...\...-..\...\..._([0-9]+)', campaign) or \
                re.search(r'..\...-.\..._([0-9]+)', campaign) or \
                re.search(r'..\....-.\..._([0-9]+)', campaign) or \
                re.search(r'..\...\...-..\...\..._([0-9]+)', re.sub('%2520', '', campaign)) or \
                re.search(r'[0-9]{6}_[0-9]{6}_([0-9]+)', campaign) or \
                re.search(r'[0-9]{4}_[0-9]{4}_([0-9]+)', campaign)

        if match:
            return match.group(1)


    elif segment == 'jira_id':
        match = re.search(r'_([0-9]+)_.*\...-..\...\...', campaign) or \
                re.search(r'_([0-9]+)_.*\...-.\...\...', campaign) or \
                re.search(r'_([0-9]+)_.*-.*', campaign)

        if match:
            return match.group(1)


    elif segment == 'period':
        match = re.search(r'(..\...-..\...\...)', campaign) or \
                re.search(r'(..\...\.....-..\...\.....)', campaign) or \
                re.search(r'(..\...-..\...)', campaign) or \
                re.search(r'(..\...-.\...\...)', campaign)

        if match:
            return match.group(1)


    elif segment == 'category':
        if re.search(r'(mv|eldo).*(_se_)', campaign):
            return 'Сервисы'
        elif re.search(r'(mv|eldo).*(_ер_|_е-р_|_ep_|_e-p_)', campaign):
            return 'Фото и видео'
        elif re.search(r'(mv|eldo).*(_ас_|_а-с_|_ac_|_a-c_)', campaign):
            return 'Аксессуары МВ'
        elif re.search(r'(mv|eldo).*(_но_|_н-о_|_ho_|_h-o_)', campaign):
            return 'Домашний офис'
        elif re.search(r'(mv|eldo).*(_с-е_|_се_|_c-e_|_ce_)', campaign):
            return 'Аксессуары'
        elif re.search(r'(mv|eldo).*(_c-s_|_cs_|_c_s_)', campaign):
            return 'Кино и звук'
        elif re.search(r'(mv|eldo).*(_н-с_|_h-c_|_h_c_|_н_с_)', campaign):
            return 'Дом и забота о себе'
        elif re.search(r'(mv|eldo).*(_kt_|_кт_)', campaign):
            return 'Кухня'
        elif re.search(r'(mv|eldo).*(_мв_|_mb_|_мb_|_mв_|_mv_)', campaign):
            return 'Телеком'


    return f'NaN - {campaign}'
