# ДЗ 3.1. Найпростіший калькулятор

number1 = float(input("Enter first number: "))
operator = input("Enter operator +, -, *, / : ")
number2 = float(input("Enter second number: "))

result: float = 0

if operator == '+':
    result = number1 + number2
elif operator == '-':
    result = number1 - number2
elif operator == '*':
    result = number1 * number2
elif operator == '/':
    if number2 == 0:
        print("Error: Division by zero is not possible!")
    else:
        result = number1 / number2

print(f"Result: {result}")