import re
import datetime as dt

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def cut_url(url, part):
    url = is_none(url).strip()

    url_transformed = re.sub(r'(&|=|$)', 'S', url)

    url_cleaned = re.sub(r'utm_sourceSS|utm_mediumSS|utm_campaignSS|utm_contentSS|utm_termSS', '', url_transformed)

    pattern = rf'{part}S(.+?)S'
    match = re.search(pattern, url_cleaned)

    return match.group(1) if match else "None"