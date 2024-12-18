import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_call_duration(call_duration):
    call_duration = is_none(call_duration)
    match = re.search(r'..:..:(.*)', call_duration)
    if match and len(call_duration) > 8 or int(match.group(1)) >= 60:
        minutes = str(int(match.group(1)) // 60).zfill(2)
        seconds = str(int(match.group(1)) % 60).zfill(2)
        return f"00:{minutes}:{seconds}"
    return call_duration