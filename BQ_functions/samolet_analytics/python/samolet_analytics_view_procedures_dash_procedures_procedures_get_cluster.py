import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_cluster(date, parameter, res_type):
    parameter = is_none(parameter)
    if re.search(r'cl-nmsk_| | ', parameter):
        return 'Кластер - НМ' if res_type == 'short_name' else 'Кластер - Новая Москва'
    elif re.search(r'cl-yug_| | ', parameter):
        return 'Кластер - Юг'
    elif re.search(r'cl-sever_| | ', parameter):
        return 'Кластер - Север'
    elif re.search(r'cl-zapad_| | ', parameter):
        return 'Кластер - Запад'
    elif re.search(r'cl-vostok_| | ', parameter):
        return 'Кластер - Восток'
    elif re.search(r'cl-bus_| | ', parameter):
        return 'Кластер - БК' if res_type == 'short_name' else 'Кластер - Бизнес-класс'
    else:
        return '-'