# ДЗ 6.1. Діапазон букв

# Приклади:
# "a-c" -> abc
# "a-a" -> a
# "s-H" -> stuvwxyzABCDEFGH
# "a-A" -> abcdefghijklmnopqrstuvwxyzA

import string

print("Type two letters separated by \' - \'")
user_input = input('-> ')

start = string.ascii_letters.find(user_input[0])
end = string.ascii_letters.find(user_input[-1])

result = string.ascii_letters[start:end + 1]

print(result)