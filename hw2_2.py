# ДЗ 2.2. Необхідно "перевернути" 5-ти значне число

number = int(input("Enter a 5-digit number: "))

num1 = (number // 1) % 10
num2 = (number // 10) % 10
num3 = (number // 100) % 10
num4 = (number // 1000) % 10
num5 = number // 10000

result = num1 * 10000 + num2 * 1000 + num3 * 100 + num4 * 10 + num5

print("First option: ")
print(result, "\n")

### Або ###

print("Second option: ")
print(f"{num1}{num2}{num3}{num4}{num5}")