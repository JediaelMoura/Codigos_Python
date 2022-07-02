arquivo = open('ArquivodeTeste.txt', 'w')

arquivo.write('Curso Python \n')
arquivo.write('Aula Prática')
arquivo.close()

#leitura do arquivo de texto
leitura = open('ArquivodeTeste.txt', 'r')
print(leitura.read())
leitura.close()