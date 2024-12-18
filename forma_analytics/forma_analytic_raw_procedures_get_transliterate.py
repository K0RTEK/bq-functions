import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_transliterate(name):
    name = is_none(name)
    converter = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd',
        'е': 'e', 'ё': 'e', 'ж': 'zh', 'з': 'z', 'и': 'i',
        'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n',
        'о': 'o', 'п': 'p', 'р': 'p', 'с': 'c', 'т': 't',
        'у': 'u', 'ф': 'f', 'х': 'x', 'ц': 'c', 'ч': 'ch',
        'ш': 'sh', 'щ': 'sch', 'ь': '', 'ы': 'y', 'ъ': '',
        'э': 'e', 'ю': 'yu', 'я': 'ya'
    }
    word = name.lower().strip()
    answer = ''.join([converter.get(char, char) for char in word])
    answer = re.sub(r'[^-0-9a-z]', '-', answer)
    answer = re.sub(r'[-]+', '-', answer)
    answer = re.sub(r'^-|-$', '', answer)
    return answer