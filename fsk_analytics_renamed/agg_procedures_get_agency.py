import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_agency(date, campaign_calltracking, utm_source, utm_medium, utm_campaign, campaign_name, ad_group_name, form_name, object_name):
    form_name_lower = is_none(form_name)
    utm_source = is_none(utm_source)
    utm_medium = is_none(utm_medium)
    utm_campaign = is_none(utm_campaign)
    campaign_name = is_none(campaign_name)
    ad_group_name = is_none(ad_group_name)
    object_name = is_none(object_name)

    if not re.search(r'^rw|^ipro|form_name|^artsofte', form_name_lower) or \
        'mg%' in campaign_calltracking or \
        'mg%' in utm_source or \
        'mg%' in utm_campaign or \
        'mg%' in campaign_name or \
        'mg%' in ad_group_name:
        return 'MGCom'
    elif re.search(r'воскресенск|дружб|жаворонки|калуга (17|18|19|31|32)|тайфун|молод(е|ё)жный|настроение|олимп|поколение|апрель|режиссер|римский|рихард|сабурово|сидней|прайм|prime|скай.*гарден|одинцово|сколковский|lake|лейк|лэйк', object_name):
        return 'MGCom'
    else:
        return 'Не MGCom'