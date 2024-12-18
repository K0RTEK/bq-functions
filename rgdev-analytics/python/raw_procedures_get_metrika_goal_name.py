import re
import datetime as dt

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_metrika_goal_name(goal):
    goal_lower = is_none(goal)

    if re.search(r'111111111', goal_lower):
        return 'ЦЕЛЬ'
    else:
        return f'NaN - {goal}'