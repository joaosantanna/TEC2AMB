from prettytable import PrettyTable
from random import randint

tabela = PrettyTable()

turma = []
nomes = ["Ana", "Eduardo", "Marcia", "Lucas"]
idades = [4, 5, 6, 4]

for i in range(4):
    nome = nomes[i]
    idade = idades[i]
    print("Digite as 4 notas do aluno")
    notas = []
    for n in range(1, 5):
        nota = float(randint(40, 100) / 10)
        notas.append(nota)
    ficha = {"nome": nome, "idade": idade, "notas": notas}
    turma.append(ficha)


print("Dados da turma")
tabela.field_names = ["Nome", "Idade", "Notas", "Media das notas"]
for aluno in turma:
    media = sum(aluno["notas"]) / 4
    tabela.add_row([aluno["nome"], aluno["idade"], aluno["notas"], media])
    # print(f'{aluno["nome"]} - idade: {aluno["idade"]} ', end="")
    # print(f' Notas:{aluno["notas"]} - Media: {sum(aluno["notas"])/4:.2f}')

print(tabela)
