import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()


def utm_decode(date, parameter, utm_source, utm_medium, utm_campaign, utm_content, utm_term):
    parameter = is_none(parameter)
    utm_source = is_none(utm_source)
    utm_medium = is_none(utm_medium)
    utm_campaign = is_none(utm_campaign)
    utm_content = is_none(utm_content)
    utm_term = is_none(utm_term)

    return re.search(
        r'S' + parameter + r'S*(.+?)S',
        r'SNonaInfoS*(.+?)S' + utm_source + r'S*(.+?)S' + utm_medium + r'S*(.+?)S' +
        utm_campaign + r'S*(.+?)S' + utm_content + r'S*(.+?)S' + utm_term + r'S*(.+?)S'
    ).group(1)