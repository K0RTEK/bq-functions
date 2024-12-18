import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_object(parameter):
    parameter = is_none(parameter)
    akvilon_analytics_variables_mg_var_project_signal = 'Signal'
    akvilon_analytics_variables_mg_var_project_beside = 'Beside'
    akvilon_analytics_variables_mg_var_project_indy = 'INDY Towers'
    object_mapping = {
        'akvilon-signal-mg': akvilon_analytics_variables_mg_var_project_signal,
        '64019': akvilon_analytics_variables_mg_var_project_signal,
        'Аквилон Signal': akvilon_analytics_variables_mg_var_project_signal,
        'akvilon-beside-mg': akvilon_analytics_variables_mg_var_project_beside,
        '42072': akvilon_analytics_variables_mg_var_project_beside,
        'beside': akvilon_analytics_variables_mg_var_project_beside,
        'Аквилон Beside 2.0': akvilon_analytics_variables_mg_var_project_beside,
        'akvilon-indy-mg': akvilon_analytics_variables_mg_var_project_indy,
        '52820': akvilon_analytics_variables_mg_var_project_indy,
        '60462': akvilon_analytics_variables_mg_var_project_indy,
        'INDY Towers': akvilon_analytics_variables_mg_var_project_indy,
        '5372874717': akvilon_analytics_variables_mg_var_project_indy
    }
    if parameter in object_mapping:
        return object_mapping[parameter]()

    elif re.search(r'(_|-|^)signal(_|-|$)', parameter):
        return akvilon_analytics_variables_mg_var_project_signal
    elif re.search(r'(_|-|^)indy(_|-|$)', parameter):
        return akvilon_analytics_variables_mg_var_project_indy
    elif re.search(r'(_|-| |^)(beside|бисайд|бесайд)(_|-| |$)', parameter):
        return akvilon_analytics_variables_mg_var_project_beside
    elif re.search(r'signal|сигнал', parameter):
        return akvilon_analytics_variables_mg_var_project_signal
    elif re.search(r'indy|инди', parameter):
        return akvilon_analytics_variables_mg_var_project_indy
    elif re.search(r'beside|бисайд|бесайд', parameter):
        return akvilon_analytics_variables_mg_var_project_beside

    return 'Неизвестный'