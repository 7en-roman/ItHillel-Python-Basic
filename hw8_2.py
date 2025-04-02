# ДЗ 8.2. Паліандром

import string

def is_palindrome(text):
    clean_text = text.lower().replace(' ', '')

    for el in string.punctuation:
        if clean_text.find(el) != -1:
            clean_text = clean_text.replace(el, '')

    if clean_text == clean_text[::-1]:
        return True
    else:
        return False

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")

