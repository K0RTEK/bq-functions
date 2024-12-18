import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def cont_mg_or_non_mg(campaign, project_name):
    campaign = is_none(campaign)
    project_name = is_none(project_name)
    if project_name == 'eldorado' and re.search(r'dsa|_tk_|_smartbanners_|image|_autotarget_|yandex_shopping_segmented_', campaign) and not re.search(r'flight', campaign):
        return 'non-MGCom'
    elif project_name == 'mvideo' and re.search(r'image', campaign) and not re.search(r'flight', campaign):
        return 'non-MGCom'
    else:
        return 'MGCom'