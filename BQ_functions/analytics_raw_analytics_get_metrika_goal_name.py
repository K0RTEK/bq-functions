def analytics_raw_analytics_get_metrika_goal_name(parameter):
    goal_mapping = {
        'tempgoalprefix_goal273736797reaches': 'Время на сайте от 180 секунд',
        'tempgoalprefix_goal231454727reaches': 'Автоцель: отправка формы',
        'tempgoalprefix_goal273736915reaches': 'Просмотрено 75% ленда (скролинг)',
        'tempgoalprefix_goal189922555reaches': 'Отправки заявки NEW',
        'tempgoalprefix_goal273733838reaches': 'Время на сайте от 180 секунд',
        'tempgoalprefix_goal273733856reaches': 'Просмотрено 75% ленда (скролинг)',
    }

    # Возвращаем значение, соответствующее ключу parameter
    return goal_mapping.get(parameter, None)

# Пример использования функции
print(analytics_raw_analytics_get_metrika_goal_name('tempgoalprefix_goal273736797reaches'))  # Время на сайте от 180 секунд
print(analytics_raw_analytics_get_metrika_goal_name('tempgoalprefix_goal231454727reaches'))  # Автоцель: отправка формы
