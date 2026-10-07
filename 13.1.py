import codecs
import re


def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html_content = file.read()

    # Регулярное выражение удаляет всё, что находится между < и >
    clean_text = re.sub(r'<[^>]+>', '', html_content)

    with codecs.open(result_file, 'w', 'utf-8') as file:
        file.write(clean_text)