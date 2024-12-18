import re
import datetime as dt

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_mv_mp_groupping(data_group, date, source, medium, campaign, content, term):
    # Apply is_none to all inputs
    data_group = is_none(data_group).lower()
    date = dt.date.today() if is_none(date) == '' else dt.datetime.strptime(is_none(date), "%Y-%m-%d").date()
    source = is_none(source).lower()
    medium = is_none(medium).lower()
    campaign = is_none(campaign).lower()
    content = is_none(content).lower()
    term = is_none(term).lower()

    if re.search(r'_non-dsh_', campaign):
        if data_group in ('total_site', 'total_tops'):
            return 'OTHER'
        elif data_group == 'placement':
            return 'non-dsh'
        elif data_group == 'flight':
            return 'alwayson'
        else:
            return 'Other_data'

    elif source == 'yandex' and medium == 'cpc' and re.search(r'flight', campaign) and not re.search(r'fed', campaign):
        if data_group in ('channel', 'total_paid'):
            return 'Флайты Венд. бюджет'
        elif data_group in ('total_site', 'total_tops'):
            return 'PAID'
        elif data_group == 'flight':
            return 'Контекст'
        else:
            return 'Контекст Венд. бюджет'

    elif source in ('mt', 'vk', 'vkontakte', 'vkr') and medium in ('cpc', 'cpm') and re.search(r'flight', campaign) and not re.search(r'fed', campaign):
        if data_group in ('channel', 'total_paid'):
            return 'Флайты Венд. бюджет'
        elif data_group in ('total_site', 'total_tops'):
            return 'PAID'
        elif data_group == 'flight':
            return 'Соцсети'
        else:
            return 'Соцсети Венд. бюджет'

    elif source in ('mt', 'vkr') and medium == 'cpc' and re.search(r'rezedent', campaign):
        if data_group in ('total_site', 'total_tops'):
            return 'OTHER'
        elif data_group == 'placement':
            return 'Нерезиденты'
        elif data_group == 'flight':
            return 'alwayson'
        else:
            return 'Other_data'

    elif source == 'yandex' and medium == 'cpc' and re.search(r'_vacansii_', campaign):
        if data_group in ('total_site', 'total_tops'):
            return 'OTHER'
        elif data_group == 'placement':
            return 'Вакансии'
        elif data_group == 'flight':
            return 'alwayson'
        else:
            return 'Other_data'

    elif source == 'yandex' and medium == 'cpc' and re.search(r'flight', campaign) and re.search(r'fed', campaign):
        if data_group in ('channel', 'total_paid'):
            return 'Контекст'
        elif data_group in ('total_site', 'total_tops'):
            return 'PAID'
        elif data_group == 'flight':
            return 'Контекст'
        else:
            return 'Яндекс Директ Фед. бюджет'

    elif source == 'yandex' and medium == 'cpc' and re.search(r'_image_name', campaign) and not re.search(r'mg_', campaign):
        if data_group in ('channel', 'total_paid'):
            return 'Докаты'
        elif data_group == 'placement':
            return 'Докаты (iProspect)'
        elif data_group in ('total_site', 'total_tops'):
            return 'PAID'
        elif data_group == 'flight':
            return 'alwayson'
        else:
            return 'Докаты IProspect (Бренд)'

    elif source == 'yandex' and medium == 'cpc' and not re.search(r'mg_', campaign) and not re.search(r'_image_name', campaign):
        if data_group in ('channel', 'total_paid'):
            return 'Докаты'
        elif data_group == 'placement':
            return 'Докаты (iProspect)'
        elif data_group in ('total_site', 'total_tops'):
            return 'PAID'
        elif data_group == 'flight':
            return 'alwayson'
        else:
            return 'Докаты IProspect (Небренд)'

    elif source == 'yandex' and medium == 'cpc' and re.search(r'_s_|brand_s', campaign) and not re.search(r'smartbanners|_rem', campaign) and date >= dt.date(2024, 1, 1):
        if data_group in ('channel', 'total_paid'):
            return 'Контекст'
        elif data_group == 'placement':
            return 'Яндекс Директ Небренд'
        elif data_group in ('total_site', 'total_tops'):
            return 'PAID'
        elif data_group == 'flight':
            return 'alwayson'
        else:
            return 'М.Видео | РСЯ'

    elif source == 'yandex' and medium == 'cpc' and re.search(r'_image_name|_brand', campaign) and not re.search(r'_s_', campaign) and date >= dt.date(2024, 1, 1):
        if data_group in ('channel', 'total_paid'):
            return 'Контекст'
        elif data_group == 'placement':
            return 'Яндекс Директ Бренд'
        elif data_group in ('total_site', 'total_tops'):
            return 'PAID'
        elif data_group == 'flight':
            return 'alwayson'
        else:
            return 'М.Видео | Бренд'

    elif source == 'yandex' and medium == 'cpc' and re.search(r'_dsa|_dsa-|shopping', campaign) and date >= dt.date(2024, 1, 1):
        if data_group in ('channel', 'total_paid'):
            return 'Контекст'
        elif data_group == 'placement':
            return 'Яндекс Директ Небренд'
        elif data_group in ('total_site', 'total_tops'):
            return 'PAID'
        elif data_group == 'flight':
            return 'alwayson'
        else:
            return 'М.Видео | DSA'

    elif source == 'yandex' and medium == 'cpc' and re.search(r'_api_', campaign) and date >= dt.date(2024, 1, 1):
        if data_group in ('channel', 'total_paid'):
            return 'Контекст'
        elif data_group == 'placement':
            return 'Яндекс Директ Небренд'
        elif data_group in ('total_site', 'total_tops'):
            return 'PAID'
        elif data_group == 'flight':
            return 'alwayson'
        else:
            return 'М.Видео | API (K50)'

    elif source == 'yandex' and medium == 'cpc' and re.search(r'smartbanner|_rem', campaign) and date >= dt.date(2024, 1, 1):
        if data_group in ('channel', 'total_paid'):
            return 'Контекст'
        elif data_group == 'placement':
            return 'Яндекс Директ Небренд'
        elif data_group in ('total_site', 'total_tops'):
            return 'PAID'
        elif data_group == 'flight':
            return 'alwayson'
        else:
            return 'М.Видео | Смарт баннеры + Ремаркетинг'

    elif source == 'yandex' and medium == 'cpc' and re.search(r'_tk_', campaign) and date >= dt.date(2024, 1, 1):
        if data_group in ('channel', 'total_paid'):
            return 'Контекст'
        elif data_group == 'placement':
            return 'Яндекс Директ Небренд'
        elif data_group in ('total_site', 'total_tops'):
            return 'PAID'
        elif data_group == 'flight':
            return 'alwayson'
        else:
            return 'М.Видео | Товарные кампании'

    elif source == 'yandex' and medium == 'cpc' and re.search(r'_p_', campaign) and re.search(r'_cat-ven_|_cat_|_category_|_hand_|autotarget|keywords|compet', campaign) and date >= dt.date(2024, 1, 1):
        if data_group in ('channel', 'total_paid'):
            return 'Контекст'
        elif data_group == 'placement':
            return 'Яндекс Директ Небренд'
        elif data_group in ('total_site', 'total_tops'):
            return 'PAID'
        elif data_group == 'flight':
            return 'alwayson'
        else:
            return 'Яндекс Категорийные РК (модельные+катвенд) + Автотаргет'

    return 'Other_data' if data_group not in ('total_tops', 'total_site', 'flight') else 'alwayson' if data_group == 'flight' else 'OTHER'
