import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_segment_1(campaign_name):

    campaign_name_lower = is_none(campaign_name.lower())

    if re.search(r'( |_|-|^)brand( |-|_|$)', campaign_name_lower) and not re.search(r'( |_|-|^)network( |-|_|$)', campaign_name_lower):
        return 'Бренд'
    elif re.search(r'( |_|-|^)search( |-|_|$)', campaign_name_lower) and not re.search(r'(_|-|^)brand( |-|_|$)', campaign_name_lower):
        return 'Поиск'
    elif re.search(r'( |_|-|^)network( |-|_|$)', campaign_name_lower) and not re.search(r'( |_|-|^)retargeting( |-|_|$)|( |_|-|^)remarketing( |-|_|$)|( |_|-|^)retarget( |-|_|$)|( |_|-|^)remarket( |-|_|$)', campaign_name_lower):
        return 'РСЯ'
    elif re.search(r'( |_|-|^)mc( |-|_|$)', campaign_name_lower) and not re.search(r'Без исключений', campaign_name_lower):
        return 'Мастер кампаний'
    elif re.search(r'( |_|-|^)tc( |-|_|$)', campaign_name_lower) and not re.search(r'Без исключений', campaign_name_lower):
        return 'Товарная кампания'
    elif re.search(r'( |_|-|^)визитка( |-|_|$)|(^|_| |-)vizitka( |-|_|$)', campaign_name_lower) and not re.search(r'Без исключений', campaign_name_lower):
        return 'Визитка'
    elif re.search(r'( |_|-|^)retargeting( |-|_|$)|( |_|-|^)remarketing( |-|_|$)|( |_|-|^)retarget( |-|_|$)|( |_|-|^)remarket( |-|_|$)', campaign_name_lower) and not re.search(r'Без исключений', campaign_name_lower):
        return 'Ретаргетинг'
    else:
        return 'Прочее'