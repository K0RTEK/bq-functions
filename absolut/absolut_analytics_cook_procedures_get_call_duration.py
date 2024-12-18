import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_call_duration(call_duration):
    call_duration = is_none(call_duration)
    match = re.search(r'..:..:(\d+)', call_duration)
    if match:
        seconds = int(match.group(1))
        if len(call_duration) > 8 or seconds >= 60:
            minutes = seconds // 60
            seconds = seconds % 60
            formatted_time = f"0:{minutes:02d}:{seconds:02d}"
            return formatted_time
    return call_duration
