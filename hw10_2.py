# ДЗ 10.2. Знайти перше слово

import string

def first_word(text):
    """ Пошук першого слова """

    for i in string.punctuation:
        if i in text and i != "'":
           text = text.replace(i, " ").strip()

    words = text.split()

    return str(words[0]) if words else None

assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')
