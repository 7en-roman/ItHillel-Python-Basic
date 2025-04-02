# ДЗ 4.1. Перемістити всі нулі до кінця списку

# Приклади:
# [0, 1, 0, 12, 3] -> [1, 12, 3, 0, 0]
# [0] -> [0]
# [1, 0, 13, 0, 0, 0, 5] -> [1, 13, 5, 0, 0, 0, 0]
# [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0] -> [9, 7, 31, 45, 45, 45, 96, 0, 0, 0, 0, 0, 0, 0]

lst = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
non_zero_elements = []
elements = []

for el in lst:
    if el != 0:
        non_zero_elements.append(el)
    else:
        elements.append(el)
result = non_zero_elements + elements
print(result)