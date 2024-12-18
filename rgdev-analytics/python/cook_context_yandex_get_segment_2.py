import re
import datetime as dt

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_segment_2(campaign_name):
    campaign_name = is_none(campaign_name)
    return (
        'Бренд' if re.search(r'( |_|-|^)brand( |-|_|$)', campaign_name) and not re.search(r' ', campaign_name) else
        'Конкуренты' if re.search(r'( |_|-|^)compet( |-|_|$)|( |_|-|^)competitors( |-|_|$)', campaign_name) and not re.search(r' ', campaign_name) else
        'Гео' if re.search(r'( |_|-|^)geo( |-|_|$)', campaign_name) and not re.search(r' ', campaign_name) else
        'Общие' if re.search(r'(_|-|^)generic( |-|_|$)', campaign_name) and not re.search(r'autotargeting', campaign_name) else
        'Визитка' if re.search(r'( |_|-|^)визитка( |-|_|$)|(^|_| |-)vizitka( |-|_|$)', campaign_name) and not re.search(r' ', campaign_name) else
        'Ретаргетинг' if re.search(r'( |_|-|^)retargeting( |-|_|$)|( |_|-|^)remarketing( |-|_|$)|( |_|-|^)retarget( |-|_|$)|( |_|-|^)remarket( |-|_|$)', campaign_name) and not re.search(r' ', campaign_name) else
        'Поиск' if re.search(r'( |_|-|^)search( |-|_|$)', campaign_name) else
        'РСЯ' if re.search(r'( |_|-|^)network( |-|_|$)', campaign_name) else
        'Мастер кампаний' if re.search(r'( |_|-|^)mc( |-|_|$)', campaign_name) and not re.search(r' ', campaign_name) else
        'Товарная кампания' if re.search(r'( |_|-|^)tc( |-|_|$)', campaign_name) and not re.search(r' ', campaign_name) else
        'Прочее'
    )