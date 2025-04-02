# ДЗ 7.3. Пошук підрядка

def second_index(text, any_str):
    first_index = text.find(any_str)
    result = text.find(any_str, first_index + 1)

    if first_index == -1 or result == -1:
        return None
    else:
        return result

assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')
