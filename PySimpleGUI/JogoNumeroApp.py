from random import randint
import PySimpleGUI as sg

sg.theme("LightGrey1")
segredo = randint(1, 100)
tentativas = 0

layout = [
    [sg.Push(), sg.Image(source="PySimpleGUI/Number-Guessing-Game.png"), sg.Push()],
    [sg.Push(), sg.Text("Adivinhe o número secreto", font=("Currier", 20)), sg.Push()],
    [sg.Text("Chute um número entre 1 e 100", key="-MENSAGEM-")],
    [
        sg.Text("Número:", size=(10, 1), key="-CHUTE-"),
        sg.InputText(key="-NUM-", size=(15, 1)),
    ],
    [sg.Button("Chutar", size=(10, 1)), sg.Button("Sair", size=(10, 1))],
]

janela = sg.Window("Jogo do Número Secreto", layout, font=("Currier", 14))

while True:
    botao, valores = janela.Read()
    if botao in ("Sair", sg.WIN_CLOSED):
        break
    if botao == "Chutar":
        chute = int(valores["-NUM-"])
        if chute == segredo:
            sg.popup(
                f"Parabéns, você acertou! \n em {tentativas} tentativas",
                font=("Currier", 14),
            )
            break
        else:
            tentativas += 1
            janela["-CHUTE-"].Update(f"Numero: {chute}")
            if chute > segredo:
                janela["-MENSAGEM-"].Update("Tente um número menor")
            else:
                janela["-MENSAGEM-"].Update("Tente um número maior")
janela.close()
