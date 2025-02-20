import numpy as np

notas = np.random.randint(40, 100, size=(30, 3))

print(notas)

print(f"media da primeira avaliação : {np.mean(notas,axis=0)[0]}")
print(f"media da segunda avaliação : {np.mean(notas,axis=0)[1]}")
print(f"media da substitutiva avaliação : {np.mean(notas,axis=0)[2]}")

# print(f"medias por aluno {np.mean(notas,axis=1)}")

media = 0
tamanho = notas.shape
print(tamanho)

for linha in range(tamanho[0]):
    media += notas[linha, 0]
print(f"media da primeira avaliação : {media/tamanho[0]}")
