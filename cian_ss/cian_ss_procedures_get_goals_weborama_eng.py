def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_goals_weborama_eng(conversion_page):
    conversion_page = is_none(conversion_page)
    if conversion_page == 'CIAN_All_site':
        return 'cian_all_site'
    elif conversion_page == 'CIAN_Watch_Phone_Number':
        return 'cian_watch_phone_number'
    elif conversion_page == 'CIAN // Black Friday // Application form':
        return 'cian_bf_application_form'
    elif conversion_page == 'CIAN // Black Friday // Users':
        return 'cian_bf_users'
    else:
        return 'NaN'