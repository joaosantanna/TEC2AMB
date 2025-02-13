import string
from random import choices


def gerar_senha(tamanho, maiusculas, minusculas, numeros, simbolos):
    caracteres = ""

    if maiusculas:
        caracteres += string.ascii_uppercase
    if minusculas:
        caracteres += string.ascii_lowercase
    if numeros:
        caracteres += string.digits
    if simbolos:
        caracteres += string.punctuation
    letras = choices(caracteres, k=tamanho)

    senha = "".join(letras)
    return senha


if __name__ == "__main__":
    print(gerar_senha(8, True, True, True, False))
    print(gerar_senha(30, True, True, True, False))
