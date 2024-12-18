import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_metrika_goal_name(parameter):
    parameter = is_none(parameter)
    goal_mapping = {
        'tempgoalprefix_goal273736797reaches': 'Время на сайте от 180 секунд',
        'tempgoalprefix_goal231454727reaches': 'Автоцель: отправка формы',
        'tempgoalprefix_goal273736915reaches': 'Просмотрено 75% ленда (скролинг)',
        'tempgoalprefix_goal189922555reaches': 'Отправки заявки NEW',
        'tempgoalprefix_goal273733838reaches': 'Время на сайте от 180 секунд',
        'tempgoalprefix_goal273733856reaches': 'Просмотрено 75% ленда (скролинг)',
    }
    return goal_mapping.get(parameter, None)