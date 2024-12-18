import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_campaign_id(date, channel, placement, utm_source, utm_medium, utm_campaign, utm_content, utm_term):
    utm_content_lower = is_none(utm_content)
    utm_campaign_lower = is_none(utm_campaign)
    utm_term = is_none(utm_term)
    utm_source = is_none(utm_source)
    utm_medium = is_none(utm_medium)
    channel = is_none(channel)
    placement = is_none(placement)

    if channel == 'Контекстная реклама' and placement == 'Яндекс Директ':
        if 'cid:' in utm_content_lower:
            return re.search(r'cid:([0-9]+)', utm_content_lower).group(1)
        elif 'cid|' in utm_content_lower:
            return re.search(r'cid\|([0-9]+)', utm_content_lower).group(1)
        elif '|c:' in utm_content_lower:
            return re.search(r'\|c:([0-9]+)', utm_content_lower).group(1)
        elif re.search(r'кампания.*мкб или смарт-кампания', utm_campaign_lower):
            return re.search(r'[0-9]+', utm_campaign_lower).group(0)
    elif channel == 'Реклама в соц.сетях':
        if placement == 'Facebook':
            if 'cid:' in utm_content_lower:
                return re.search(r'cid:([0-9]+)', utm_content_lower).group(1)
            elif 'cid|' in utm_content_lower:
                return re.search(r'cid\|([0-9]+)', utm_content_lower).group(1)
            elif '|c:' in utm_content_lower:
                return re.search(r'\|c:([0-9]+)', utm_content_lower).group(1)
        elif placement == 'MyTarget':
            if 'cid:' in utm_content_lower:
                return re.search(r'cid:([0-9]+)', utm_content_lower).group(1)
            elif re.search(r'cid:', utm_campaign_lower):
                return re.search(r'cid:([0-9]{5,})', utm_campaign_lower).group(1)
        elif placement == 'Vkontakte':
            if 'cid:' in utm_content_lower:
                return re.search(r'cid:([0-9]+)', utm_content_lower).group(1)
            elif re.search(r'cid:', utm_campaign_lower):
                return re.search(r'cid:([0-9]{5,})', utm_campaign_lower).group(1)
    return None