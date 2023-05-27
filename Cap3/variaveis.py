# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

ano = 1989
nome = "Luke Skywalker"
saldo = 50.30

# tipo da variável
print(("O tipo da variável ano é {}".format(type(ano))))
print(("O tipo da variável nome é {}".format(type(nome))))
print(("O tipo da variável saldo é {}".format(type(saldo))))

# convertendo a variável folat para int
variavel_int = int(saldo)
print(saldo) # float
print(variavel_int)

# vamos interagir com o usuario
nome = input("Digite seu nome ")
# .format vai incluir dentro da chave o conteudo da variável
print("Seu nome é {}".format(nome))

# usando if
rm = input("Insira seu RM ")
idade = input("Insira sua idade ")
if int(idade) >= 18:
    print("Sua participação foi autorizada, aluno de RM {}!".format(rm))
    print("Mais informações serão enviadas para seu e-mail cadastrado!")

