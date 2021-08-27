## Преобразовать слова «разработка», «администрирование», «protocol», «standard»
## из строкового представления в байтовое и выполнить обратное преобразование (используя методы encode и decode).


w_bytes = []

words = ['разработка', 'администрирование', 'protocol', 'standard']
for word in words:
   b = word.encode('utf-8')
   w_bytes.append(b)
   print(b)

for b in w_bytes:
    print(bytes.decode(b, 'utf-8'))
