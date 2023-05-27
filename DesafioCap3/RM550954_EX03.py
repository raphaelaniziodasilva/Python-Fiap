#  3 – Muitos professores preferem adotar modelos diferentes de provas quando dão aulas para turmas muito grandes. Por essa
#  razão, a escola de inglês JoWell Sant’ana, em que todas as turmas são compostas por 50 alunos, solicitou que você criasse
#  um sistema capaz de atender ao seguinte requisito: o professor deve digitar primeiro as notas dos 25 alunos que têm número
#  ímpar na chamada (1, 3, 5..., 47, 49) e depois as notas dos 25 alunos que têm número par (2, 4, 6..., 48, 50).
#  O sistema deve calcular e exibir a média de cada uma das metades da sala e informar, ao final, qual delas teve a maior nota.
#
# Há ainda um pedido especial do mantenedor: para que os professores não se confundam, ao digitar cada uma das notas,
# deve ser exibida uma mensagem no seguinte padrão:
#
# VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES (ou ímpares, quando for o caso).
#
# POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO x.

notaImpar = 0
alunosImpar = 0
notaPar = 0
alunosPar = 0

alunos = int(input("Digite a quantidade de alunos "))

print(("Digite as notas dos alunos impares "))
for i in range(1, alunos +1, 2):
    notas = float(input("Aluno numero {} ".format(i)))
    notaImpar += notas
    alunosImpar += 1

mediaAlunosImpar = notaImpar / alunosImpar
print("A media da turma impar {}".format(mediaAlunosImpar))

print(("Digite as notas dos alunos pares "))
for i in range(2, alunos +1, 2):
    notas = float(input("Aluno numero {} ".format(i)))
    notaPar += notas
    alunosPar += 1

mediaAlunosPar = notaPar / alunosPar
print("A media da turma par {}".format(mediaAlunosPar))

if mediaAlunosImpar > mediaAlunosPar:
    print("A turma impar tem a melhor media de {}".format(mediaAlunosImpar))
else:
    print("A turma par tem a melhor media de {}".format(mediaAlunosPar))
