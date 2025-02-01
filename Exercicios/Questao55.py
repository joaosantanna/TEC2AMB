from random import randint

lacamento_dados = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
for i in range(1000):
    d1 = randint(1, 6)
    d2 = randint(1, 6)
    v = d1 + d2
    lacamento_dados[v] += 1

for chave, valor in lacamento_dados.items():
    print(f"{chave} - {valor/10:.2f} %")

print(sum(lacamento_dados.values()))
