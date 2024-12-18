import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_metrika_goal_name(goal):
    goal = is_none(goal)
    if re.search(r'140137726', goal):
        return 'nan'
    else:
        return f'NaN - {goal}'