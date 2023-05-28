#Criando uma variável de texto
conteudo = "Estou testando criar um arquivo de texto. Então, estou... textando?"

#usando a função open para criar um objeto do tipo arquivo w = write
arquivo = open("c:\arquivos\novo_arquivo.txt", "w")

#Escrevendo o conteúdo da variável conteudo dentro do arquivo
arquivo.write(conteudo)

#fechando o arquivo
arquivo.close()

print("###############################################")

#Criando uma variável de texto
conteudo = "Estou testando criar um arquivo de texto. Então, estou... textando?"

#usando a função open para criar um objeto do tipo arquivo
# a = abrindo para escrita, anexando o novo conteudo ao final do conteudo ja existente no arquivo
arquivo = open("c:\arquivos\novo_arquivo.txt", "a")

#Escrevendo o conteúdo da variável conteudo dentro do arquivo
arquivo.write(conteudo)

#fechando o arquivo
arquivo.close()