import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_agency(date: str, campaign_calltracking: str, utm_source: str, utm_medium: str, utm_campaign: str, campaign_name: str, ad_group_name: str, form_name: str, object_name: str) -> str:
    campaign_name = is_none(campaign_name)
    ad_group_name = is_none(ad_group_name)
    form_name = is_none(form_name)
    object_name = is_none(object_name)
    campaign_calltracking = is_none(campaign_calltracking)
    utm_source = is_none(utm_source)
    utm_medium = is_none(utm_medium)
    utm_campaign = is_none(utm_campaign)

    # Условие для 'MGCom'
    if (not re.search(r'^rw|^ipro|form_name|^artsofte', form_name)) or \
       campaign_calltracking.startswith('mg') or \
       (campaign_calltracking in ['sydney', 'skygarden', 'rimskiy', 'rihard', 'rezhiser', 'nastroenie'] and object_name == 'программатик') or \
       utm_source.startswith('mg') or \
       utm_campaign.startswith('mg') or \
       campaign_name.startswith('mg') or \
       ad_group_name.startswith('mg'):
        return 'MGCom'

    # Условие для других 'MGCom' по object
    if re.search(r'измайловск|воскресенск|дружб|жаворонки|калуга (17|18|19|31|32)|тайфун|молод(е|ё)жный|настроение|олимп|поколение|апрель|режиссер|римский|рихард|сабурово|сидней|sydney|прайм|prime|скай.*гарден|garden|одинцово|сколковский|lake|лейк|лэйк|химкинс', object):
        return 'MGCom'

    # Если ни одно из условий не выполнено, возвращаем 'Не MGCom'
    return 'Не MGCom'
