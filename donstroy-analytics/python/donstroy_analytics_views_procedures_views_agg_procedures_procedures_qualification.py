import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def qualification(crm_stage, date):
    crm_stage = is_none(crm_stage)
    date = is_none(date)
    if re.search(r'перевод в продажу|новый|продажа завершена неуспешно', crm_stage):
        return 'Квалифицированный'
    else:
        return 'Неквалифицированный'