# ДЗ 5.3. hashtag

# Приклади:
# 'Python Community' -> #PythonCommunity
# 'i like python community!' -> #ILikePythonCommunity
# 'Should, I. subscribe? Yes!' -> #ShouldISubscribeYes

import string

user_input = input("Enter some text to create a hashtag: ")

hashtag = user_input.split()
words = []

for el in hashtag:
    for i in string.punctuation:
        el = el.replace(i, "")
    words.append(el.capitalize())

hashtag = "#" + "".join(words)

if len(hashtag) > 140:
    hashtag = hashtag[:140]

print(f"{user_input} -> {hashtag}")