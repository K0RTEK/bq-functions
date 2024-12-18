import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_placement_price(campaign_name):
    campaign_name = is_none(campaign_name)

    if re.search(r'базы.*cian.*xml|базы.*циан.*xml', campaign_name):
        return 'Циан'
    elif re.search(r'базы.*yandex.*xml|базы.*яндекс.*xml', campaign_name):
        return 'Яндекс.Недвижимость'
    elif re.search(r'базы.*avito.*xml|базы.*авито.*xml', campaign_name):
        return 'Авито'
    elif re.search(r'базы.*cat.*xml', campaign_name):
        return 'JCat'
    else:
        return f'NaN - {campaign_name}'