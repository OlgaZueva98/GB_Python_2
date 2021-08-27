## Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
## преобразовать результаты из байтовового в строковый тип на кириллице.

import subprocess


line_res = ''
args = [['ping', 'yandex.ru'], ['ping', 'youtube.com']]

def ping(arg, line_res):
    ping_res = subprocess.Popen(arg, stdout=subprocess.PIPE)
    for line in ping_res.stdout:
        line_res += line.decode('cp866')
    return line_res

for arg in args:
    result = ping(arg, line_res)
    print(result)
