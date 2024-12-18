import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_goals(platform, source_medium, event_category, event_label, event_action,
                                 cplcalltracking_id84):
    platform_lower = is_none(platform)
    source_medium_lower = is_none(source_medium)
    event_category_lower = is_none(event_category)
    event_label_lower = is_none(event_label)
    event_action_lower = is_none(event_action)


    if platform_lower == 'web':
        if re.search(r'new_ad', event_category_lower) and event_action == 'success':
            return 'Подачи'
        elif re.search(r'send_message', event_action_lower) and event_category_lower == 'message_popup':
            return 'Чаты'
        elif re.search(r'open', event_action_lower) and re.search(r'/(sale|rent)/commercial/|/bc/|/tc/',
                                                                  event_label_lower) and event_category_lower == 'phones':
            return 'Расхлоп КН'
        elif event_action == 'dynamic_call' and event_label == 'target' and event_category_lower == 'cian_newbuilding_call':
            return 'Целевой звонок'
        elif re.search(r'open', event_action_lower) and re.search(r'sale/jk/|/sale/flat/.*object_type=2',
                                                                  event_label_lower) and event_category_lower == 'phones' and cplcalltracking_id84 == '1':
            return 'Расхлоп CPL'
        elif event_action == 'click_button_auth' and event_category_lower == 'promo':
            return 'ИАП (вход)'
        elif event_action == 'Send_form' and event_label_lower == 'success' and event_category_lower == 'promo':
            return 'ИАП (промо)'
        elif event_action == 'click_sopr' and event_label_lower == 'kpn_chat' and event_category_lower == 'newbuilding_finder':
            return 'Начать чат'
        elif event_action == 'callback' and event_label_lower == 'success' and event_category_lower == 'newbuilding_finder':
            return 'Заявки на обратный звонок'
        elif event_action == 'add_collection' and event_category_lower == 'listingfavorites' and re.search(
                r'social_cpc', source_medium_lower):
            return 'Подборки'
        elif event_action == 'click_sopr' and event_label_lower == 'callback' and event_category_lower == 'newbuilding_finder' and re.search(
                r'social_cpc', source_medium_lower):
            return 'ЧП (тизер)'
        else:
            return 'NaN'

    elif platform_lower == 'app':
        if re.search(r'mytarget / mytarget|social_cpc|vk / vk', source_medium_lower) and re.search(r'open',
                                                                                                   event_action_lower) and event_category_lower == 'phones':
            return 'Расхлоп APP'
        elif event_category_lower == 'chat' and event_action == 'ChatSendMessage':
            return 'Чаты APP'
        else:
            return 'NaN'

    return 'NaN'