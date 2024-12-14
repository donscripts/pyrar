import os
from os.path import exists, isfile, normcase
import subprocess
from sys import argv

if argv[1:]:
    co= ' '.join(argv[1:])
    pasta= argv[-1]
    argv.pop()
    arquivo= ' '.join(argv[1:])
    if exists(arquivo) and isfile(arquivo) and not exists(pasta):
        print(f'{arquivo} indo para {pasta}')
        c= ['rar.exe', 'x', arquivo, normcase(f'{pasta}/')]
        res= subprocess.run(c, stdout= subprocess.DEVNULL, stderr= subprocess.DEVNULL)
        if res.returncode== 0:
            print(f'[concluido] => extracao feita')
        else:
            print(f'[encerramento] => ocorreu algum erro')
    else:
        print(f'[encerramento] => informe um arquivo existente e uma pasta que nao exista')
else:
    print(f'[encerramento] => informe o arquivo .rar para extrai-lo')
