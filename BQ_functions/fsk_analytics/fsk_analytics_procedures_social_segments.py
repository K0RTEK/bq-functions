import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def social_segments(ad_name: str) -> str:
    ad_name = is_none(ad_name)

    if re.search(r'mktr|maketrue', ad_name):
        return 'Maketrue'
    elif re.search(r'amdt', ad_name):
        return 'Amberdata'
    elif re.search(r'konnektu|tec-', ad_name):
        return 'CDP'
    elif re.search(r'lal|vco-special', ad_name):
        return 'LAL'
    elif re.search(r'ret|open-lead-cpc|positive', ad_name):
        return 'Retargeting'
    elif re.search(r'dmp|gorod-nedvizh', ad_name):
        return 'DMP'
    elif re.search(r'keys', ad_name):
        return 'Keys'
    elif re.search(r'dinrem|prospe.ting', ad_name):
        return 'Dinrem'
    elif re.search(r'regions', ad_name):
        return 'Regions'
    elif re.search(r'groups', ad_name):
        return 'Group'
    elif re.search(
            r'apple|a(u|v)to|business|remont|dosug|employer|family|finance|geotag|income|interest|invest|ipoteka|job|leisure|naruzh|new-buil|newbuil|owner|parents|professions|realty|repair|socdem|supergeo|travel|villa|vklady|sport|highinc|interior|bus-edu|gorodskaya-nedv|luxury|inftec|beauty',
            ad_name):
        return 'Interests'
    elif ad_name == 'NaN':
        return 'Не опознается'
    else:
        return 'NaN'
