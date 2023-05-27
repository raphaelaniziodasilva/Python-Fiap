#criando um dicionário vazio
dicionário = {}
#exibindo o tipo do dicionário
print("O objeto dicionário é do tipo {}".format(type(dicionário)))

print("##########################################")

#criando um dicionário com dados
dicionário = {"Yoda":"Mestre Jedi", "Mace Windu": "Mestre Jedi", "Anakin Skywalker":"Cavaleiro Jedi", "R2-D2":"Dróide", "Dex":"Balconista"}
#exibindo o valor associado a uma chave específica
print(dicionário["R2-D2"])
#exibindo todos os valores em um dicionário
for valor in dicionário.values():
    print(valor)

print("##########################################")

#criando um dicionário com dados
dicionário = {"Yoda":"Mestre Jedi", "Mace Windu": "Mestre Jedi", "Anakin Skywalker":"Cavaleiro Jedi", "R2-D2":"Dróide", "Dex":"Balconista"}
#exibindo o dicionário completo
for chave, valor in dicionário.items():
    print("O personagem {} é da categoria {}".format(chave, valor))

print("##########################################")

#criando um dicionário vazio
dicionário = {}
#incluindo dados no dicionário
dicionário["André David"] = "Professor"
#Pedindo para o usuário incluir dados no dicionário
nova_chave = input("Informe o nome do colaborador da FIAP")
novo_valor = input("Informe a função do colaborador da FIAP")
dicionário[nova_chave] = novo_valor
#exibindo o dicionário completo
for chave, valor in dicionário.items():
    print("O colaborador {} desempenha a função de {}".format(chave, valor))

print("##########################################")

#criando um dicionário vazio
dicionário = {}
#incluindo dados no dicionário
dicionário["André David"] = "Professor"
#alterando dados no dicionário
dicionário["André David"] = "Coordenador"
#exibindo o dicionário completo
for chave, valor in dicionário.items():
    print("O colaborador {} desempenha a função de {}".format(chave, valor))

print("##########################################")

#criando um dicionário com dados
dicionário = {"Yoda":"Mestre Jedi", "Mace Windu": "Mestre Jedi", "Anakin Skywalker":"Cavaleiro Jedi", "R2-D2":"Dróide", "Dex":"Balconista"}
#exibindo o dicionário completo
for chave, valor in dicionário.items():
    print("O personagem {} é da categoria {}".format(chave, valor))
#removendo o item cuja chave é R2-D2
dicionário.pop("R2-D2")
#exibindo o dicionário completo após a remoção
for chave, valor in dicionário.items():
    print("O personagem {} é da categoria {}".format(chave, valor))

print("##########################################")

#criando um dicionário com dados
dicionário = {"Yoda":"Mestre Jedi", "Mace Windu": "Mestre Jedi", "Anakin Skywalker":"Cavaleiro Jedi", "R2-D2":"Dróide", "Dex":"Balconista"}
#exibindo o dicionário completo
for chave, valor in dicionário.items():
    print("O personagem {} é da categoria {}".format(chave, valor))
#removendo o último item
dicionário.popitem()
#exibindo o dicionário completo após a remoção
for chave, valor in dicionário.items():
    print("O personagem {} é da categoria {}".format(chave, valor))

print("##########################################")

#criando um dicionário com dados
dicionário = {"Yoda":"Mestre Jedi", "Mace Windu": "Mestre Jedi", "Anakin Skywalker":"Cavaleiro Jedi", "R2-D2":"Dróide", "Dex":"Balconista"}
#exibindo o dicionário completo
for chave, valor in dicionário.items():
    print("O personagem {} é da categoria {}".format(chave, valor))
#removendo todos os itens do dicionário
dicionário.clear()
#exibindo o dicionário completo após a remoção
for chave, valor in dicionário.items():
    print("O personagem {} é da categoria {}".format(chave, valor))

print("##########################################")

#criando o dicionário dos contatos
contatos = {
    "Clark Kent":
        {"Celular":"123456",
         "Email":"super@krypton.com"},
    "Bruce Wayne":
        {"Celular":"654321",
         "Email":"bat@caverna.com.br"}
}
#esse for passará por todos os items do dicionário contatos, com a variável "contato" contendo as chaves desses items e o objeto formas contendo os valores, que são os dicionários de formas de contatos
for contato, formas in contatos.items():
    #para cada item encontrado no dicionário anterior, que estão contidos no dicionário "formas", vamos recuperar as chaves "celular" e "email" e seus valores
    for celular, email in formas.items():
        #exibimos aqui o nome do contato e as suas formas de contato
        print("O contato {} pode ser encontrado no celular {} e no email {}".format(contato, celular, email))