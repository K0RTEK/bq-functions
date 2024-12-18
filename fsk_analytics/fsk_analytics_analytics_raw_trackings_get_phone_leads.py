import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def fsk_analytics_analytics_raw_trackings_get_phone_leads(phone):
    phone = is_none(phone)
    # Удаляем все буквы и пробелы из строки
    cleaned_phone = re.sub(r'[а-яёa-z ]', '', phone)

    # Применяем те же правила, что и в SQL CASE
    if len(cleaned_phone) == 11 and cleaned_phone[:2] in ('84', '89'):
        return '7' + cleaned_phone[-10:]
    elif len(cleaned_phone) == 10:
        return '7' + cleaned_phone
    elif len(cleaned_phone) == 12 and phone.startswith('77'):
        return cleaned_phone[-11:]
    elif len(cleaned_phone) == 12 and phone.startswith('789'):
        return '7' + cleaned_phone[-10:]
    elif len(cleaned_phone) > 12 and phone.startswith('79'):
        return cleaned_phone[:11]
    else:
        return cleaned_phone

