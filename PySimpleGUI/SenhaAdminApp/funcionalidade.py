import string
import random


def gerar_senha(tamanho, usar_maiusculas, usar_minusculas, usar_numeros, usar_simbolos):
    caracteres = ""
    if usar_maiusculas:
        caracteres += string.ascii_uppercase
    if usar_minusculas:
        caracteres += string.ascii_lowercase
    if usar_numeros:
        caracteres += string.digits
    if usar_simbolos:
        caracteres += string.punctuation

    # print(caracteres) # visualizar os caracteres que serão usados

    if not caracteres:  # se nada for escolhido caracteres será vazio
        return ""

    senha = ""
    for i in range(tamanho):
        senha += random.choice(caracteres)

    return senha


if __name__ == "__main__":
    print(gerar_senha(10, True, True, True, True))
