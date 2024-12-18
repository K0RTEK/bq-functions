import re
import datetime as dt

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()
    


def get_adv_owner(date, project, source, medium, campaign, content, term):
    date = is_none(date)
    project = is_none(project)
    source = is_none(source)
    medium = is_none(medium)
    campaign = is_none(campaign)
    content = is_none(content)
    term = is_none(term)

    try:
        date = dt.datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        date = None

    def is_in_date_range(start_date, end_date, date_to_check):
        return start_date <= date_to_check <= end_date

    if date is not None and date >= dt.date(2024, 1, 1) and project == 'mvideo' and source == 'yandex' and medium == 'cpc' and not re.search(r'flight', campaign.lower()):
        return 'non-MGCom'

    elif date is not None and is_in_date_range(dt.date(2023, 11, 1), dt.date(2023, 12, 31), date) and project == 'mvideo' and source == 'yandex' and medium == 'cpc':
        if (re.search(r'_api_', campaign.lower()) or
            (re.search(r'_image_name|_brand', campaign.lower()) and not re.search(r'_s_', campaign.lower())) or
            (re.search(r'_s_|brand_s', campaign.lower()) and not re.search(r'smartbanners|_rem', campaign.lower())) or
            (re.search(r'_p_', campaign.lower()) and re.search(r'_cat-ven_|_cat_|_category_|_hand_|autotarget|keywords|compet', campaign.lower()))):
            return 'non-MGCom'

    elif date is not None and is_in_date_range(dt.date(2023, 2, 1), dt.date(2023, 11, 1), date) and project == 'mvideo' and source == 'yandex' and medium == 'cpc' and not re.search(r'flight', campaign.lower()) and re.search(r'image', campaign.lower()):
        return 'non-MGCom'

    elif date is not None and is_in_date_range(dt.date(2023, 2, 1), dt.date(2023, 10, 1), date) and project == 'eldorado' and source == 'yandex' and medium == 'cpc' and not re.search(r'flight', campaign.lower()) and re.search(r'dsa|_tk_|_smartbanners_|image|_autotarget_|yandex_shopping_segmented_', campaign.lower()):
        return 'non-MGCom'

    elif date is not None and date >= dt.date(2023, 10, 1) and project == 'eldorado' and source == 'yandex' and medium == 'cpc':
        return 'non-MGCom'

    ### CPA
    elif medium == 'cpa':
        return 'non-MGCom'

    ### Органик
    elif (re.search(r'yandex', source.lower()) and medium in ('organic', 'referral')) or (re.search(r'google', source.lower()) and medium == 'organic'):
        return 'non-MGCom'

    elif date is not None and date >= dt.date(2023, 10, 1) and project == 'eldorado' and source == 'Контекст':
        return 'non-MGCom'

    elif date is not None and is_in_date_range(dt.date(2023, 2, 1), dt.date(2023, 10, 1), date) and project == 'eldorado' and campaign in ('Яндекс Бренд', 'Яндекс DSA', 'Яндекс Смартбаннеры', 'Яндекс Товарная РК'):
        return 'non-MGCom'

    elif date is not None and date >= dt.date(2024, 1, 1) and project == 'mvideo' and source == 'Контекст':
        return 'non-MGCom'

    elif date is not None and is_in_date_range(dt.date(2023, 11, 1), dt.date(2023, 12, 31), date) and project == 'mvideo' and campaign in ('Яндекс Бренд (общий)', 'Яндекс Api (к50)', 'Яндекс РСЯ (CPC)', 'Яндекс Категорийные РК (модельные+катвенд) + Автотаргет'):
        return 'non-MGCom'

    elif date is not None and is_in_date_range(dt.date(2023, 2, 1), dt.date(2023, 11, 1), date) and project == 'mvideo' and campaign in ('Яндекс Бренд (общий)'):
        return 'non-MGCom'


    return 'MGCom'
