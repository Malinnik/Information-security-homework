from common.ciphers import caesar_cipher, vertical_permutation, vigenere_cipher
from common.alhabets import ALHABET, ALHABET_FROM_INT


def get_ceasar_key(text: str, cypher: str) -> int:
    """
        Возвращает ключ шифра Цезаря на основе текста и шифра
        Вернет -1 если ключ не найден
    """
    res = 0
    print(f"{text} - {cypher}: ", end="")
    while True:
        # print(f"{res}: {caesar_cipher(text, res)}")
        if cypher == caesar_cipher(text, res):
            print(res)
            return res

        if res > 100:
            print(-1)
            return -1

        res += 1

def get_ceasar_key_from_cipher(cipher: str, key: int | None = None) -> tuple[str, int]:
    """
    Возвращает оригинальное сообщение и ключ, на основе шифра

    Если ключ не указан, потребуется перебор возможных значений.
    Будет спрашиваться, является ли вариант декодировки корректным, если да, то возвращается декодированное сообщение и ключ

    Если ключ указан, то возвращается декодированное сообщение и ключ
    """
    res = 0

    if key:
        message = caesar_cipher(cipher, -key)
        print(f"{cipher} -> {message}")
        return message, key

    while True:
        message = caesar_cipher(cipher, -res)
        answer = input(f"{cipher} -> {message}  (y/N)")
        if answer == "Y" or answer == "y":
            return message, res
        res += 1
        if res > 33:
            print("Can`t decipher. No key")

def get_key_from_vigenere_cipher(text:str, cipher: str) -> str:
    """
        Возвращает ключ шифра Виженера на основе текста и шифра

        Так как буква шифра является индексом алфавита от разницы букв сообщения и шифра

        Итоговая строка шифра будет повторятся (как того требует алгоритм шифрования)
        Требуется самостоятельно найти слово (ключ), которое повторяется в строке

        Пример:
            Щ - З = 26 - 8 = 18 -> C
            ...
            сомсомсо -> СОМ

         
    """
    res = []
    for k, v in zip(text.lower(), cipher.lower()):
        key = ALHABET[v] - ALHABET[k]
        if key < 0:
            key = 33 - (-key)
        else:
            key %= 33
        res.append(ALHABET_FROM_INT[key])
    
    print(f"{text}-{cipher} -> {''.join(res)}")
    return ''.join(res)


if __name__ == "__main__":
    with open('result.txt', 'w', encoding='utf-8') as f:    
        print("Задание 2.1.")
        f.write("Задание 2.1.\n")
        f.write(f"Апельсин-Са(б)цэнгъя -> {get_ceasar_key('апельсин', 'сбцэнгъя')}\n")
        # Ошибка задания, не сАцэнгъя а сБцэнгъя
        f.write(f"Засада-Цоаото -> {get_ceasar_key('засада', 'цоаото')}\n")
        f.write(f"Синица-Жюгюлх -> {get_ceasar_key('синица', 'жюгюлх')}\n")
        f.write(f'Ягода-Дзуие -> {get_ceasar_key("ягода", "дзуие")}\n')
        f.write(f'Лисица-Гаианч -> {get_ceasar_key("лисица", "гаианч")}\n')

        print("\n\n")
        print("Задание 2.2.")
        f.write("\n\nЗадание 2.2.\n")
        f.write(f"Арутуьчн -> {get_ceasar_key_from_cipher('арутуьчн', 15)}\n")
        f.write(f"Дьюка -> {get_ceasar_key_from_cipher('дьюка', 29)}\n")
        f.write(f"Деэаэц -> {get_ceasar_key_from_cipher('деэаэц', 21)}\n")
        f.write(f"Лдотс -> {get_ceasar_key_from_cipher('лдотс', 4)}\n")
        f.write(f"Аратз -> {get_ceasar_key_from_cipher('аратз', 8)}\n")
        
        print("\n\n")

        print("Задание 2.3.")
        f.write("\n\nЗадание 2.3.\n")
        
        f.write(f"Закладка-Щочэорьо -> {get_key_from_vigenere_cipher('закладка', 'щочэорьо')}\n")
        print(f"Проверка СОМ:  {vigenere_cipher('щочэорьо', 'сом', decipher=True)} \n")
        f.write(f"Проверка СОМ:  {vigenere_cipher('щочэорьо', 'сом', decipher=True)}\n\n")
        
        
        f.write(f"Лесенка-Цндпцэк -> {get_key_from_vigenere_cipher('Лесенка', 'цндпцэк')}\n")
        print(f"Проверка КИТ:  {vigenere_cipher('цндпцэк', 'Кит', decipher=True)} \n")
        f.write(f"Проверка КИТ:  {vigenere_cipher('цндпцэк', 'Кит', decipher=True)}\n\n")

        f.write(f"Крокодил-Ьщъкамфл -> {get_key_from_vigenere_cipher('Крокодил', 'ьщъкамфл')}\n")
        print(f"Проверка СИЛА:  {vigenere_cipher('ьщъкамфл', 'Сила', decipher=True)} \n")
        f.write(f"Проверка СИЛА:  {vigenere_cipher('ьщъкамфл', 'Сила', decipher=True)}\n\n")

        f.write(f"Серенада-Йррпёлдк -> {get_key_from_vigenere_cipher('Серенада', 'йррпёлдк')}\n")
        print(f"Проверка ШЛАК:  {vigenere_cipher('йррпёлдк', 'Шлак', decipher=True)} \n")
        f.write(f"Проверка ШЛАК:  {vigenere_cipher('йррпёлдк', 'Шлак', decipher=True)}\n\n")

        f.write(f"Кукуруза-Чоцвэоуо -> {get_key_from_vigenere_cipher('Кукуруза', 'чоцвэоуо')}\n")
        print(f"Проверка МЫЛО:  {vigenere_cipher('чоцвэоуо', 'Мыло', decipher=True)} \n")
        f.write(f"Проверка МЫЛО:  {vigenere_cipher('чоцвэоуо', 'Мыло', decipher=True)}\n\n")




        print("Задание 2.4.")
        f.write("Задание 2.4.\n")
        f.write("ЗГА ТХСХЩЁТИЕП ФСПГУЫ ЕВВЭУ, МЯЭХМИП ЯДНЮЧКДП РЛЕКЫЕ\n")
        print("ЗГА ТХСХЩЁТИЕП ФСПГУЫ ЕВВЭУ, МЯЭХМИП ЯДНЮЧКДП РЛЕКЫЕ")

        result = (vigenere_cipher("ЗГА ТХСХЩЁТИЕП ФСПГУЫ ЕВВЭУ, МЯЭХМИП ЯДНЮЧКДП РЛЕКЫЕ", 'ошибка', decipher=True))
        f.write(f"1) {result}\n")
        print(f"1) {result}")
        result = (vigenere_cipher(result, 'ошибка', decipher=True))
        f.write(f"2) {result}\n\n")
        print(f"2) {result}")

        print("Задание 2.5.")
        f.write("Задание 2.5.\n")
        result = (vertical_permutation("Компьютерная безопасность", [6,2,3,1,5,4]))
        print(result)
        f.write(f"{result}\n\n")

        print("Задание 2.6.")
        f.write("Задание 2.6.\n")
        result = (vertical_permutation("Стеганография не является частью криптографии", [2,3,6,5,1,4]))
        print(result)
        f.write(f"{result}\n\n")
