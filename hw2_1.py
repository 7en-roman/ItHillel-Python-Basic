# ДЗ 2.1. Виведення числа в стовпчик

number = int(input("Enter a 4-digit number: "))

num1 = number // 1000
num2 = (number // 100) % 10
num3 = (number // 10) % 10
num4 = (number // 1) % 10

print("First option: ")
print(num1)
print(num2)
print(num3)
print(num4, "\n")

### Або ###

print("Second option: ")
print(f"{num1}\n{num2}\n{num3}\n{num4}")