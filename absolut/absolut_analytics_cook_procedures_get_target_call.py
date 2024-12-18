import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_target_call(call_tags, object_type):
    call_tags = is_none(call_tags)
    object_type = is_none(object_type)
    if re.search(r'целевой', call_tags, re.IGNORECASE) and not re.search(r'нецелевой', call_tags, re.IGNORECASE):
        if object_type == 'Жилая недвижимость':
            return True
        if re.search(r'коммер', call_tags, re.IGNORECASE) and object_type == 'Коммерческая недвижимость':
            return True
    return False
