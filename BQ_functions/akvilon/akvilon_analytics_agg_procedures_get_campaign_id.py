import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_channel(date, utm_source, utm_medium, utm_campaign, utm_content, utm_term, ct_campaign_name):
    utm_source = is_none(utm_source)
    utm_medium = is_none(utm_medium)
    utm_campaign = is_none(utm_campaign)
    utm_content = is_none(utm_content)
    utm_term = is_none(utm_term)
    ct_campaign_name = is_none(ct_campaign_name)
    if (utm_source == 'yandex' and utm_medium == 'cpc') or re.search(r'контекстная реклама', ct_campaign_name.strip()):
        return "Контекстная реклама"
    elif re.search(r'не указано|не заполнено', utm_source.strip()) and re.search(r'не указано|не заполнено', utm_medium.strip()):
        return "Органика"
    elif re.search(r'офлайн|оффлайн|offline|ofline', utm_medium.strip()):
        return "Органика"
    return "Неизвестный"

def get_campaign_id(date, utm_source, utm_medium, utm_campaign, utm_content, utm_term, ct_campaign_name):
    if get_channel(date, utm_source, utm_medium, utm_campaign, utm_content, utm_term, ct_campaign_name) == "Контекстная реклама":
        return re.search(r'cid:([0-9]+)', utm_content).group(1) if re.search(r'cid:([0-9]+)', utm_content) else None
    return None
