# ДЗ 11.3. Перевірка на парність

def is_even(number):
    last_digit = str(number)[-1]
    return last_digit in '02468'

assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'
print('Ok')