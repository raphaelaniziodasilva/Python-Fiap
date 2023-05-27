nome = input("Digite o nome do funcionario ")
salario = float(input("Digite o salario do funcionario "))

if salario < 0:
    salario = salario * -1
    print("O salário é negativo")

print("O salário do funcionário {} é {}".format(nome, salario))

# if e else
rm = input("Insira seu RM ")
idade = input("Insira sua idade ")
if int(idade) >= 18:
    print("Sua participação foi autorizada, aluno de RM {}!".format(rm))
    print("Mais informações serão enviadas para seu e-mail cadastrado!")
else:
    print("Sua participação não foi autorizada por causa da sua idade")

# if encadeado
rm = input("Insira seu RM")
idade = input("Insira sua idade")
if int(idade) >= 18:
    print("Sua participação foi autorizada, aluno de RM {}!".format(rm))
    print("Mais informações serão enviadas para seu e-mail cadastrado!")
else:
    autorizado = input("Você possui autorização dos responsáveis? S-SIM ou N-NÃO")
    if autorizado == 'S':
        print("Sua participação foi autorizada, aluno de RM {}!".format(rm))
        print("Mais informações serão enviadas para o email dos responsáveis!")
    else:
        print("Sua participação não foi autorizada por causa da sua idade")

# pontuacao = input("Insira a pontuação do cliente: ")
# pontuacao = int(pontuacao)
# if pontuacao >= 1000:
#     print("O cliente tem direito a receber mais 3gb na sua franquia de internet!")
# else:
#     if pontuacao >=500:
#         print("O cliente tem direito a receber mais 1,5gb na sua franquia de internet!")
#     else:
#         if pontuacao >=200:
#             print("O cliente tem direito a receber mais 500mb na sua franquia de internet!")
#         else:
#             print("O cliente não receberá bônus.")
pontuacao = input("Insira a pontuação do cliente: ")
pontuacao = int(pontuacao)
if pontuacao >= 1000:
    print("O cliente tem direito a receber mais 3gb na sua franquia de internet!")
elif pontuacao >= 500:
    print("O cliente tem direito a receber mais 1,5gb na sua franquia de internet!")
elif pontuacao >= 200:
    print("O cliente tem direito a receber mais 500mb na sua franquia de internet!")
else:
    print("O cliente não receberá bônus.")

# solicitando os dados do aluno
email_aluno = input("Informe o e-mail do aluno")
nota_semestral = input("Informe a nota semestral do aluno: ")
# convertendo a nota para o formato float
nota_semestral = float(nota_semestral)
# realizando o teste lógico
if nota_semestral > 8.5:
    print("ENVIANDO E-MAIL PARA {}".format(email_aluno))

# solicitando os dados do cliente
valor_compra = input("Informe o valor da compra realizada ")
cupom = input("Digite o cupom de desconto ")
# realizando o teste lógico com o cupom em maiúsculas
if cupom.upper() == "NIVER10":
    print("10% de desconto")
