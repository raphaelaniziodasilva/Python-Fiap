#valores fora de ordem
valores = [1, 7, 7, 19, 3, 2, 11, 15, 6, 1, 5]
#exibição da lista
print("A lista foi criada assim: {}".format(valores))
#contagem de elementos
contagem = valores.count(7)
print("Nessa lista o número 7 aparece {} vezes".format(contagem))
#invertendo a lista
valores.reverse()
print("A lista agora está invertida: {}".format(valores))
#ordenando a lista
valores.sort()
print("A lista agora está ordenada: {}".format(valores))

#valores de uma lista
valores = [2, 3, 5, 10]
#tamanho da lista
tamanho = len(valores)
print("A lista tem {} elementos".format(tamanho))
#soma dos elementos
soma = sum(valores)
print("A soma dos elementos é {}".format(soma))

notas = []
opcao = -1
while opcao !=4:
    print("1 - Informar notas ")
    print("2 - Exibir notas ")
    print("3 - Calcular média ")
    print("4 - Sair")
    opcao = int(input(("Escolha sua opção: ")))

    if opcao == 1:
        notas.append(float(input("Digite sua nota: ")))
    elif opcao == 2:
        for n in notas:
            print(n)
    elif opcao == 3:
        print(sum(notas) / len(notas))