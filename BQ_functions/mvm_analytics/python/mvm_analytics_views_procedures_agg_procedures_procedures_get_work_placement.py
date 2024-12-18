import re
import datetime as dt


def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_work_placement(source_groupping, date, project, source, medium, campaign, content, term):
    source_groupping = is_none(source_groupping)
    date = is_none(date)
    project = is_none(project)
    source = is_none(source)
    medium = is_none(medium)
    campaign = is_none(campaign)
    content = is_none(content)
    term = is_none(term)

    # Helper function to check date ranges
    def is_in_date_range(start_date, end_date, date_to_check):
        return start_date <= date_to_check <= end_date

    # Parse the date string into a dt.date object
    try:
        date = dt.datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        date = None

    # Context
    if source in ('yandex', 'yandexdirect_int') and medium in ('cpc', 'af_web_banner', ''):
        if source_groupping == 'placement':
            return 'Яндекс Директ'
        else:
            return 'context'

    # Social
    if source == 'mt' and medium in ('cpc', 'cpm', 'af_web_banner', ''):
        if source_groupping == 'placement':
            return 'MyTarget'
        else:
            return 'social'

    if source in ('vk', 'vkontakte') and medium in ('cpc', 'cpm', 'af_web_banner', ''):
        if source_groupping == 'placement':
            return 'Vkontakte'
        else:
            return 'social'

    if source == 'vkr' and medium in ('cpc', 'cpm', 'af_web_banner', ''):
        if source_groupping == 'placement':
            return 'VK Reklama'
        else:
            return 'social'

    # RTG
    if (re.search(r'soloway', source.lower()) and medium == 'rs') or re.search(r'adriver.ru', source.lower()):
        if source_groupping == 'placement':
            return 'Soloway'
        else:
            return 'rtg'

    if (date is not None and (is_in_date_range(dt.date(2023, 4, 1), dt.date(2023, 8, 9), date) or date >= dt.date(2023, 8, 24))) and source == 'hybrid' and medium == 'cpc' and not re.search(r'flight', campaign.lower()):
        if source_groupping == 'placement':
            return 'Hybrid'
        else:
            return 'rtg'

    if date is not None and is_in_date_range(dt.date(2023, 8, 10), dt.date(2023, 8, 23), date) and source.lower() == 'hybrid' and medium == 'cpm' and re.search(r'mvideo|eldorado', campaign.lower()) and not re.search(r'flight', campaign.lower()):
        if source_groupping == 'placement':
            return 'Hybrid'
        else:
            return 'rtg'

    if source.lower() == 'turbotarget' and medium == 'cpc':
        if source_groupping == 'placement':
            return 'Turbotarget'
        else:
            return 'rtg'

    if source.lower() == 'mtsdspdynrem' and medium == 'cpm':
        if source_groupping == 'placement':
            return 'MTS'
        else:
            return 'rtg'

    if source.lower() == 'simb-ad' and medium == 'rs':
        if source_groupping == 'placement':
            return 'SimbAd'
        else:
            return 'rtg'

    if source.lower() == 'getintentdynrem' and medium == 'cpc':
        if source_groupping == 'placement':
            return 'Getintent'
        else:
            return 'rtg'

    # Prices
    if re.search(r'price', source.lower()) and medium == 'cpc':
        if source_groupping == 'placement':
            return 'PriceRu'
        else:
            return 'prices'

    if re.search(r'blizko', source.lower()) and medium == 'cpc':
        if source_groupping == 'placement':
            return 'Blizko'
        else:
            return 'prices'

    if re.search(r'pulscen', source.lower()) and medium == 'cpc':
        if source_groupping == 'placement':
            return 'Пульс Цен'
        else:
            return 'prices'

    if re.search(r'regmarket', source.lower()) and medium == 'cpc':
        if source_groupping == 'placement':
            return 'RegmarketsRu'
        else:
            return 'prices'

    # Geoservices
    if source.lower() == 'yandex_maps':
        if source_groupping == 'placement':
            return 'Яндекс Карты'
        else:
            return 'geoservices'

    if source.lower() == '2gis':
        if source_groupping == 'placement':
            return '2ГИС'
        else:
            return 'geoservices'

    # Telegram
    if source.lower() == 'telegram' and medium.lower() == 'cpc':
        if source_groupping == 'placement':
            return 'Telegram'
        else:
            return 'telegram'

    # CPA
    if re.search(r'advcake', source.lower()) and medium == 'cpa':
        if source_groupping == 'placement':
            return 'Adv.Cake'
        else:
            return 'cpa'

    if re.search(r'tinkoff', source.lower()) and medium == 'cpa':
        if source_groupping == 'placement':
            return 'Tinkoff'
        else:
            return 'cpa'

    # Default case
    if source_groupping == 'placement':
        return f'{source} / {medium}'
    else:
        return 'other'
