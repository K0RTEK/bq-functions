import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_metrika_goal_name(goal):
    goal = is_none(goal)
    if re.search(r'130361575', goal):
        return 'Посмотрели Акции и Скидки'
    elif re.search(r'204085729', goal):
        return 'Автоцель: отправка формы'
    elif re.search(r'229295889', goal):
        return 'Весь сайт. Отправлена форма'
    elif re.search(r'254559703', goal):
        return 'ФСК // Посетили выбор квартир в ЖК'
    elif re.search(r'296239163', goal):
        return 'Шереметьевский // Просмотр квартир'
    elif re.search(r'297423180', goal):
        return 'Дружба // Посетили выбор квартир'
    elif re.search(r'180465367', goal):
        return 'Молодежный // Посетили выбор квартир'
    elif re.search(r'130361446', goal):
        return 'Олимп // Посетили выбор квартир'
    elif re.search(r'136794757', goal):
        return 'Режиссёр // Посетили выбор квартир'
    elif re.search(r'47819251', goal):
        return 'Рихард // Посетили выбор квартир'
    elif re.search(r'136708495', goal):
        return 'Римский // Посетили выбор квартир'
    elif re.search(r'226780776', goal):
        return 'Скай Гарден // Посетили выбор квартир'
    elif re.search(r'151241110', goal):
        return 'Сидней Сити // Посетили выбор квартир'
    elif re.search(r'251222896', goal):
        return 'Сидней Прайм // Посетили выбор квартир'
    elif re.search(r'297423123', goal):
        return 'THE LAKE // Посетили выбор квартир'
    elif re.search(r'130290436', goal):
        return 'Парк Апрель // Посетили выбор квартир'
    elif re.search(r'297423133', goal):
        return 'Сабурово Клаб // Посетили выбор квартир'
    elif re.search(r'296355203', goal):
        return 'Жаворонки // Посетили выбор квартир'
    return f'NaN - {goal}'