# ДЗ 4.3. Список із 3 елементів

# Приклади:
# [1, 2, 3, 4, 5, 6, 7, 9] == [1, 3, 7]
# [1, 1, 2, 1] == [1, 2, 2]
# [6, 3, 7] == [6, 7, 3]

import random

lst = [1, 2, 3, 4, 5, 6, 7, 9]
result1 = [lst[0], lst[2], lst[-2]]

print("Homework list:")
print(f"{lst} == {result1}")

#-*- Next task -*-#

random_list = []
range_list = random.randint(3, 10)
num = 0

while num != range_list:
    random_list.append(random.randint(1, 10))
    num = num + 1

result2 = [random_list[0], random_list[2], random_list[-2]]

print("Random list:")
print(f"{random_list} == {result2}")