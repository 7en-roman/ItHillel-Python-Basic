# ДЗ 5.2. Модифікувати калькулятор

while True:
    first_number = float(input("Enter first number: "))
    operator = input("Enter operator +, -, *, / : ")
    second_number = float(input("Enter second number: "))

    result: float = 0

    if operator == '+':
        result = first_number + second_number
    elif operator == '-':
        result = first_number - second_number
    elif operator == '*':
        result = first_number * second_number
    elif operator == '/':
        if second_number == 0:
            print("Error: Division by zero is not possible!")
        else:
            result = first_number / second_number

    print(f"Result: {result}")

    menu = input('Do you want to continue? (Y) press enter to exit the program: ')

    if menu != 'Y' and menu.lower() != 'y':
        print("The program has finished its work!")
        break