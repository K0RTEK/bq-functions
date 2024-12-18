import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def type_pf_md(campaign_name, ad_name, campaign_id):
    campaign_name = is_none(campaign_name)
    ad_name = is_none(ad_name)
    campaign_id = is_none(campaign_id)
    if re.search(r'^pf|_pf_|_pf$', campaign_name) or re.search(r'^pf|_pf_|_pf$', ad_name):
        return 'Перформ'
    elif re.search(r'^md|_md_|_md$|^report_|_report_|_report$', campaign_name) or re.search(r'^md|_md_|_md$|^report_|_report_|_report$', ad_name):
        return 'Медийка'
    return "Перформ"