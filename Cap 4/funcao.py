#solicitar distância e tempo
distancia = float(input("Digite a distância percorrida"))
tempo = float(input("Digite o tempo da viagem"))
#calcular a velocidade média
velocidade_media = distancia/tempo
#exibir o resultado
print("A velocidade média é {} km/h".format(velocidade_media))

#Função que calcula a velocidade média
def calcularVelocidadeMedia():
    #solicitar distância e tempo
    distancia = float(input("Digite a distância percorrida"))
    tempo = float(input("Digite o tempo da viagem"))
    #calcular a velocidade média
    velocidade_media = distancia/tempo
    #exibir o resultado
    print("A velocidade média é {} km/h".format(velocidade_media))

#aqui começa o programa principal
calcularVelocidadeMedia()

#Função que calcula a velocidade média
def calcularVelocidadeMedia(distancia, tempo):
    #calcular a velocidade média
    velocidade_media = distancia/tempo
    #exibir o resultado
    print("A velocidade média é {} km/h".format(velocidade_media))

#aqui começa o programa principal
distancia = float(input("Informe a distância"))
tempo = float(input("Informe o tempo"))
#chamando a função com valores definidos pelo usuário
calcularVelocidadeMedia(distancia, tempo)

#chamando a função com valores definidos pelo programador
calcularVelocidadeMedia(15,2)

#Função que calcula a velocidade média
def calcularVelocidadeMedia(distancia, tempo):
    #calcular a velocidade média
    velocidade_media = distancia/tempo
    #exibir o resultado
    return velocidade_media
#aqui começa o programa principal
dist = float(input("Informe a distância"))
temp = float(input("Informe o tempo"))
#chamando a função com valores definidos pelo usuário
print("A velocidade média é {}".format(calcularVelocidadeMedia(dist, temp)))

#função de soma
def somar(a, b):
    return float(a) + float(b)

#função de subtração
def subtrair(a, b):
    return float(a) - float(b)

#função de divisão
def dividir(a, b):
    if b==0:
        return 0
    return float(a) / float(b)

#função de multiplicar
def multiplicar(a, b):
          return float(a) * float(b)

