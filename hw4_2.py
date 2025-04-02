# ДЗ 4.2. Знайти суму елементів із парними індексами

# Пояснення:
# [0, 1, 7, 2, 4, 8] => (0 + 7 + 4) * 8 = 88

# [1, 3, 5] => 30
# [6] => 36
# [] => 0

lst = [0, 1, 7, 2, 4, 8]
even_index_sum = 0

if lst:
    for i, el in enumerate(lst):
        if i % 2 == 0:
            even_index_sum += el
    result = even_index_sum * lst[-1]
    print(f"{lst} == {result}")
else:
    print(0)