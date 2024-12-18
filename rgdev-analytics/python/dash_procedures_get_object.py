import re
import datetime as dt

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_object(parameter):
    parameter = is_none(parameter)

    if re.search(r'мих|михалковский|mihalkovskij|mihalkov', parameter):
        return 'Михалковский'
    elif re.search(r'вв|варшавские ворота', parameter):
        return 'Варшавские ворота'
    elif re.search(r'пп2|петровский парк 2|petrovskij\.park\.2', parameter):
        return 'Петровский парк 2'
    elif re.search(r'пп|петровский парк', parameter) and not re.search(r'пп2', parameter):
        return 'Петровский парк'
    elif re.search(r'сп2|семеновский парк 2|семёновский парк 2|semenovskij\.park\.2', parameter):
        return 'Семеновский парк 2'
    elif re.search(r'сп|семеновский парк|семёновский парк', parameter) and not re.search(r'2', parameter):
        return 'Семеновский парк'
    elif re.search(r'фнв|фн|фонвизинский', parameter):
        return 'Фонвизинский'
    elif re.search(r'блт|бт|балтийский', parameter):
        return 'Балтийский'
    elif re.search(r'окп|октябрьское поле|oktyabrskoe\.pole', parameter):
        return 'Октябрьское поле'
    elif re.search(r'ках|каховская', parameter):
        return 'Каховская'
    elif re.search(r'орб|орехово', parameter):
        return 'Орехово-Борисово'
    elif re.search(r'воп|воронцовский парк', parameter):
        return 'Воронцовский парк'

    return 'Не определено'