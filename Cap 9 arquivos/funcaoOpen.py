#usando a função open para criar um objeto do tipo arquivo
arquivo = open("c:\arquivos\arquivo_de_texto.txt")

#verificando o tipo do objeto arquivo
print(type(arquivo))

#printando o conteúdo do objeto arquivo
print(arquivo)

#printando o conteúdo do objeto arquivo
print(arquivo.read())

#printando uma linha do arquivo
print(arquivo.readline())

#printando outra linha do arquivo
print(arquivo.readline())

#Exibindo uma linha por vez, utilizando o loop for e o método readlines()
for linha in arquivo.readlines():
    print(linha)

print("###############################################")

#usando a função open para criar um objeto do tipo arquivo
arquivo = open("c:\arquivos\arquivo_de_texto.txt")

#Passando o conteúdo do arquivo para uma lista
linhas_do_arquivo = arquivo.readlines()

#comprovando o tipo do objeto linhas_do_arquivo
print("Ei! Eu consegui transformar meu arquivo em uma {} ".format(type(linhas_do_arquivo)))

#colocando a lista em ordem alfabética
linhas_do_arquivo.sort()

#Exibindo nossa lista, agora em ordem alfabética
print(linhas_do_arquivo)

print("###############################################")

#usando a função open para criar um objeto do tipo arquivo
arquivo = open("c:\arquivos\arquivo_de_texto.txt")

#Exibindo uma linha por vez, utilizando o loop for e o método readlines()
for linha in arquivo.readlines():
    print(linha)
arquivo.close()