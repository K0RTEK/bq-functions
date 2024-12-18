import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_segment_2(campaign_name):
    campaign_name = is_none(campaign_name)
    if re.search(r'( |_|-|^)brand( |-|_|$)', campaign_name) and \
       not re.search(r'Без исключений', campaign_name):
        return 'Бренд'
    elif re.search(r'( |_|-|^)compet( |-|_|$)|( |_|-|^)competitors( |-|_|$)', campaign_name) and \
         not re.search(r'Без исключений', campaign_name):
        return 'Конкуренты'
    elif re.search(r'( |_|-|^)geo( |-|_|$)', campaign_name) and \
         not re.search(r'Без исключений', campaign_name):
        return 'Гео'
    elif re.search(r'(_|-|^)generic( |-|_|$)', campaign_name) and \
         not re.search(r'autotargeting', campaign_name):
        return 'Общие'
    elif re.search(r'( |_|-|^)визитка( |-|_|$)|(^|_| |-)vizitka( |-|_|$)', campaign_name) and \
         not re.search(r'Без исключений', campaign_name):
        return 'Визитка'
    elif not re.search(r'( |_|-|^)compet( |-|_|$)|( |_|-|^)competitors( |-|_|$)|( |_|-|^)geo( |-|_|$)|( |_|-|^)brand( |-|_|$)', campaign_name):
        return 'Общие'
    elif re.search(r'( |_|-|^)retargeting( |-|_|$)|( |_|-|^)remarketing( |-|_|$)|( |_|-|^)retarget( |-|_|$)|( |_|-|^)remarket( |-|_|$)', campaign_name) and \
         not re.search(r'Без исключений', campaign_name):
        return 'Ретаргетинг'
    elif re.search(r'( |_|-|^)search( |-|_|$)', campaign_name):
        return 'Поиск'
    elif re.search(r'( |_|-|^)network( |-|_|$)', campaign_name):
        return 'РСЯ'
    elif re.search(r'( |_|-|^)mc( |-|_|$)', campaign_name) and \
         not re.search(r'Без исключений', campaign_name):
        return 'Мастер кампаний'
    elif re.search(r'( |_|-|^)tc( |-|_|$)', campaign_name) and \
         not re.search(r'Без исключений', campaign_name):
        return 'Товарная кампания'
    else:
        return 'Прочее'
