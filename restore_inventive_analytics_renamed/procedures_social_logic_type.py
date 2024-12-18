import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def logic_type(campaign):
    campaign = is_none(campaign)
    if re.search(r'kw_', campaign):
        return 'ключи'
    elif re.search(r'int_|int-', campaign):
        return 'интересы'
    elif re.search(r'auto', campaign):
        return 'автоинтересы'
    elif re.search(r'dnmc_', campaign):
        return 'динрем'
    elif re.search(r'sttc_|stts_', campaign):
        return 'стат.ремаркетинг'
    elif re.search(r'lal_', campaign):
        return 'похожая аудитория'
    else:
        return 'NaN'
