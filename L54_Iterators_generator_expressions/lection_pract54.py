'''Генерация безопасных паролей
Программа должна сгенерировать все возможные пароли длиной 4 символа, соблюдая следующие условия:
● Пароль должен содержать хотя бы одну заглавную букву, одну строчную букву и одну цифру.
● Символы не должны повторяться.
● Соседние символы не могут быть расположены подряд в таблице символов.
● Все подходящие пароли записываются в файл valid_passwords.txt.
Данные:
from string import ascii_lowercase,
ascii_uppercase, digits
Пример данных в файле:
acA0
acA1
acA2
acA3
acA4
acA5
acA6
acA7
acA8
'''

from itertools import permutations
from string import ascii_lowercase, ascii_uppercase, digits

all_chars = list(ascii_lowercase + ascii_uppercase + digits)

# Фильтр для проверки условий пароля
def is_valid(password):
    has_lower = any(c in ascii_lowercase for c in password)
    has_upper = any(c in ascii_uppercase for c in password)
    has_digit = any(c in digits for c in password)
    if not (has_lower and has_upper and has_digit):
        return False
    for i in range(len(password) - 1):
        if abs(ord(password[i]) - ord(password[i + 1])) == 1:
            return False
    return True

# Генерация всех перестановок
all_variants = permutations(all_chars, 4)
valid_passwords = ("".join(p) for p in all_variants if is_valid(p))
with open("valid_passwords.txt", "w") as file:
    file.write("\n".join(valid_passwords))