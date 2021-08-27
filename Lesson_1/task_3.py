## Определить, какие из слов «attribute», «класс», «функция»,
## «type» невозможно записать в байтовом типе.


words = [b'attribute', b'класс', b'функция', b'type']

## b'класс', b'функция' - SyntaxError: bytes can only contain ASCII literal characters.
