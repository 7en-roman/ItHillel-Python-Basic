# ДЗ 5.1. Ім'я змінної

# Приклади:
# _ => True
# __ => False
# ___ => False
# x => True
# get_value => True
# get value => False
# get!value => False
# some_super_puper_value => True
# Get_value => False
# get_Value => False
# getValue => False
# 3m => False
# m3 => True
# assert => False
# assert_exception => True

import string
import keyword

while True:
    user_text = input("Enter your variable name: ")
    text_valid = 0

    if user_text.count("__") or user_text.count("___"):
        print(f"{user_text} => ", False)
    elif user_text[0] == "_":
        print(f"{user_text} => ", True)
    else:
        if user_text[0].isdigit():
            print(f"{user_text} => ", False)
        elif not user_text.islower():
            print(f"{user_text} => ", False)
        elif user_text.isspace():
            print(f"{user_text} => ", False)
        else:
            for el in user_text:
                for symbol in string.punctuation:
                    if symbol == "_":
                        continue

                    elif el == " " or el == symbol:
                        text_valid += 1

            if text_valid > 0:
                print(f"{user_text} => ", False)
            elif user_text in keyword.kwlist:
                print(f"{user_text} => ", False)
            else:
                print(f"{user_text} => ", True)

    menu = input('Do you want to continue? (Y) press enter to exit the program: ')

    if menu != 'Y' and menu.lower() != 'y':
        print("The program has finished its work!")
        break