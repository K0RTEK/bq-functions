import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_channel(source_medium):
    source_medium = is_none(source_medium)
    if re.search(r'mytarget', source_medium):
        return 'Соцсети'
    elif re.search(r'vk ', source_medium):
        return 'Соцсети'
    elif re.search(r'vkr', source_medium):
        return 'Соцсети'
    elif re.search(r'yandex / cpc', source_medium):
        return 'Контекст'
    elif re.search(r'google / cpc', source_medium):
        return 'Контекст'
    elif re.search(r'soloway', source_medium):
        return 'Ретаргетинг'
    else:
        return 'channel - NaN'

def type_camp(source_medium, campaign_name, ad_name, campaign_id):
    source_medium = is_none(source_medium)
    campaign_name = is_none(campaign_name)
    ad_name = is_none(ad_name)
    campaign_id = is_none(campaign_id)
    channel = get_channel(source_medium)
    if channel == "Контекст":
        if re.search(r'^br[ae]nd|_br[ae]nd_|_br[ae]nd$', campaign_name) or re.search(r'^br[ae]nd|_br[ae]nd_|_br[ae]nd$', ad_name):
            return 'Бренд'
        return 'Небренд'
    elif channel == "Соцсети":
        if re.search(r'^new|_new_|_new$', campaign_name) or re.search(r'^new|_new_|_new$', ad_name):
            return 'Новая'
        elif re.search(r'^rtg|_rtg_|_rtg$', campaign_name) or re.search(r'^rtg|_rtg_|_rtg$', ad_name):
            return 'Ретаргет'
        elif re.search(r'^hybrid|_hybrid_|_hybrid$', campaign_name) or re.search(r'^hybrid|_hybrid_|_hybrid$', ad_name):
            return 'Гибрид'
        return "type_camp - NaN"
    return "type_camp - NaN"