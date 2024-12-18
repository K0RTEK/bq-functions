import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_bonus(date, parameter, account_name, cost):
    account_name = is_none(account_name)
    parameter = is_none(parameter)
    cost = int(cost)
    if parameter == 'get_cost' and 'bonus' not in account_name:
        return cost * 1.2 * 0.9865
    elif parameter == 'get_cost' and 'bonus' in account_name:
        return cost * 1.2 * 0.9865 * 0.1
    elif parameter == 'get_bonus' and 'bonus' not in account_name:
        return cost * 0
    elif parameter == 'get_bonus' and 'bonus' in account_name:
        return cost * 0.9
    else:
        return None