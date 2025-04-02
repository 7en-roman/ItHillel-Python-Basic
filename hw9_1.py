# ДЗ 9.1. Визначити популярність певних слів у тексті

def popular_words (text, words):
    get_text = text.lower().split()
    result = {}

    for word in words:
        result_count = get_text.count(word)
        result[word] = result_count
    return result

assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''',
                     ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')
