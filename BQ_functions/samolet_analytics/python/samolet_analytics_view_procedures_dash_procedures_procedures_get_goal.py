import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_cluster(type, date, goal):
    goal = is_none(goal)
    type = is_none(type)
    if re.search(r'309324554', goal):
        return {'col_name': 'izhivika_goal309324554', 'project': 'И живи-ка', 'description': 'Успешное бронирование'}
    elif re.search(r'308760363', goal):
        return {'col_name': 'izhivika_goal308760363', 'project': 'И живи-ка', 'description': 'Клик на Закажите консультацию'}
    elif re.search(r'326313875', goal):
        return {'col_name': 'izhivika_goal326313875', 'project': 'И живи-ка', 'description': 'Выбрать квартиру (шаг 1)'}
    elif re.search(r'326313876', goal):
        return {'col_name': 'izhivika_goa326313876', 'project': 'И живи-ка', 'description': 'Выбор квартиры. Бронирование: Шаг 2 - Клик на кнопку “Забронировать”'}
    elif re.search(r'326313877', goal):
        return {'col_name': 'izhivika_goal326313877', 'project': 'И живи-ка', 'description': 'Выбор квартиры. Бронирование: Шаг 3 - Клик на кнопку “Начать бронирование”'}
    elif re.search(r'326313878', goal):
        return {'col_name': 'izhivika_goal326313878', 'project': 'И живи-ка', 'description': 'Успешное бронирование (шаг 4)'}
    elif re.search(r'326190310', goal):
        return {'col_name': 'izhivika_goal326190310', 'project': 'И живи-ка', 'description': 'Вереск Лист ожидания клик'}
    elif re.search(r'326136175', goal):
        return {'col_name': 'izhivika_goal326136175', 'project': 'И живи-ка', 'description': 'Вереск Лист ожидания'}
    elif re.search(r'326982523', goal):
        return {'col_name': 'izhivika_goal326982523', 'project': 'И живи-ка', 'description': 'Мята Лист ожидания клик'}
    elif re.search(r'326982434', goal):
        return {'col_name': 'izhivika_goal326982434', 'project': 'И живи-ка', 'description': 'Мята Лист ожидания'}
    elif re.search(r'316924482', goal):
        return {'col_name': 'izhivika_goal316924482', 'project': 'Целепорт', 'description': 'Отправка формы и паспортных данных и ИНН (шаг 4)'}
    elif re.search(r'316924334', goal):
        return {'col_name': 'izhivika_goal316924334', 'project': 'Целепорт', 'description': 'Клик на Открыть Целепорт (шаг 1)'}
    elif re.search(r'317614125', goal):
        return {'col_name': 'izhivika_goal317614125', 'project': 'Целепорт', 'description': 'Отправка номера (шаг 2)'}
    elif re.search(r'317614126', goal):
        return {'col_name': 'izhivika_goal317614126', 'project': 'Целепорт', 'description': 'Клик на отправку формы (шаг 3)'}
    elif re.search(r'317612819', goal):
        return {'col_name': 'izhivika_goal317612819', 'project': 'Целепорт', 'description': 'Открыть Целепорт (шаг 1)'}
    elif re.search(r'317612820', goal):
        return {'col_name': 'izhivika_goal317612820', 'project': 'Целепорт', 'description': 'Отправка номера (шаг 2)'}
    elif re.search(r'317612821', goal):
        return {'col_name': 'izhivika_goal317612821', 'project': 'Целепорт', 'description': 'Отправка формы и паспортных данных и ИНН (шаг 3)'}
    elif re.search(r'322894105', goal):
        return {'col_name': 'izhivika_goal322894105', 'project': 'Формула счастья', 'description': 'Финишная страница, опрос завершен'}