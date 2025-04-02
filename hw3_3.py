# ДЗ 3.3. Розділити один список на два списки

# Приклади:
# [1, 2, 3, 4, 5, 6] => [[1, 2, 3], [4, 5, 6]]
# [1, 2, 3] => [[1, 2], [3]]
# [1, 2, 3, 4, 5] => [[1, 2, 3], [4, 5]]
# [1] => [[1], []]
# [] => [[], []]

list_numbers = []
split_index = len(list_numbers) // 2

if len(list_numbers) % 2 != 0:
    split_index += 1

type1 = list_numbers[:split_index]
type2 = list_numbers[split_index:]

print(f"Result 1 ->\t {type1}")
print(f"Result 2 ->\t {type2}")

final_result = [type1, type2]
print(final_result)