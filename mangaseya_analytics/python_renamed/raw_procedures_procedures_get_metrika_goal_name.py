import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_metrika_goal_name(goal):
    goal = is_none(goal)
    if re.search(r'329061850', goal):
        return 'ym_scroll_100'
    elif re.search(r'329062055', goal):
        return 'ym_time_3_min'
    elif re.search(r'329062356', goal):
        return 'ym_telephone_click_header'
    elif re.search(r'329062406', goal):
        return 'ym_telephone_click_footer'
    else:
        return 'NaN - ' + goal if goal else ''