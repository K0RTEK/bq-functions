import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def cut_url(url, part):
    url = is_none(url)
    part = is_none(part)

    url = re.sub(r'($|&|=)', 'S', url.strip())
    url = re.sub(r'utm_sourceSS|utm_mediumSS|utm_campaignSS|utm_contentSS|utm_termSS', '', url)
    match = re.search(rf'{part}S(.+?)S', url)
    return match.group(1) if match else 'None'