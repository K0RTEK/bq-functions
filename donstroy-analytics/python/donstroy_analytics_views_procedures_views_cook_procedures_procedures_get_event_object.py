import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_campaign_object(date, parameters):
    parameters = [is_none(x) for x in parameters]
    if any(x in parameters for x in ['don-sobytie-mg', 'sobytie', 'sob']):
        return ' '
    elif any(x in parameters for x in ['don-simvol-mg', 'simvol', 'sim']):
        return ' '
    elif any(x in parameters for x in ['don-regiony', ' ']):
        return ' '
    elif any(x in parameters for x in ['don-kommercia-mg', ' ']):
        return ' '
    elif any(x in parameters for x in ['don-brand-mg', 'donstroy.com']):
        return 'donstroy.com'
    elif all(re.search(r'^sobytie|^sob', x) for x in parameters):
        return ' '
    elif all(re.search(r'^simvol|^sim', x) for x in parameters):
        return ' '
    elif all(re.search(r'^donstroy', x) for x in parameters):
        return 'donstroy.com | | '
    else:
        return None

def get_event_object(date, parameters):
    """
    cook_procedures.get_event_object(date, [param1,param2]) as event_object
    /*   Относится только к ОПРЕДЕЛЁННОМУ СОБЫТИЮ (соответствует напр. Объекту встречи или сделки)
        Источники уже ПОСЛЕ кабинета
        На случай коррекций - заложена дата (если можно обойтись без неё)
    */
    """

    parameters = [is_none(x) for x in parameters]
    if any(re.search(r'^событие', x) for x in parameters):
        return 'Событие'
    elif any(re.search(r'^символ', x) for x in parameters):
        return 'Символ'
    elif any(re.search(r'^региональн', x) for x in parameters):
        return 'РЕГИОНАЛЬНАЯ КАМПАНИЯ'
    elif any(re.search(r'^коммерческа', x) for x in parameters):
        return 'КОММЕРЧЕСКАЯ НЕДВИЖИМОСТЬ'
    elif any(re.search(r'^donstroy', x) for x in parameters):
        return 'donstroy.com'
    else:
        return get_campaign_object(date, parameters)