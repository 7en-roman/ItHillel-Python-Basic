# ДЗ 6.3. Добуток чисел

# Приклади:
# 999 -> 2 # Ось чому - 999 розбиваємо на цифри і перемножуємо 9 * 9 * 9 = 729, Потім 7 * 2 * 9 = 126, потім 1 * 2 * 6 = 12 і в результаті 1 * 2 = 2
# 1000 -> 0
# 423 -> 8
# 33 -> 9
# 25 -> 0
# 1 -> 1

user_enter = int(input("Enter digits -> "))

while user_enter > 9:
    counter = 1

    for digits in str(user_enter):
        counter *= int(digits)
    user_enter = counter

print(f"Result: {user_enter}")
