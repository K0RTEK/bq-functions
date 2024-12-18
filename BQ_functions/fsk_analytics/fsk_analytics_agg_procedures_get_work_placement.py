import re
import datetime as dt

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_work_placement(group_type, date, campaign_calltracking, channel_smartis, placement_smartis, utm_source, utm_medium, utm_campaign, form_name):
    utm_source = is_none(utm_source)
    utm_medium = is_none(utm_medium)
    utm_campaign = is_none(utm_campaign)
    campaign_calltracking = is_none(campaign_calltracking)
    form_name = is_none(form_name)
    group_type = is_none(group_type)
    channel_smartis = is_none(channel_smartis)
    placement_smartis = is_none(placement_smartis)

    if utm_source == 'google' and utm_medium == 'cpc':
        if group_type == 'channel':
            return 'Контекстная реклама'
        elif group_type == 'placement':
            return 'Google Ads'
    elif utm_source == 'yandex' and utm_medium == 'cpc':
        if group_type == 'channel':
            return 'Контекстная реклама'
        elif group_type == 'placement':
            return 'Яндекс Директ'
    elif re.search(r'facebook|fb_ig|inst|_fb$', utm_source) and utm_medium in ['cpc', 'cpm']:
        if group_type == 'channel':
            return 'Реклама в соц.сетях'
        elif group_type == 'placement':
            return 'Facebook'
    elif re.search(r'tiktok', utm_source) and utm_medium in ['cpc', 'cpm']:
        if group_type == 'channel':
            return 'Реклама в соц.сетях'
        elif group_type == 'placement':
            return 'Tik-tok'
    elif re.search(r'telegram', utm_source) and utm_medium in ['cpc', 'cpm']:
        if group_type == 'channel':
            return 'Реклама в соц.сетях'
        elif group_type == 'placement':
            return 'Telegram'
    elif re.search(r'mytarget|_mt$', utm_source) and utm_medium in ['cpc', 'cpm']:
        if group_type == 'channel':
            return 'Реклама в соц.сетях'
        elif group_type == 'placement':
            return 'MyTarget'
    elif re.search(r'vk_ads|vk_reklama|_vkr_', utm_source) and utm_medium in ['cpc', 'cpm']:
        if group_type == 'channel':
            return 'Реклама в соц.сетях'
        elif group_type == 'placement':
            return 'ВК Реклама'
    elif re.search(r'_vk$|^vk$|^vk_', utm_source) and utm_medium in ['cpc', 'cpm']:
        if group_type == 'channel':
            return 'Реклама в соц.сетях'
        elif group_type == 'placement':
            return 'Vkontakte'
    elif re.search(r'google', form_name) or re.search(r'google.*adwords|google.*ads|google.*бренд|ipro google$', campaign_calltracking) or (channel_smartis == 'Контекстная реклама' and re.search(r'google', placement_smartis)):
        if group_type == 'channel':
            return 'Контекстная реклама'
        elif group_type == 'placement':
            return 'Google Ads'
    elif re.search(r'yandex|яндекс|context', form_name) or re.search(r'яндекс', campaign_calltracking) or (channel_smartis == 'Контекстная реклама' and re.search(r'яндекс|yandex', placement_smartis)):
        if group_type == 'channel':
            return 'Контекстная реклама'
        elif group_type == 'placement':
            return 'Яндекс Директ'
    elif re.search(r' fb | fb$', form_name) or re.search(r'facebook| fb |insta|fb.inst', campaign_calltracking) or (channel_smartis == 'Реклама в соц.сетях' and re.search(r'facebook|instagram', placement_smartis)):
        if group_type == 'channel':
            return 'Реклама в соц.сетях'
        elif group_type == 'placement':
            return 'Facebook'
    elif re.search(r'tiktok|tik-tok', form_name) or re.search(r'tiktok|tik-tok', campaign_calltracking) or (channel_smartis == 'Реклама в соц.сетях' and re.search(r'tiktok|tik-tok', placement_smartis)):
        if group_type == 'channel':
            return 'Реклама в соц.сетях'
        elif group_type == 'placement':
            return 'Tik-tok'
    elif re.search(r'telegram', campaign_calltracking) and not re.search(r'nearby', campaign_calltracking) or (channel_smartis == 'Реклама в соц.сетях' and re.search(r'telegram', placement_smartis)):
        if group_type == 'channel':
            return 'Реклама в соц.сетях'
        elif group_type == 'placement':
            return 'Telegram'
    elif re.search(r'tenchat', form_name) or re.search(r'tenchat', campaign_calltracking) or (channel_smartis == 'Реклама в соц.сетях' and re.search(r'tenchat', placement_smartis)):
        if group_type == 'channel':
            return 'Реклама в соц.сетях'
        elif group_type == 'placement':
            return 'TenChat'
    elif re.search(r' mt$| mt |fb.*mt| мт$| мт ', form_name) or re.search(r'mt|mytarget|target.mail| mail ', campaign_calltracking) or (channel_smartis == 'Реклама в соц.сетях' and re.search(r'mytarget', placement_smartis)):
        if group_type == 'channel':
            return 'Реклама в соц.сетях'
        elif group_type == 'placement':
            return 'MyTarget'
    elif re.search(r'vkr', form_name) or re.search(r'vk reklama|vk ads|vkads', campaign_calltracking) or (channel_smartis == 'Реклама в соц.сетях' and re.search(r'vk.com', placement_smartis) and date >= dt.date(2023, 5, 1)):
        if group_type == 'channel':
            return 'Реклама в соц.сетях'
        elif group_type == 'placement':
            return 'ВК Реклама'
    elif re.search(r'	vk | vk$| vk | вк | вк$|fb.*vk|вконтакте', form_name) or re.search(r' vk | vk$|vkontakte|вконтакте| вк ', campaign_calltracking) or (channel_smartis == 'Реклама в соц.сетях' and re.search(r'vk.com|юла', placement_smartis)):
        if group_type == 'channel':
            return 'Реклама в соц.сетях'
        elif group_type == 'placement':
            return 'Vkontakte'
    elif form_name in ['FSK BR', 'FSK BR BUS New', 'FSK BR BUSINESS', 'FSK BR OLV', 'FSK LAND черновик', 'FSK NSTR', 'FSK REZH', 'FSK REZH Черновик', 'FSK RIH', 'FSK RIM', 'FSK SKOL', 'FSK BR'] or re.search(r'social network|соц. сети|соцсети|leadads|redirect|lead-ads|quiz|трафик', campaign_calltracking):
        if group_type == 'channel':
            return 'Реклама в соц.сетях'
        elif group_type == 'placement':
            return 'Facebook'
    elif re.search(r'cpa|cpа|сра', campaign_calltracking) or (channel_smartis == 'Лидогенерация'):
        if group_type == 'channel':
            return 'Лидогенерация'
        elif group_type == 'placement':
            return placement_smartis
    elif re.search(r'programmatic|программатик|prm', campaign_calltracking) or (channel_smartis == 'Программатик'):
        if group_type == 'channel':
            return 'Программатик'
        elif group_type == 'placement':
            return placement_smartis
    return None