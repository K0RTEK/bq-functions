import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def segments(campaign):
    campaign = is_none(campaign)
    if re.search(r'autotargeting', campaign) and not re.search(r'compet|brend', campaign):
        return 'Автотаргетинг'
    elif re.search(r'invest', campaign):
      return 'Инвестиции'
    elif re.search(r'audience|intent|interest', campaign) and not re.search(r'prilozheniya|tec|alfabank|olv|lal|ipoteka|brend', campaign):
      return 'Интересы'
    elif re.search(r'ipoteka', campaign) and not re.search(r'remarketing|retargeting', campaign):
      return 'Ипотека'
    elif re.search(r'1kom|2kom|3kom', campaign):
      return 'Комнатность'
    elif re.search(r'compet', campaign) and not re.search(r'ipoteka|rassrochka', campaign):
      return 'Конкуренты'
    elif re.search(r'mobapp', campaign):
      return 'Приложение'
    elif re.search(r'rassrochka', campaign):
      return 'Рассрочка'
    elif re.search(r'remarketing|retargeting|olv|alfabank|posetiteli', campaign):
      return 'Ретаргетинг'
    elif re.search(r'smart', campaign) and not re.search(r'autotargeting|company', campaign):
      return 'Смарт-баннеры'
    elif re.search(r'brand|контекст бренд', campaign) and re.search(r'mg_ya_|mg \| контекст', campaign) and not re.search(r'_net_', campaign):
      return 'Brand'
    elif re.search(r'tec|aidata|konnektu', campaign) and not re.search(r'compet|dokhod', campaign):
      return 'CDP'
    elif re.search(r'discovery', campaign) and not re.search(r'tec|compet|intent', campaign):
      return 'Discovery'
    elif re.search(r'dsa', campaign):
      return 'DSA'
    elif re.search(r'generic', campaign) and not re.search(r'invest|intent|ipoteca|1com|2com|3com|compet|discovery|rassrochka|brend|tec|geo|rlsa', campaign):
      return 'Generic'
    elif re.search(r'geo', campaign) and not re.search(r'brend', campaign):
      return 'Geo'
    elif re.search(r'lal', campaign) and not re.search(r'tec|discovery|rlsa', campaign):
      return 'LAL'
    elif re.search(r'rlsa', campaign) and not re.search(r'tec', campaign):
        return 'RLSA'
    return 'Остальное'