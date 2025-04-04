# ДЗ 12.1. Очистити текст від html-тегів

import codecs

def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()
        cleaned_html = ''
        tag_text = False

        for i in html:
            if i == '<':
                tag_text = True
            elif i == '>':
                tag_text = False
            elif not tag_text:
                cleaned_html += i

    with codecs.open(result_file, 'w', 'utf-8') as file:
        file.write(cleaned_html)

delete_html_tags('draft.html', 'cleaned_text')
