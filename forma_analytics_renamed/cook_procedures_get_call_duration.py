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
        minutes_str = f'0{minutes}' if len(str(minutes)) < 2 else str(minutes)
        seconds = round(float('0.' + re.search(r'\.(.*)', str(round(int(re.search(r'..:..:(.*)', call_duration).group(1)) / 60, 2))).split('.')[-1]) * 60)
        seconds_str = f'0{seconds}' if len(str(seconds)) < 2 else str(seconds)
        return f'00:{minutes_str}:{seconds_str}'
    return call_duration