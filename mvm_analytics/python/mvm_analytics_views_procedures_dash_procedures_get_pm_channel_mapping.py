import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_pm_channel_mapping(date, data_group, channel, placement, placement_pf, total_paid, total_site, total_tops):
    channel = is_none(channel)
    placement = is_none(placement)
    placement_pf = is_none(placement_pf)
    total_paid = is_none(total_paid)
    total_site = is_none(total_site)
    total_tops = is_none(total_tops)

    if channel in ('контекст','соцсети','ретаргетинг','прайс-площадки','докаты','геосервисы','telegram') or re.search(r'докаты', channel):
        if data_group == 'channel':
            return channel
        elif data_group == 'placement':
            return placement
        elif data_group == 'placement_pf':
            return placement_pf
        elif data_group == 'total_paid':
            return channel
        else:
            return 'PAID'
    elif total_site in ('organic yandex','organic google'):
        if data_group == 'total_site':
            return total_site
        elif data_group == 'total_tops':
            return 'ORGANIC'
        else:
            return 'Other_data'
    elif total_site == 'organic other':
        if data_group == 'total_site':
            return 'OTHER'
        elif data_group == 'total_tops':
            return 'ORGANIC'
        else:
            return 'Other_data'
    elif total_site in ('CPA','DIRECT','EMAIL','PAID','GEO'):
        if data_group in ('total_tops','total_site'):
            return total_site
        else:
            return 'Other_data'
    else:
        if data_group in ('total_tops','total_site'):
            return 'OTHER'
        else:
            return 'Other_data'