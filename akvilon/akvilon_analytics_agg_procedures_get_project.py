import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_project(date, utm_source, utm_medium, utm_campaign, utm_content, utm_term, ct_campaign_name):
    utm_source = is_none(utm_source)
    utm_medium = is_none(utm_medium)
    utm_campaign = is_none(utm_campaign)
    utm_content = is_none(utm_content)
    utm_term = is_none(utm_term)
    ct_campaign_name = is_none(ct_campaign_name)
    akvilon_analytics_variables_mg_var_project_signal = 'Signal'
    akvilon_analytics_variables_mg_var_project_beside = 'Beside'
    akvilon_analytics_variables_mg_var_project_indy = 'INDY Towers'
    if ct_campaign_name == '52820':
        if re.search(r'mg_', utm_term) and re.search(r'mg_[аa]квилон [cс]игнал', utm_term):
            return akvilon_analytics_variables_mg_var_project_signal
        elif re.search(r'mg_', utm_term) and re.search(r'mg_бисайд', utm_term):
            return akvilon_analytics_variables_mg_var_project_beside
        elif re.search(r'mg_', utm_term):
            return akvilon_analytics_variables_mg_var_project_indy
        return "Другие проекты"
    elif ct_campaign_name in ['akvilon-signal-mg', '64019', 'Аквилон Signal', '95741242', '745']:
        return akvilon_analytics_variables_mg_var_project_signal
    elif ct_campaign_name in ['akvilon-indy-mg', '60462', 'INDY Towers', '5372874717', 'indy', 'indy-olv', 'akv-indy-olv', '94044884', '724']:
        return akvilon_analytics_variables_mg_var_project_indy
    elif ct_campaign_name in ['akvilon-beside-mg', '42072', 'beside', 'Аквилон Beside 2.0', '71105419']:
        return akvilon_analytics_variables_mg_var_project_beside
    elif re.search(r'signal|сигнал', ct_campaign_name):
        return akvilon_analytics_variables_mg_var_project_signal
    elif re.search(r'indy|инди', ct_campaign_name):
        return akvilon_analytics_variables_mg_var_project_indy
    elif re.search(r'beside|бисайд|бесайд', ct_campaign_name) and not re.search(r'^аквилон beside$', ct_campaign_name):
        return akvilon_analytics_variables_mg_var_project_beside
    elif re.search(r'signal|сигнал', utm_campaign):
        return akvilon_analytics_variables_mg_var_project_signal
    elif re.search(r'indy|инди', utm_campaign):
        return akvilon_analytics_variables_mg_var_project_indy
    elif re.search(r'beside|бисайд|бесайд', utm_campaign) and not re.search(r'^аквилон beside$', ct_campaign_name):
        return akvilon_analytics_variables_mg_var_project_beside
    return "Другие проекты"
