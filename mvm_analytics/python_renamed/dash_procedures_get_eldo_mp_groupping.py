import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

import re
import datetime as dt

def is_none(value):
    return value if value is not None else ''

def get_eldo_mp_groupping(data_group, date, source, medium, campaign, content, term):
    # Apply is_none to all arguments
    data_group = is_none(data_group)
    date = dt.date.fromisoformat(is_none(date)) if is_none(date) else None
    source = is_none(source).lower()
    medium = is_none(medium).lower()
    campaign = is_none(campaign).lower()
    content = is_none(content)
    term = is_none(term)

    # Define the logic as per the SQL CASE statement
    if re.search(r'_non-dsh_', campaign) or re.search(r'_ios|_aos_', campaign):
        if data_group in ['total_site', 'total_tops']:
            return 'OTHER'
        elif data_group == 'placement':
            return 'non-dsh'
        elif data_group == 'flight':
            return 'alwayson'
        else:
            return 'Other_data'

    elif source == 'yandex' and medium == 'cpc' and re.search(r'flight', campaign) and re.search(r'mg_', campaign) and not re.search(r'fed', campaign):
        if data_group in ['channel', 'total_paid']:
            return 'Флайты Венд. бюджет'
        elif data_group in ['total_site', 'total_tops']:
            return 'PAID'
        elif data_group == 'flight':
            return 'Контекст'
        else:
            return 'Контекст Венд. бюджет'

    elif source in ['mt', 'vk', 'vkontakte', 'vkr'] and medium in ['cpc', 'cpm'] and re.search(r'flight', campaign) and re.search(r'mg_', campaign) and not re.search(r'fed', campaign):
        if data_group in ['channel', 'total_paid']:
            return 'Флайты Венд. бюджет'
        elif data_group in ['total_site', 'total_tops']:
            return 'PAID'
        elif data_group == 'flight':
            return 'Соцсети'
        else:
            return 'Соцсети Венд. бюджет'

    elif source in ['mt', 'vkr'] and medium == 'cpc' and re.search(r'rezedent', campaign):
        if data_group in ['total_site', 'total_tops']:
            return 'OTHER'
        elif data_group == 'placement':
            return 'Нерезиденты'
        elif data_group == 'flight':
            return 'alwayson'
        else:
            return 'Other_data'

    elif source == 'yandex' and medium == 'cpc' and re.search(r'_vacansii_', campaign):
        if data_group in ['total_site', 'total_tops']:
            return 'OTHER'
        elif data_group == 'placement':
            return 'Вакансии'
        elif data_group == 'flight':
            return 'alwayson'
        else:
            return 'Other_data'

    elif source == 'yandex' and medium == 'cpc' and re.search(r'flight', campaign) and re.search(r'fed', campaign) and re.search(r'mg_', campaign):
        if data_group in ['channel', 'total_paid']:
            return 'Контекст'
        elif data_group in ['total_site', 'total_tops']:
            return 'PAID'
        elif data_group == 'flight':
            return 'Контекст'
        else:
            return 'Эльдорадо | Фед. бюджет'

    elif source == 'yandex' and medium == 'cpc' and re.search(r'ipr_', campaign) and re.search(r'_image_name', campaign):
        if data_group in ['channel', 'total_paid']:
            return 'Докаты'
        elif data_group == 'placement':
            return 'Докаты (iProspect)'
        elif data_group in ['total_site', 'total_tops']:
            return 'PAID'
        elif data_group == 'flight':
            return 'alwayson'
        else:
            return 'Докаты IProspect (Бренд)'

    elif source == 'yandex' and medium == 'cpc' and re.search(r'ipr', campaign) and not re.search(r'_image_name', campaign):
        if data_group in ['channel', 'total_paid']:
            return 'Докаты'
        elif data_group == 'placement':
            return 'Докаты (iProspect)'
        elif data_group in ['total_site', 'total_tops']:
            return 'PAID'
        elif data_group == 'flight':
            return 'alwayson'
        else:
            return 'Докаты IProspect (Небренд)'

    elif source == 'yandex' and medium == 'cpc' and not re.search(r'mg_', campaign):
        if data_group in ['total_site', 'total_tops']:
            return 'PAID'
        elif data_group == 'flight':
            return 'alwayson'
        else:
            return 'Докаты'

    elif date and date >= dt.date(2023, 10, 1):
        if source == 'yandex' and medium == 'cpc' and re.search(r'_s_', campaign) and not re.search(r'smartbanners|_rem', campaign):
            if data_group in ['channel', 'total_paid']:
                return 'Контекст'
            elif data_group == 'placement':
                return 'Яндекс Директ Небренд'
            elif data_group in ['total_site', 'total_tops']:
                return 'PAID'
            elif data_group == 'flight':
                return 'alwayson'
            else:
                return 'Эльдорадо | РСЯ'

        elif source == 'yandex' and medium == 'cpc' and re.search(r'_image_', campaign) and re.search(r'_p_', campaign):
            if data_group in ['channel', 'total_paid']:
                return 'Контекст'
            elif data_group == 'placement':
                return 'Яндекс Директ Бренд'
            elif data_group in ['total_site', 'total_tops']:
                return 'PAID'
            elif data_group == 'flight':
                return 'alwayson'
            else:
                return 'Эльдорадо | Бренд'

        elif source == 'yandex' and medium == 'cpc' and re.search(r'_autotarget_|_mc_', campaign):
            if data_group in ['channel', 'total_paid']:
                return 'Контекст'
            elif data_group == 'placement':
                return 'Яндекс Директ Небренд'
            elif data_group in ['total_site', 'total_tops']:
                return 'PAID'
            elif data_group == 'flight':
                return 'alwayson'
            else:
                return 'Эльдорадо | Автотаргетинг+МК'

        elif source == 'yandex' and medium == 'cpc' and re.search(r'_dsa|shopping', campaign):
            if data_group in ['channel', 'total_paid']:
                return 'Контекст'
            elif data_group == 'placement':
                return 'Яндекс Директ Небренд'
            elif data_group in ['total_site', 'total_tops']:
                return 'PAID'
            elif data_group == 'flight':
                return 'alwayson'
            else:
                return 'Эльдорадо | DSA'

        elif source == 'yandex' and medium == 'cpc' and re.search(r'smartbanner|_rem', campaign) and not re.search(r'_competitors_', campaign):
            if data_group in ['channel', 'total_paid']:
                return 'Контекст'
            elif data_group == 'placement':
                return 'Яндекс Директ Небренд'
            elif data_group in ['total_site', 'total_tops']:
                return 'PAID'
            elif data_group == 'flight':
                return 'alwayson'
            else:
                return 'Эльдорадо | Смарт-баннеры + Ремаркетинг'

        elif source == 'yandex' and medium == 'cpc' and re.search(r'_tk_', campaign):
            if data_group in ['channel', 'total_paid']:
                return 'Контекст'
            elif data_group == 'placement':
                return 'Яндекс Директ Небренд'
            elif data_group in ['total_site', 'total_tops']:
                return 'PAID'
            elif data_group == 'flight':
                return 'alwayson'
            else:
                return 'Эльдорадо | Товарная РК'

        elif source == 'yandex' and medium == 'cpc' and re.search(r'_api_', campaign):
            if data_group in ['channel', 'total_paid']:
                return 'Контекст'
            elif data_group == 'placement':
                return 'Яндекс Директ Небренд'
            elif data_group in ['total_site', 'total_tops']:
                return 'PAID'
            elif data_group == 'flight':
                return 'alwayson'
            else:
                return 'Эльдорадо | API (К50)'

        elif source == 'yandex' and medium == 'cpc' and re.search(r'category|cat-ven', campaign):
            if data_group in ['channel', 'total_paid']:
                return 'Контекст'
            elif data_group == 'placement':
                return 'Яндекс Директ Небренд'
            elif data_group in ['total_site', 'total_tops']:
                return 'PAID'
            elif data_group == 'flight':
                return 'alwayson'
            else:
                return 'Эльдорадо | Категорийные + Кат-вендорные'

        elif source == 'yandex' and medium == 'cpc' and re.search(r'competitors', campaign):
            if data_group in ['channel', 'total_paid']:
                return 'Контекст'
            elif data_group == 'placement':
                return 'Яндекс Директ Небренд'
            elif data_group in ['total_site', 'total_tops']:
                return 'PAID'
            elif data_group == 'flight':
                return 'alwayson'
            else:
                return 'Эльдорадо | Конкуренты'


    if data_group in ['total_tops', 'total_site']:
        return 'OTHER'
    elif data_group == 'flight':
        return 'alwayson'
    else:
        return 'Other_data'
