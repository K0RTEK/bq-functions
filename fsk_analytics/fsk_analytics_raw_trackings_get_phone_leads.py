import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_phone_leads(phone: str) -> str:
    phone = is_none(phone)
    # Удаляем все буквы (латиницу и кириллицу) и пробелы
    cleaned_phone = re.sub(r'[а-яёa-z ]', '', phone)

    # Определяем длину строки после удаления букв и пробелов
    phone_length = len(cleaned_phone)

    # Применяем логику, аналогичную SQL-функции
    if phone_length == 11 and cleaned_phone[:2] in ['84', '89']:
        return '7' + cleaned_phone[-10:]
    elif phone_length == 10:
        return '7' + cleaned_phone
    elif phone_length == 12 and cleaned_phone.startswith('77'):
        return cleaned_phone[-11:]
    elif phone_length == 12 and cleaned_phone.startswith('789'):
        return '7' + cleaned_phone[-10:]
    elif phone_length > 12 and cleaned_phone.startswith('79'):
        return cleaned_phone[:11]
    else:
        return cleaned_phone
