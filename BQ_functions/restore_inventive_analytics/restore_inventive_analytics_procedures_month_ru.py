def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def month_ru(date):
    month = date.month
    if month == 1:
        return 'январь'
    elif month == 2:
        return 'февраль'
    elif month == 3:
        return 'март'
    elif month == 4:
        return 'апрель'
    elif month == 5:
        return 'май'
    elif month == 6:
        return 'июнь'
    elif month == 7:
        return 'июль'
    elif month == 8:
        return 'август'
    elif month == 9:
        return 'сентябрь'
    elif month == 10:
        return 'октябрь'
    elif month == 11:
        return 'ноябрь'
    elif month == 12:
        return 'декабрь'
    else:
        return 'NaN'
