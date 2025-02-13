import PySimpleGUI as sg
from funcionalidade import gerar_senha


sg.theme("LightGrey1")


layout = [
    [sg.Text("Gerenciador de senhas", font=("Helvetica", 20))],
    [sg.Text("Conta", size=(10, 1)), sg.Input(key="-CONTA-", size=(30, 1))],
    [sg.Text("Usuário", size=(10, 1)), sg.Input(key="-USUARIO-", size=(30, 1))],
    [
        sg.Text("Senha", size=(10, 1)),
        sg.Input(key="-SENHA-", password_char="*", size=(30, 1)),
        sg.Checkbox("Visualizar", key="-VER-", enable_events=True),
    ],
    [
        sg.Text("Campos"),
        sg.Button("Gerar Senha"),
        sg.Spin(
            values=[i for i in range(6, 31)],
            initial_value=6,
            key="-TAMANHO-",
            size=(3, 2),
        ),
    ],
    [
        sg.Checkbox("Minusculas", key="-MINUSCULAS-", default=True),
        sg.Checkbox("Maiusculas", key="-MAIUSCULAS-", default=True),
        sg.Checkbox("Numeros", key="-NUMEROS-"),
        sg.Checkbox("Simbolos", key="-SIMBOLOS-"),
    ],
    [sg.Button("Gravar Senha", size=(15, 1)), sg.Button("Sair", size=(15, 1))],
]

janela = sg.Window("Gerenciador de senhas", layout, font=("Helvetica", 14))

while True:
    eventos, valores = janela.read()
    if eventos in ("Sair", sg.WIN_CLOSED):
        break
    if eventos == "Gerar Senha":
        tamanho = valores["-TAMANHO-"]
        maiusculas = valores["-MAIUSCULAS-"]
        minuscula = valores["-MINUSCULAS-"]
        numeros = valores["-NUMEROS-"]
        simbolos = valores["-SIMBOLOS-"]
        senha = gerar_senha(tamanho, maiusculas, minuscula, numeros, simbolos)
        janela["-SENHA-"].update(senha)

    if eventos == "-VER-":
        if valores["-VER-"]:
            janela["-SENHA-"].update(password_char="")
        else:
            janela["-SENHA-"].update(password_char="*")
