def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_goals_weborama(conversion_page):
    conversion_page = is_none(conversion_page)
    valid_pages = [
        'CIAN_All_site', 'CIAN_Watch_Phone_Number',
        'CIAN // Black Friday // Application form', 'CIAN // Black Friday // Users'
    ]

    if conversion_page in valid_pages:
        return conversion_page
    else:
        return 'NaN'