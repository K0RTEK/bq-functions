import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_goals_eng(platform, source_medium, event_category, event_label, event_action, cplcalltracking_id84):
    platform_lower = is_none(platform.strip())
    source_medium_lower = is_none(source_medium.strip())
    event_category_lower = is_none(event_category.strip())
    event_label_lower = is_none(event_label.strip())
    event_action_lower = is_none(event_action.strip())

    # Если платформа 'web'
    if platform_lower == 'web':
        if re.search(r'new_ad', event_category_lower) and event_action_lower == 'success':
            return 'passes'
        elif re.search(r'send_message', event_action_lower) and event_category_lower == 'message_popup':
            return 'chats'
        elif re.search(r'open', event_action_lower) and re.search(r'/(sale|rent)/commercial/|/bc/|/tc/', event_label_lower) and event_category_lower == 'phones':
            return 'collapse_kn'
        elif event_action_lower == 'dynamic_call' and event_label_lower == 'target' and event_category_lower == 'cian_newbuilding_call':
            return 'target_call'
        elif re.search(r'open', event_action_lower) and re.search(r'sale/jk/|/sale/flat/.*object_type=2', event_label_lower) and event_category_lower == 'phones' and cplcalltracking_id84 == '1':
            return 'collapse_cpl'
        elif event_action_lower == 'click_button_auth' and event_category_lower == 'promo':
            return 'iap_enter'
        elif event_action_lower == 'send_form' and event_label_lower == 'success' and event_category_lower == 'promo':
            return 'iap_promo'
        elif event_action_lower == 'click_sopr' and event_label_lower == 'kpn_chat' and event_category_lower == 'newbuilding_finder':
            return 'start_chat'
        elif event_action_lower == 'callback' and event_label_lower == 'success' and event_category_lower == 'newbuilding_finder':
            return 'callback'
        elif event_action_lower == 'add_collection' and event_category_lower == 'listingfavorites' and re.search(r'social_cpc', source_medium_lower):
            return 'selections'
        elif event_action_lower == 'click_sopr' and event_label_lower == 'callback' and event_category_lower == 'newbuilding_finder' and re.search(r'social_cpc', source_medium_lower):
            return 'bf_teaser'
        else:
            return 'NaN'

    # Если платформа 'app'
    elif platform_lower == 'app':
        if re.search(r'mytarget / mytarget|social_cpc|vk / vk', source_medium_lower) and re.search(r'open', event_action_lower) and event_category_lower == 'phones':
            return 'collapse_app'
        elif event_category_lower == 'chat' and event_action_lower == 'chatsendmessage':
            return 'chats_app'
        elif re.search(r'open', event_action_lower) and re.search(r'commercial', event_label_lower) and event_category_lower == 'phones':
            return 'collapse_kn_app'
        elif event_action_lower == 'phonesopen' and event_label_lower == 'fromdevcpl' and event_category_lower == 'marketingteam':
            return 'cpl_app'
        else:
            return 'NaN'

    return 'NaN'
