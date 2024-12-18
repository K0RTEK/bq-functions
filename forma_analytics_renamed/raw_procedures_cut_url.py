import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def cut_url(url, part):
    url = is_none(url)
    part = is_none(part)
    clean_url = re.sub(r'($|&|=)', 'S', url.strip())
    clean_url = re.sub(r'utm_sourceSS|utm_mediumSS|utm_campaignSS|utm_contentSS|utm_termSS', '', clean_url)
    match = re.search(fr'{part}S(.+?)S', clean_url)
    return match.group(1) if match else 'None'