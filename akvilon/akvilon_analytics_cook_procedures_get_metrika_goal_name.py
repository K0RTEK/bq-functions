import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_metrika_goal_name(goal):
    goal = is_none(goal)
    goal_mapping = {
        '140137726': 'Амарант // Посетил страницу Контакты',
        '140137636': 'Амарант // Посетил страницу О проекте',
        '270238386': 'Амарант // Клик по номеру Телефона',
        '140137618': 'Амарант // Посетил страницу "Планировки/квартиры"'
    }
    for key, value in goal_mapping.items():
        if re.search(key, goal):
            return value
    return f'NaN - {goal}'