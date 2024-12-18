import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_cpa_cost_coeff(date, project, utm_source, utm_medium, utm_campaign, utm_content, utm_term):
    date = is_none(date)
    project = is_none(project)
    utm_source = is_none(utm_source)
    utm_medium = is_none(utm_medium)
    utm_campaign = is_none(utm_campaign)
    utm_content = is_none(utm_content)
    utm_term = is_none(utm_term)

    if project == 'mvideo':
        if re.search(r'advcake|tinkoff', utm_source) and utm_medium == 'cpa':
            if date < '2023-07-01':
                return 0.55*0.047/1.2
            else:
                return 0.04*0.7/1.2
        else:
            return 1
    elif project == 'eldorado':
        if re.search(r'advcake|tinkoff', utm_source) and utm_medium == 'cpa':
            if date < '2023-07-01':
                return 0.55*0.047/1.2
            else:
                return 0.04*0.65/1.2
        else:
            return 1
    else:
        return 1