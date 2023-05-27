# 2 – Os alunos da sua turma fizeram uma votação para escolher qual dia da semana é o melhor para a realização das lives.
# Desenvolva um programa em que o usuário informe a quantidade de votos que cada um dos 5 dias da semana
# (segunda-feira, terça-feira, quarta-feira, quinta-feira e sexta-feira) obtiveram, verifique e exiba qual dia foi o escolhido.

listaVotos = []
diaSemana = []
dia = ''
maior = 0

for v in range(0, 5):
    diaSemana.append(input("Informe o dia da semana "))
    listaVotos.append(int(input("Digite a quantidade de votos do dia ")))

    if listaVotos[v] > maior:
        maior = listaVotos[v]
        dia = diaSemana[v]

print("O melhor dia para a realização das lives {}, eleito por {} votos".format(dia, maior))