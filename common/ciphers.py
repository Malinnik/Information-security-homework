from common.alhabets import ALHABET, ALHABET_FROM_INT
def caesar_cipher(text: str, key: int = 3) -> str:
    """
    Шифр Цезаря

    Args:
        text: текст для шифрования
        key: ключ сдвига для шифрования
    """
    result = ""

    for char in text.lower():
        if char not in ALHABET.keys():
            result += char
            continue
        result += ALHABET_FROM_INT[(ALHABET[char] + key) % 33]

    return result

    # Однострочный вариант, если интересно
    # return ''.join([int_to_char.get((ALHABET.get(char) + key) % 33) if char in ALHABET.keys() else char for char in text.lower()])


def vigenere_cipher(text: str, key_word: str, extra: int = 0, decipher: bool = False) -> str:
    """
    Шивр Виженера

    Сдвиг буквы происходит засчет шифра Цезаря, где текст - буква, а ключ - число (буква шифра)
    Args:
        text: текст для шифрования
        key_word: слово - ключ для шифрования
        extra: дополнительный сдвиг шифра
        decipher: bool - шифровать или дешифровать
    """
    result = ""

    def iter_key():
        """
        Итератор ключа шифврования

        Для данного алгоритма удобнее в использовании 
        чем вложенные циклы или zip / itertools
        """
        while True:
            for key in key_word.lower():
                yield key
    
    keys = iter_key()
    for char in text.lower():
        if char not in ALHABET.keys():
            result += char
            continue
        
        if decipher:
            result += caesar_cipher(char, -ALHABET[next(keys)] - extra)
        else:
            result += caesar_cipher(char, ALHABET[next(keys)] + extra)

    return result


def vertical_permutation(text, seq: list[int]):
    """
    Шифр вертикальной перестановки

    Args:
        text: текст для шифрования
        seq: последовательность шифрования

    Пример:
        text = "Hello"
        seq = [1, 2, 3]
    """
    chars = (char for char in text.lower() if char in ALHABET.keys())

    table: list[list[str]] = []
    for i in range((len(text) // len(seq)) + 1):
        line = []
        for j in range(len(seq)):
            try:
                line.append(next(chars))
            except StopIteration:
                line.append('')
        table.append(line)

    [print(row) for row in table]

    seq: dict[int, int] = {num: i for i, num in enumerate(seq)}
    seq = dict(sorted(seq.items()))

    result = ""

    for num, i in seq.items():
        for row in table:
            result += row[i]
                
        

    return result