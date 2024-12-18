import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_call_duration(call_duration):
    call_duration = is_none(call_duration)
    if len(call_duration) > 8 or int(re.search(r'..:..:(.*)', call_duration).group(1)) >= 60:
        minutes = int(int(re.search(r'..:..:(.*)', call_duration).group(1)) / 60)
        seconds = int((int(re.search(r'..:..:(.*)', call_duration).group(1)) % 60))
        return f"0:{minutes:02}:{seconds:02}"
    else:
        return call_duration