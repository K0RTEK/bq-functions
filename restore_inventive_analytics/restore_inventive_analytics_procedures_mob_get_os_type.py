import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_os_type(campaign):
    campaign = is_none(campaign)
    if re.search(r'restore_android_ios_yandex_29.09', campaign):
        return 'Android'
    elif re.search(r'_ios|-ios| ios', campaign):
        return 'IOS'
    elif re.search(r'_aos|-aos| aos', campaign):
        return 'Android'
    elif re.search(r'vm_s5_1|ad_1|er_kk|vm_s28_1|er_mk', campaign):
        return 'Android'
    elif re.search(r'er_hm|er_mn', campaign):
        return 'IOS'
    elif re.search(r'ios', campaign):
        return 'IOS'
    elif re.search(r'android', campaign):
        return 'Android'
    else:
        return 'Прочее'
