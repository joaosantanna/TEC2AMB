import PySimpleGUI as sg
from funcionalidade import gerar_senha


sg.theme("LightGrey1")

layout = [
    [sg.Text("Conta:", size=(10, 1)), sg.Input(key="-CONTA-", size=(35, 1))],
    [sg.Text("Usuário:", size=(10, 1)), sg.Input(key="-USUARIO-", size=(35, 1))],
    [
        sg.Text("Senha:", size=(10, 1)),
        sg.Input(key="-SENHA-", password_char="*", size=(35, 1)),
        sg.Checkbox("Ver", default=False, key="-VER-", enable_events=True),
    ],
    [
        sg.Text("Campos da Senha"),
        sg.Button("Gerar Senha"),
        sg.Spin(
            [i for i in range(6, 30)], initial_value=8, key="-TAMANHO-", size=(3, 1)
        ),
    ],
    [
        sg.Checkbox("Maiúsculas", default=True, key="-MAIUSCULAS-"),
        sg.Checkbox("Minúsculas", default=True, key="-MINUSCULAS-"),
        sg.Checkbox("Números", default=True, key="-NUMEROS-"),
        sg.Checkbox("Símbolos", default=False, key="-SIMBOLOS-"),
    ],
    [sg.Button("Cadastrar", size=(10, 1)), sg.Button("Sair", size=(10, 1))],
]

janela = sg.Window("Gerenciador de Senhas", layout, font=("Arial", 14))
while True:

    evento, valores = janela.read()

    if evento in ("Sair", sg.WIN_CLOSED):
        break
    if evento == "-VER-":  # EVENTO PEGA PELA CHAVE DO CHECKBOX
        if valores["-VER-"]:
            janela["-SENHA-"].update(password_char="")
        else:
            janela["-SENHA-"].update(password_char="*")
    if evento == "Gerar Senha":
        maiusculas = valores["-MAIUSCULAS-"]
        minusculas = valores["-MINUSCULAS-"]
        numeros = valores["-NUMEROS-"]
        simbolos = valores["-SIMBOLOS-"]
        tamanho = valores["-TAMANHO-"]
        senha = gerar_senha(tamanho, maiusculas, minusculas, numeros, simbolos)
        janela["-SENHA-"].update(senha)

janela.close()
