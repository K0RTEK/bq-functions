import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_segment_1(campaign_name):
    campaign_name = is_none(campaign_name)
    if re.search(r'( |_|-|^)brand( |-|_|$)', campaign_name) and \
       not re.search(r'( |_|-|^)network( |-|_|$)', campaign_name):
        return 'Бренд'
    elif re.search(r'( |_|-|^)search( |-|_|$)|( |_|-|^)s( |-|_|$)', campaign_name) and \
         not re.search(r'(_|-|^)brand( |-|_|$)', campaign_name):
        return 'Поиск'
    elif re.search(r'( |_|-|^)performance( |-|_|$)', campaign_name) and \
         not re.search(r'Без исключений', campaign_name):
        return 'Мастер кампаний'
    elif re.search(r'( |_|-|^)mc( |-|_|$)', campaign_name) and \
         not re.search(r'Без исключений', campaign_name):
        return 'Мастер кампаний'
    elif re.search(r'( |_|-|^)tc( |-|_|$)|( |_|-|^)tg( |-|_|$)', campaign_name) and \
         not re.search(r'Без исключений', campaign_name):
        return 'Товарная кампания'
    elif re.search(r'( |_|-|^)визитка( |-|_|$)|(^|_| |-)vizitka( |-|_|$)', campaign_name) and \
         not re.search(r'Без исключений', campaign_name):
        return 'Визитка'
    elif re.search(r'( |_|-|^)network( |-|_|$)|( |_|-|^)n( |-|_|$)', campaign_name):
        return 'РСЯ'
    else:
        return 'Прочее'