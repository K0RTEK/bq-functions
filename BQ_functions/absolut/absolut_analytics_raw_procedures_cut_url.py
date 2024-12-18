import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def cut_url(url, part):
    url = is_none(url)
    part = is_none(part)
    if url:
        cleaned_url = re.sub(r'($|&|=)', 'S', url.strip())
        cleaned_url = re.sub(r'utm_sourceSS|utm_mediumSS|utm_campaignSS|utm_contentSS|utm_termSS', '', cleaned_url)
        match = re.search(rf'{part}S(.+?)S', cleaned_url)
        if match:
            return match.group(1)
    return "None"
