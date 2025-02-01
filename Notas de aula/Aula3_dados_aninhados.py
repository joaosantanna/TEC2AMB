turma = [
    ["everton", 8.0, 7.5, 8.5],
    ["maria", 9.0, 8.5, 7.5],
    ["joao", 5.0, 6.0, 6.5],
]

# for aluno in turma:
#    print(aluno)


f1 = turma[0][1:]
f1.insert(0, turma[2][0])
f2 = turma[2][1:]
f2.insert(0, turma[0][0])
# print(f1)
# print(f2)

turma.insert(0, f2)
turma.append(f1)

turma.pop(1)
turma.pop(2)

for aluno in turma:
    print(aluno)


"""

for aluno in turma:
    print(aluno)

turma[0][1], turma[0][2], turma[0][3], turma[2][1], turma[2][2], turma[2][3] = (
    turma[2][1],
    turma[2][2],
    turma[2][3],
    turma[0][1],
    turma[0][2],
    turma[0][3],
)

for aluno in turma:
    print(aluno)
"""
