import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def cont_category(campaign):
    campaign = is_none(campaign)
    if re.search(r'_tv_', campaign):
        return 'Телевизоры'
    elif re.search(r'smartphone', campaign):
        return 'Смартфоны'
    elif re.search(r'conditioners', campaign):
        return 'Кондиционеры'
    elif re.search(r'notebook', campaign):
        return 'Ноутбуки'
    elif re.search(r'duhovie-shkafy|ovens', campaign):
        return 'Духовые шкафы'
    elif re.search(r'fridges|refrigerators|holodilniki', campaign):
        return 'Холодильники'
    elif re.search(r'obogrevateli', campaign):
        return 'Обогреватели'
    elif re.search(r'laptops|notebook', campaign):
        return 'Ноутбуки'
    elif re.search(r'planshety|tablets', campaign):
        return 'Планшеты'
    elif re.search(r'game-console', campaign):
        return 'Игровые консоли'
    elif re.search(r'dyson', campaign):
        return 'Дайсон'
    elif re.search(r'kitchen|cookers|cooktops', campaign):
        return 'Панели и плиты'
    elif re.search(r'pylesosy', campaign):
        return 'Пылесосы'
    elif re.search(r'sushilnye-mashiny|_dm_', campaign):
        return 'Сушильные машины'
    elif re.search(r'coffee', campaign):
        return 'Кофемашины'
    elif re.search(r'vytyazhki', campaign):
        return 'Вытяжки'
    elif re.search(r'posudomoechnye-mashiny|_dw_', campaign):
        return 'Посудомоечные машины'
    elif re.search(r'_smart-chasy_', campaign):
        return 'Умные часы'
    elif re.search(r'vstroyka', campaign):
        return 'Встройка'
    elif re.search(r'stiralnie-mashiny|stiralnye-mashiny', campaign):
        return 'Стиральные машины'
    else:
        return 'NaN'