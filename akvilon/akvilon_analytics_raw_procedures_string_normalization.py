def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def string_normalization(str_field):
    str_field = is_none(str_field)
    # Нормализует строку: удаляет лишние пробелы, преобразует в нижний регистр, возвращает NULL для пустых значений
    if str_field is None or str_field.strip() == '' or str_field.strip() == '-':
        return None
    return str_field.strip()