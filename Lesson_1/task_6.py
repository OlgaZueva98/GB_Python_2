## Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование»,
## «сокет», «декоратор». Проверить кодировку файла по умолчанию.
## Принудительно открыть файл в формате Unicode и вывести его содержимое.


import locale


words = ['сетевое программирование', 'сокет', 'декоратор']

with open('test_file.txt', 'w') as f:
    for word in words:
        f.write(word + '\n')

    print('Кодировка файла: {}'.format(f))

with open('test_file.txt', 'r', encoding='utf-8', errors='replace') as f:
    print(f.read())

## ������� ����������������
## �����
## ���������
