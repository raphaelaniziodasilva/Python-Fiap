# 1- Elabore um algoritmo em que o usuario informe quantos alimntos consumiu naquele dia e depois possa informar o numero
# de calorias de cada um dos alimentos e exibir o total de calorias consumido.

quantidade_alimentos = int(input("Informe quantos alimentos você consumiu hoje"))
total_calorias: int = 0
for alimento in range(1, quantidade_alimentos +1, 1):
    calorias = int(input("Informe a quantidade de calorias do {} alimento".format(alimento)))
    total_calorias = total_calorias + calorias

print("Foram consumidos {} calorias ao longo do dia".format(total_calorias))

# 2- bservando o mercado de educação infantil, você e sua equipe decidem criar um aplicativo por meio do qual as crianças
# aprndam a controlar seus gastos
# Com forma de validar um prototipo, foi solicitado que você crie um script simples, em que o usuario deve informar Quantas
# transações financeiras realizou ao longo de um dia e, na sequencia, deve informar o valor de cada uma das transações que realizou
# Seu programa devera exibir, ao final, o valor total gasto pelo usuario, bem como a média do valor de cada transação

quantidade_trasacoes = int(input("Informe a quantidade de transações"))
total_trasacoes = 0
for n_transacoes in range(1, quantidade_trasacoes +1, 1):
    transacao = float(input("Informe a transação de número {}".format(n_transacoes)))
    total_trasacoes = total_trasacoes + transacao

media = total_trasacoes / quantidade_trasacoes
print("Neste dia foi gasto um total de R${}, cm uma média de R${} por transação".format(total_trasacoes, media))