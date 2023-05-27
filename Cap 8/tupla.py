#criação de uma tupla com as categorias dos Jedi
categorias = ("Youngling", "Padawan", "Knight", "Master")
#exibindo a tupla inteira -> ('Youngling', 'Padawan', 'Knight', 'Master')
print(categorias)
#exibindo o segundo item da tupla -> Padawan
print(categorias[1])
#usando um índice negativo para exibir o último item da tupla -> Master
print(categorias[-1])

print("##########################################")

#criação de uma tupla com as categorias dos Jedi
categorias = ("Youngling", "Padawan", "Knight", "Master")
#exibindo cada item da tupla usando um loop
for categoria in categorias:
    print(categoria)

print("##########################################")

#importando o módulo sys para conseguirmos usar o getsizeof
import sys
#criando uma lista e uma tupla vazias, respectivamente
lista_vazia = []
tupla_vazia = ()
#printando o tipo e tamanho de cada estrutura
print("O objeto lista_vazia é do tipo {} e ocupa {} bytes na memória".format(type(lista_vazia), sys.getsizeof(lista_vazia)))
print("O objeto tupla_vazia é do tipo {} e ocupa {} bytes na memória".format(type(tupla_vazia), sys.getsizeof(tupla_vazia)))

print("##########################################")

#criação e exibição da tupla
tupla = (1, 7, 7, 19, 3, 2, 11, 15, 6, 1, 5)
print(f"A tupla foi criada assim: {tupla}")
#utilizando enumerate para mostrar uma sequência
for numero, valor in enumerate(tupla):
    print(f"No índice {numero} temos: {valor}")

#mostrando a quantidade de itens na tupla
print(f"Quantidade: {len(tupla)}")

#mostrando o valor mínimo na tupla
print(f"Mínimo: {min(tupla)}")

#mostrando o valor máximo na tupla
print(f"Máximo: {max(tupla)}")

#mostrando a soma de todos os valores da tupla
print(f"Soma: {sum(tupla)}")

#utilizando tuple() para a conversão de uma lista para uma tupla
lista = [True,False]
print(f"Lista: {lista}")
tupla2 = tuple(lista)
print(f"Tupla: {tupla2}")

#criando a tupla3 com os valores 1 (True) e 0 (False)
tupla3 = (1,0)

#função all
print(f"Testando a tupla2 com all: {all(tupla2)}")
print(f"Testando a tupla3 com all: {all(tupla3)}")

#função any
print(f"Testando a tupla2 com any: {any(tupla2)}")
print(f"Testando a tupla3 com any: {any(tupla3)}")