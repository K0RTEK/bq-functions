import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_ad_id(date, channel, placement, utm_source, utm_medium, utm_campaign, utm_content, utm_term):
    utm_content_lower = is_none(utm_content)
    utm_campaign_lower = is_none(utm_campaign)
    utm_term = is_none(utm_term)
    utm_source = is_none(utm_source)
    utm_medium = is_none(utm_medium)
    channel = is_none(channel)
    placement = is_none(placement)

    # utm_campaign_lower = utm_campaign.lower()
    if channel == 'Контекстная реклама' and placement == 'Яндекс Директ':
        if 'adid:' in utm_content_lower:
            return re.search(r'adid:([0-9]+)', utm_content_lower).group(1)
        if 'gid|' in utm_content_lower:
            return re.search(r'gid\|([0-9]+)', utm_content_lower).group(1)
        if 'b:' in utm_content_lower:
            return re.search(r'b:([0-9]+)', utm_content_lower).group(1)
        if 'aid|' in utm_content_lower:
            return re.search(r'aid\|([0-9]+)', utm_content_lower).group(1)
    elif channel == 'Реклама в соц.сетях':
        if placement == 'Facebook':
            if 'adid:' in utm_content_lower:
                return re.search(r'adid:([0-9]+)', utm_content_lower).group(1)
            elif re.search(r'([0-9]{5,})', utm_content_lower) and not 'adid:' in utm_content_lower:
                return re.search(r'([0-9]{5,})', utm_content_lower).group(1)
            elif re.search(r'([0-9]{5,})', utm_campaign_lower) and not utm_content:
                return re.search(r'([0-9]{5,})', utm_campaign_lower).group(1)
        elif placement == 'MyTarget':
            if 'adid:' in utm_content_lower:
                return re.search(r'adid:([0-9]+)', utm_content_lower).group(1)
            elif re.search(r'([0-9]{5,})', utm_content_lower) and not 'adid:' in utm_content_lower:
                return re.search(r'([0-9]{5,})', utm_content_lower).group(1)
            elif re.search(r'([0-9]{5,})', utm_campaign_lower) and not utm_content:
                return re.search(r'([0-9]{5,})', utm_campaign_lower).group(1)
        elif placement == 'Vkontakte':
            if 'adid:' in utm_content_lower:
                return re.search(r'adid:([0-9]+)', utm_content_lower).group(1)
            elif re.search(r'([0-9]{5,})', utm_content_lower) and not 'adid:' in utm_content_lower:
                return re.search(r'([0-9]{5,})', utm_content_lower).group(1)
            elif re.search(r'([0-9]{5,})', utm_campaign_lower) and not utm_content:
                return re.search(r'([0-9]{5,})', utm_campaign_lower).group(1)
    elif utm_source in ['vk_ads', 'vk_reklama'] and utm_medium in ['cpc', 'cpm']:
        if 'adid:' in utm_content_lower:
            return re.search(r'adid:([0-9]+)', utm_content_lower).group(1)
        elif re.search(r'([0-9]{5,})', utm_content_lower) and not 'adid:' in utm_content_lower:
            return re.search(r'([0-9]{5,})', utm_content_lower).group(1)
    return None