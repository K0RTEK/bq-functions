import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def cont_vendor(campaign):
    vendors = {
        'lg': r'_lg_',
        'philips': r'philips',
        'samsung': r'samsung',
        'sony': r'sony',
        'apple': r'apple',
        'honor': r'honor',
        'huawei': r'huawei',
        'other': r'other',
        'realme': r'realme',
        'xiaomi': r'xiaomi',
        'acer': r'acer',
        'lenovo': r'lenovo',
        'artel': r'artel',
        'grundig': r'grundig',
        'haier': r'haier',
        'hec': r'_hec_',
        'hi': r'_hi_',
        'hisense': r'hisense',
        'novex': r'novex',
        'sber': r'sber',
        'sharp': r'sharp',
        'telefunken': r'telefunken',
        'toshiba': r'toshiba',
        'v-home': r'v-home',
        'vitjaz': r'vitjaz',
        'poco': r'poco',
        'tecno': r'tecno',
        'vivo': r'vivo',
    }
    for vendor, pattern in vendors.items():
        if re.search(pattern, is_none(campaign)):
            return vendor
    return 'NaN'