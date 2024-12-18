import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_segment_2(parameter):
    parameter = is_none(parameter)
    return {
        re.compile(r'(_|^)brand(_|$)').search(parameter): 'Бренд',
        re.compile(r'(_|^)geo(_|$)').search(parameter): 'Гео',
        re.compile(r'(_|^)compet(_|$)').search(parameter): 'Конкуренты',
        re.compile(r'(_|^)generic(_|$)').search(parameter): 'Общие',
        re.compile(r'(_|^)lal(_|$)').search(parameter): 'LAL',
        re.compile(r'(_|^)polygon(_|$)|(_|^)audiences(_|$)').search(parameter): 'Аудитории',
        re.compile(r'(_|^)remarketing(_|$)').search(parameter): 'Ретаргетинг'
    }.get(None, 'Прочее')