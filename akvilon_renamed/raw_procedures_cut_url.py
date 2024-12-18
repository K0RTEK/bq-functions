import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def cut_url(url, part):
    url = is_none(url)
    part = is_none(part)
    # Преобразует URL и извлекает нужную часть, используя регулярные выражения
    if url:
        url_lower_trimmed = url.lower().strip()
        url_cleaned = re.sub(r'($|&|=)', 'S', url_lower_trimmed)
        url_cleaned = re.sub(r'utm_sourceSS|utm_mediumSS|utm_campaignSS|utm_contentSS|utm_termSS', '', url_cleaned)
        match = re.search(f"{part}S(.+?)S", url_cleaned)
        return match.group(1) if match else "None"
    return "None"