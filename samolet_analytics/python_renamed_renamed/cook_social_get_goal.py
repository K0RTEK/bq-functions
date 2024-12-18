import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_additions(type,goal):
    goal = is_none(goal)
    type = is_none(type)
    if re.search(r'309324554', goal):
        return {
            'col_name': 'izhivika_goal309324554',
            'project': 'И живи-ка',
            'goal': 'Успешное бронирование'
        }[type]
    elif re.search(r'308760363', goal):
        return {
            'col_name': 'izhivika_goal308760363',
            'project': 'И живи-ка',
            'goal': 'Клик на Закажите консультацию'
        }[type]
    elif re.search(r'326313875', goal):
        return {
            'col_name': 'izhivika_goal326313875',
            'project': 'И живи-ка',
            'goal': 'Выбрать квартиру (шаг 1)'
        }[type]
    elif re.search(r'326313876', goal):
        return {
            'col_name': 'izhivika_goa326313876',
            'project': 'И живи-ка',
            'goal': 'Выбор квартиры. Бронирование: Шаг 2 - Клик на кнопку “Забронировать”'
        }[type]
    elif re.search(r'326313877', goal):
        return {
            'col_name': 'izhivika_goal326313877',
            'project': 'И живи-ка',
            'goal': 'Выбор квартиры. Бронирование: Шаг 3 - Клик на кнопку “Начать бронирование”'
        }[type]
    elif re.search(r'326313878', goal):
        return {
            'col_name': 'izhivika_goal326313878',
            'project': 'И живи-ка',
            'goal': 'Успешное бронирование (шаг 4)'
        }[type]
    elif re.search(r'326190310', goal):
        return {
            'col_name': 'izhivika_goal326190310',
            'project': 'И живи-ка',
            'goal': 'Вереск Лист ожидания клик'
        }[type]
    elif re.search(r'326136175', goal):
        return {
            'col_name': 'izhivika_goal326136175',
            'project': 'И живи-ка',
            'goal': 'Вереск Лист ожидания'
        }[type]
    elif re.search(r'326982523', goal):
        return {
            'col_name': 'izhivika_goal326982523',
            'project': 'И живи-ка',
            'goal': 'Мята Лист ожидания клик'
        }[type]
    elif re.search(r'326982434', goal):
        return {
            'col_name': 'izhivika_goal326982434',
            'project': 'И живи-ка',
            'goal': 'Мята Лист ожидания'
        }[type]
    elif re.search(r'316924482', goal):
        return {
            'col_name': 'izhivika_goal316924482',
            'project': 'Целепорт',
            'goal': 'Отправка формы и паспортных данных и ИНН (шаг 4)'
        }[type]
    elif re.search(r'316924334', goal):
        return {
            'col_name': 'izhivika_goal316924334',
            'project': 'Целепорт',
            'goal': 'Клик на Открыть Целепорт (шаг 1)'
        }[type]
    elif re.search(r'317614125', goal):
        return {
            'col_name': 'izhivika_goal317614125',
            'project': 'Целепорт',
            'goal': 'Отправка номера (шаг 2)'
        }[type]
    elif re.search(r'317614126', goal):
        return {
            'col_name': 'izhivika_goal317614126',
            'project': 'Целепорт',
            'goal': 'Клик на отправку формы (шаг 3)'
        }[type]
    elif re.search(r'317612819', goal):
        return {
            'col_name': 'izhivika_goal317612819',
            'project': 'Целепорт',
            'goal': 'Открыть Целепорт (шаг 1)'
        }[type]
    elif re.search(r'317612820', goal):
        return {
            'col_name': 'izhivika_goal317612820',
            'project': 'Целепорт',
            'goal': 'Отправка номера (шаг 2)'
        }[type]
    elif re.search(r'317612821', goal):
        return {
            'col_name': 'izhivika_goal317612821',
            'project': 'Целепорт',
            'goal': 'Отправка формы и паспортных данных и ИНН (шаг 3)'
        }[type]
    elif re.search(r'322894105', goal):
        return {
            'col_name': 'izhivika_goal322894105',
            'project': 'Формула счастья',
            'goal': 'Финишная страница, опрос завершен'
        }[type]
    elif re.search(r'309413255', goal):
        return {
            'col_name': 'samoletum_goal309413255',
            'project': 'Самолетум',
            'goal': 'Отправка формы и паспортных данных и ИНН (шаг 4)'
        }[type]
    elif re.search(r'323715942', goal):
        return {
            'col_name': 'samoletum_goal323715942',
            'project': 'Самолетум',
            'goal': 'Клик на Открыть Целепорт (шаг 1)'
        }[type]
    elif re.search(r'329183103', goal):
        return {
            'col_name': 'samoletum_goal329183103',
            'project': 'Самолетум',
            'goal': 'Отправка номера (шаг 2)'
        }[type]
    elif re.search(r'326177868', goal):
        return {
            'col_name': 'samoletum_goal326177868',
            'project': 'Самолетум',
            'goal': 'Клик на отправку формы (шаг 3)'
        }[type]
    elif re.search(r'336485646', goal):
        return {
            'col_name': 'zagorodfest_goal336485646',
            'project': 'Загород Fest',
            'goal': 'Клики по "Хочу на фестиваль" в шапке сайта'
        }[type]
    elif re.search(r'336486040', goal):
        return {
            'col_name': 'zagorodfest_goal336486040',
            'project': 'Загород Fest',
            'goal': 'Клик по кнопке "Хочу на фестиваль" в блоке с таймером'
        }[type]
    elif re.search(r'336486196', goal):
        return {
            'col_name': 'zagorodfest_goal336486196',
            'project': 'Загород Fest',
            'goal': 'Клик по кнопке "Хочу на фестиваль" в форме'
        }[type]
    elif re.search(r'336487337', goal):
        return {
            'col_name': 'zagorodfest_goal336487337',
            'project': 'Загород Fest',
            'goal': 'Отправка форм c поддомена fest.samolet.ru'
        }[type]
    else:
        return 'NaN - ' + goal