# ДЗ 3.2. Перемістити елемент у списку

# Приклади:
# [12, 3, 4, 10] => [10, 12, 3, 4]
# [1] => [1]
# [] => []
# [12, 3, 4, 10, 8] => [8, 12, 3, 4, 10]

list_numbers = [12, 3, 4, 10, 8]
if len(list_numbers) > 0:
    list_numbers.insert(0, list_numbers[-1])
    list_numbers.pop()

print(list_numbers)