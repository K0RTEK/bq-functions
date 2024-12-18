def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_target_call_crm(crm_target_call, crm_source, utm_referrer, communication_id):
    crm_target_call = is_none(crm_target_call)
    crm_source = is_none(crm_source)
    utm_referrer = is_none(utm_referrer)
    communication_id = is_none(communication_id)
    if crm_target_call and (crm_source == "Реклама застройщика" or utm_referrer == 'https://indy-towers.ru') and (communication_id == "" or communication_id is None):
        return True
    elif crm_target_call and communication_id not in ("", None) and crm_source != "Самоход":
        return True
    return False
