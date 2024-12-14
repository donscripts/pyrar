import os
import subprocess
from os.path import isfile, isdir, exists
import sys
from sys import argv

if argv[1:]:
    itens= []
    nome= argv[-1]
    argv.pop()
    conteudo= argv[1:]
    if not exists(nome):
        c= ['rar.exe', 'a', nome]
        print(f'[ok] => [{nome}] nao existe')
        for item in conteudo:
            if exists(item):
                print(f'[ok] => [{item}] existe')
                itens.append(item)
                c.append(item)
            else:
                print(f'[erro] => [{item}] nao existe')
        if len(itens) > 0:
            print(f'[ok] => a itens para serem inseridos')
            print(f'[info] => itens: {itens}, com um total: {len(itens)} itens')
            comando= subprocess.run(c, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            if comando.returncode== 0:
                print(f'[concluido] => arquivo .rar criado ,com {len(itens)} itens')
            else:
                print(f'[encerramento] => ocorreu algum erro')
        else:
            print(f'[encerramento] => nao a itens para serem inseridos')
    else:
        print(f'[encerrado] => [{nome}] ja existe')
