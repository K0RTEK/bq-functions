import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_object(parameter):
    parameter = is_none(parameter)

    if re.search(r'moskov|москов|пм_', parameter):
        return 'Первый Московский'
    elif re.search(r'peredelk|переделк|пб_', parameter):
        return 'Переделкино Ближнее'
    # Add more conditions based on original SQL function
    return 'Неизвестный'
