# ДЗ 6.2. Конвертер із числа в дату

# Приклади:
# 0 -> 0 днів, 00:00:00
# 224930 -> 2 дні, 14:28:50
# 466289 -> 5 днів, 09:31:29
# 950400 -> 11 днів, 00:00:00
# 1209600 -> 14 днів, 00:00:00
# 1900800 - > 22 дні, 00:00:00
# 8639999 -> 99 днів, 23:59:59
# 22493 -> 0 днів, 06:14:53
# 7948799 -> 91 день, 23:59:59

user_enter = int(input("Введіть числа від 0 до 8640000 -> "))
temp = user_enter

temp, set_sec = divmod(temp, 60)
temp, set_min = divmod(temp, 60)
day, hour = divmod(temp, 24)
result_day = 'Днів'

result_time = f"{str(hour).zfill(2)}:{str(set_min).zfill(2)}:{str(set_sec).zfill(2)}"

if 2 <= day % 10 <= 4:
    result_day = 'Дні'

elif day % 10 == 1:
    result_day = 'День'

if 11 <= day % 100 <= 14:
    result_day = 'Днів'

print(f"{day} {result_day}, {result_time}")