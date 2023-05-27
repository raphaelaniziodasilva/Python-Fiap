# 1 – Você foi procurado por um aluno do curso de Produção Multimídia do FIAP ON para desenvolver um trabalho em parceria:
# um serviço em que as pessoas possam usar um estúdio profissional para gravar seus vídeos para o YouTube com máxima qualidade.
# O serviço ganha dinheiro por meio de um sistema de assinaturas e de um bônus calculado por uma porcentagem sobre o faturamento
# que o canal do cliente obteve ao longo do ano.
#
# Sua tarefa é criar um algoritmo que receba o tipo de assinatura do cliente, o faturamento anual dele e que calcule e
# exiba qual o valor do bônus que o cliente deve pagar a vocês. A tabela abaixo mostra a porcentagem de acordo com cada
# nível de assinatura:

# Nível         Porcentagem sobre o faturamento#
# Basic                         30%
# Silver                        20%
# Gold                          10%
# Platinum                      5%

cliente = input("Digite seu nome ")
op = -1
while op != 5:
    print("ASSINATURAS ANUAL")
    print("1 - Basic R$ 240,00 com direito a 30% de desconto")
    print("2 - Silver R$ 370,00 com direito a 20% de desconto")
    print("3 - Gold R$ 490,00 com direito a 10% de desconto")
    print("4 - Platinum R$ 550,00 mes, com direito a 5% de desconto")
    print("5 - Sair do programa")

    op = int(input("Informe sua opção: "))

    if op == 1:
        valor = float(240)
        desconto = float(valor) * 0.30
        descontoTotal = valor - desconto
        print(" Valor Atual R${}".format(valor))
        print(" Valor do desconto R${}".format(desconto))
        print(" Valor total com desconto R${}".format(descontoTotal))
    elif op == 2:
        valor = float(370)
        desconto = float(valor) * 0.20
        descontoTotal = valor - desconto
        print(" Valor Atual R${}".format(valor))
        print(" Valor do desconto R${}".format(desconto))
        print(" Valor total com desconto R${}".format(descontoTotal))
    elif op == 3:
        valor = float(490)
        desconto = float(valor) * 0.10
        descontoTotal = valor - desconto
        print(" Valor Atual R${}".format(valor))
        print(" Valor do desconto R${}".format(desconto))
        print(" Valor total com desconto R${}".format(descontoTotal))
    elif op == 4:
        valor = float(550)
        desconto = float(valor) * 0.5
        descontoTotal = valor - desconto
        print(" Valor Atual R${}".format(valor))
        print(" Valor do desconto R${}".format(desconto))
        print(" Valor total com desconto R${}".format(descontoTotal))

print("OK! O programa está encerrado...")