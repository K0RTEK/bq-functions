import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_segment(date, ad_name):
    ad_name = is_none(ad_name)
    if re.search(r'mktr-|maketrue|-mktr', ad_name):
        return 'Мейктру'
    elif re.search(r'dinrem-prs', ad_name):
        return 'Проспектинг'
    elif re.search(r'lal', ad_name):
        return 'LAL'
    elif re.search(r'keys', ad_name) and not re.search(r'supergeo|naruzh', ad_name):
        return 'Ключи'
    elif re.search(r'supergeo|naruzh', ad_name) and not re.search(r'keys', ad_name):
        return 'Cупергео'
    elif re.search(r'keys', ad_name) and re.search(r'supergeo|naruzh', ad_name):
        return 'Ключи+Супергео'
    elif re.search(r'ret', ad_name):
        return 'Статрет'
    elif re.search(r'dinrem', ad_name):
        return 'Динрем'
    elif re.search(r'amdt', ad_name):
        return 'Амбердата'
    elif re.search(r'dmp', ad_name):
        return 'ДМП сегмент'
    elif re.search(r'sub', ad_name):
        return 'Подписчики'
    elif re.search(r'socdem|pars|new-built|finance|ipoteka|family|education|arndv|arndrealty|avto|repair|izhs', ad_name) and not re.search(r'keys', ad_name):
        return 'Интересы'
    else:
        return 'Интересы'