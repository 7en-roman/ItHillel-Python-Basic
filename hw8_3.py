# ДЗ 8.3. Унікальне число

def find_unique_value(just_list):
   for number in just_list:
       if just_list.count(number) == 1:
           return number

assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")
