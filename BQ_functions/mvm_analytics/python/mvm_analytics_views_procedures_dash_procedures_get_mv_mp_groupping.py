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

def get_mv_mp_groupping(data_group, date, source, medium, campaign, content, term):
    # Apply is_none to all arguments
    data_group = is_none(data_group)
    date = dt.date.fromisoformat(is_none(date)) if is_none(date) else None
    source = is_none(source).lower()
    medium = is_none(medium).lower()
    campaign = is_none(campaign).lower()
    content = is_none(content)
    term = is_none(term)

    ### _non-dsh_
    if re.search(r'_non-dsh_', campaign):
        if data_group in ['total_site', 'total_tops']:
            return 'OTHER'
        elif data_group == 'placement':
            return 'non-dsh'
        elif data_group == 'flight':
            return 'alwayson'
        else:
            return 'Other_data'

    ### Mobile исключение
    elif re.search(r'_ios|_aos_', campaign):
        if data_group in ['total_site', 'total_tops']:
            return 'OTHER'
        elif data_group == 'placement':
            return 'non-dsh'
        elif data_group == 'flight':
            return 'alwayson'
        else:
            return 'Other_data'

    ### Вендорские флайты
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

    ### Нерезиденты
    elif source in ['mt', 'vkr'] and medium == 'cpc' and re.search(r'rezedent', campaign):
        if data_group in ['total_site', 'total_tops']:
            return 'OTHER'
        elif data_group == 'placement':
            return 'Нерезиденты'
        elif data_group == 'flight':
            return 'alwayson'
        else:
            return 'Other_data'

    ### Контекст
    elif source == 'yandex' and medium == 'cpc' and re.search(r'_vacansii_', campaign):
        if data_group in ['total_site', 'total_tops']:
            return 'OTHER'
        elif data_group == 'placement':
            return 'Вакансии'
        elif data_group == 'flight':
            return 'alwayson'
        else:
            return 'Other_data'

    ### Федеральный бюджет
    elif source == 'yandex' and medium == 'cpc' and re.search(r'flight', campaign) and re.search(r'fed', campaign) and re.search(r'mg_', campaign):
        if data_group in ['channel', 'total_paid']:
            return 'Контекст'
        elif data_group in ['total_site', 'total_tops']:
            return 'PAID'
        elif data_group == 'flight':
            return 'Контекст'
        else:
            return 'М.Видео | Фед. бюджет'

    ### Докаты IProspect (Бренд)
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

    ### Докаты IProspect (Небренд)
    elif source == 'yandex' and medium == 'cpc' and re.search(r'ipr_', campaign) and not re.search(r'_image_name', campaign):
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

    ### Докаты Другое
    elif source == 'yandex' and medium == 'cpc' and not re.search(r'mg_', campaign):
        if data_group in ['total_site', 'total_tops']:
            return 'PAID'
        elif data_group == 'flight':
            return 'alwayson'
        else:
            return 'Докаты'

    ### POST 2024-01-01
    elif date and date >= dt.date(2024, 1, 1):
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
                return 'М.Видео | РСЯ'

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
                return 'М.Видео | Бренд'

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
                return 'М.Видео | Автотаргетинг+МК'

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
                return 'М.Видео | DSA'

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
                return 'М.Видео | Смарт-баннеры + Ремаркетинг'

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
                return 'М.Видео | Товарная РК'

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
                return 'М.Видео | API (К50)'

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
                return 'М.Видео | Категорийные + Кат-вендорные'

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
                return 'М.Видео | Конкуренты'

        elif source == 'yandex' and medium == 'cpc' and re.search(r'_united_|_epk_', campaign):
            if data_group in ['channel', 'total_paid']:
                return 'Контекст'
            elif data_group == 'placement':
                return 'Яндекс Директ Небренд'
            elif data_group in ['total_site', 'total_tops']:
                return 'PAID'
            elif data_group == 'flight':
                return 'alwayson'
            else:
                return 'М.Видео | ЕПК'

        elif source == 'yandex' and medium == 'cpc' and re.search(r'model_h|model_p', campaign):
            if data_group in ['channel', 'total_paid']:
                return 'Контекст'
            elif data_group == 'placement':
                return 'Яндекс Директ Небренд'
            elif data_group in ['total_site', 'total_tops']:
                return 'PAID'
            elif data_group == 'flight':
                return 'alwayson'
            else:
                return 'М.Видео | Модельные ручные'

    ### ДО 2024-01-01
    elif date and date < dt.date(2024, 1, 1):
        if source == 'yandex' and medium == 'cpc' and re.search(r'_s_|brand_s', campaign) and not re.search(r'smartbanners|_rem', campaign):
            if data_group in ['channel', 'total_paid']:
                return 'Контекст'
            elif data_group == 'placement':
                return 'Яндекс Директ Небренд'
            elif data_group in ['total_site', 'total_tops']:
                return 'PAID'
            elif data_group == 'flight':
                return 'alwayson'
            else:
                return 'Яндекс РСЯ (CPC)'

        elif source == 'yandex' and medium == 'cpc' and re.search(r'_image_name|_brand', campaign) and not re.search(r'_s_', campaign):
            if data_group in ['channel', 'total_paid']:
                return 'Контекст'
            elif data_group == 'placement':
                return 'Яндекс Директ Бренд'
            elif data_group in ['total_site', 'total_tops']:
                return 'PAID'
            elif data_group == 'flight':
                return 'alwayson'
            else:
                return 'Яндекс Бренд (общий)'

        elif source == 'yandex' and medium == 'cpc' and re.search(r'_dsa|_dsa-|shopping', campaign):
            if data_group in ['channel', 'total_paid']:
                return 'Контекст'
            elif data_group == 'placement':
                return 'Яндекс Директ Небренд'
            elif data_group in ['total_site', 'total_tops']:
                return 'PAID'
            elif data_group == 'flight':
                return 'alwayson'
            else:
                return 'Яндекс DSA'

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
                return 'Яндекс Api (к50)'

        elif source == 'yandex' and medium == 'cpc' and re.search(r'smartbanner|_rem', campaign):
            if data_group in ['channel', 'total_paid']:
                return 'Контекст'
            elif data_group == 'placement':
                return 'Яндекс Директ Небренд'
            elif data_group in ['total_site', 'total_tops']:
                return 'PAID'
            elif data_group == 'flight':
                return 'alwayson'
            else:
                return 'Яндекс Ретаргетинг (Смарт-баннеры)'

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
                return 'Яндекс Товарная РК'

        elif source == 'yandex' and medium == 'cpc' and re.search(r'_p_', campaign) and re.search(r'_cat-ven_|_cat_|_category_|_hand_|autotarget|keywords|compet', campaign):
            if data_group in ['channel', 'total_paid']:
                return 'Контекст'
            elif data_group == 'placement':
                return 'Яндекс Директ Небренд'
            elif data_group in ['total_site', 'total_tops']:
                return 'PAID'
            elif data_group == 'flight':
                return 'alwayson'
            else:
                return 'Яндекс Категорийные РК (модельные+катвенд) + Автотаргет'

    ### М.Видео Остальное
    elif source == 'yandex' and medium == 'cpc':
        if data_group in ['channel', 'total_paid']:
            return 'Контекст'
        elif data_group == 'placement':
            return 'Яндекс Директ Небренд'
        elif data_group in ['total_site', 'total_tops']:
            return 'PAID'
        elif data_group == 'flight':
            return 'alwayson'
        else:
            return 'М.Видео | Остальное'

    ### Соцсети
    elif source in ['mt', 'vk', 'vkontakte', 'vkr'] and medium in ['cpc', 'cpm'] and re.search(r'leadads', campaign):
        if data_group in ['total_site', 'total_tops']:
            return 'OTHER'
        elif data_group == 'placement':
            return 'Вакансии'
        elif data_group == 'flight':
            return 'alwayson'
        else:
            return 'Other_data'

    elif source in ['mt', 'vk', 'vkontakte', 'vkr'] and medium in ['cpc', 'cpm'] and re.search(r'flight', campaign) and re.search(r'fed', campaign):
        if data_group in ['channel', 'total_paid']:
            return 'Соцсети'
        elif data_group in ['total_site', 'total_tops']:
            return 'PAID'
        elif data_group == 'flight':
            return 'Соцсети'
        else:
            return 'Соцсети Фед. бюджет'

    elif source in ['mt', 'vk', 'vkontakte', 'vkr'] and medium in ['cpc', 'cpm'] and re.search(r'_cpm_ny-sale23', campaign):
        if data_group in ['channel', 'total_paid']:
            return 'Соцсети'
        elif data_group == 'placement':
            return 'VK Reklama'
        elif data_group in ['total_site', 'total_tops']:
            return 'PAID'
        elif data_group == 'flight':
            return 'alwayson'
        else:
            return 'Соцсети Media'

    if data_group in ['total_tops', 'total_site']:
        return 'OTHER'
    elif data_group == 'flight':
        return 'alwayson'
    else:
        return 'Other_data'
