import json
#Criando uma variável de texto
conteudo = "Estou testando criar um arquivo de texto. Então, estou... textando?"

#usando a função open para criar um objeto do tipo arquivo
arquivo = open("c:\arquivos\agenda.json")

#colocando o conteúdo do arquivo em uma variável do tipo string
conteudo_do_arquivo = arquivo.read()

#fechando o arquivo
arquivo.close()

#usando o método loads para converter uma string no formato json em um dicionário
agenda = json.loads(conteudo_do_arquivo)

#comprovando que o objeto agenda é do tipo dicionário
print("O tipo do objeto agenda é {}".format(type(agenda)))

print("###############################################")

#o with usará o open para abrir o arquivo indicado, dentro do objeto arquivo e fará sozinho o encerramento do acesso quando a última linha de código dentro dele for executada
with open("c:\arquivos\arquivo_de_texto.txt", "r") as arquivo:
    #aqui devemos escrever todos os códigos que usam o arquivo aberto, pois após a última linha de código dentro dessa estrutura, o arquivo será automaticamente encerrado
    print(arquivo.read())

print("###############################################")

#o with usará o open para abrir o arquivo indicado, dentro do objeto arquivo e fará sozinho o encerramento do acesso quando a última linha de código dentro dele for executada
with open("c:\arquivos\arquivo_de_texto.txt", "w") as arquivo:
    #aqui devemos escrever todos os códigos que usam o arquivo aberto, pois após a última linha de código dentro dessa estrutura, o arquivo será automaticamente encerrado
    arquivo.write("May the force be with you")

