import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_ad_group_id(date, source, medium, campaign, content, term):
    date = is_none(date)
    source = is_none(source)
    medium = is_none(medium)
    campaign = is_none(campaign)
    content = is_none(content)
    term = is_none(term)
    if campaign.startswith('mg_ya_') and source == 'yandex' and medium == 'cpc':
        content_lower = content.lower()
        if 'gid:' in content_lower:
            return re.search(r'gid:([0-9]+)', content_lower).group(1)
        elif 'gid|' in content_lower:
            return re.search(r'gid\|([0-9]+)', content_lower).group(1)
        elif 'gr:' in content_lower:
            return re.search(r'gr:([0-9]+)', content_lower).group(1)
        elif '|g:' in content_lower:
            return re.search(r'\|g:([0-9]+)', content_lower).group(1)
    elif source in ['vk_ads', 'vk_reklama'] and medium in ['cpc', 'cpm']:
        campaign_lower = campaign.lower()
        content_lower = content.lower()
        if re.search(r'^[0-9]+$', campaign_lower):
            return campaign_lower
        if re.search(r'cid.[0-9]+', campaign_lower):
            return re.search(r'cid.([0-9]+)', campaign_lower).group(1)
        if re.search(r'cid.[0-9]+', content_lower):
            return re.search(r'cid.([0-9]+)', content_lower).group(1)
    return None