import PyPDF2
import os
#criando o mesclador de pdf
murger = PyPDF2.PdfMerger()

#criando uma lista de arquivos
lista_arquivos = os.listdir('arquivos')

#colocando em ordem a lista
lista_arquivos.sort()

#loop e condição para adicionar todos os pdf
for arquivo in lista_arquivos:
   if '.pdf' in arquivo:
        murger.append(f'arquivos/{arquivo}')

#mandando criar o último pdf
murger.write('pdf final.pdf')