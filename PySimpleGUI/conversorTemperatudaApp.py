import PySimpleGUI as sg

# desenho da janela
sg.theme("LightGrey1")  # Add a touch of color

layout = [
    [sg.Text("Conversor de temperatura - Celsius x Fahrenheit", font=("Currier", 18))],
    [
        sg.Text("Valor"),
        sg.InputText(key="-VALOR-", size=(6, 1)),
        sg.Combo(["Celcius", "Fahrenheit"], default_value="Celcius", key="-OPCAO-"),
    ],
    [sg.Text("Resultado:", key="-RESULTADO-")],
    [sg.Button("Converter", size=(10, 1)), sg.Button("Sair", size=(10, 1))],
]

janela = sg.Window("Conversor de Temperatura", layout, font=("Currier", 14))


# comportamento
while True:
    botao, valores = janela.Read()
    if botao in ("Sair", sg.WIN_CLOSED):
        break
    if botao == "Converter":
        valor = float(valores["-VALOR-"])
        # print(f"valor : {valor}")
        # print(valores)
        if valores["-OPCAO-"] == "Fahrenheit":
            # coonverter valor para Fahrenheit
            F = valor * 1.8 + 32
            # print(f"{valor} celcius = {F} Fahrenheit")
            janela["-RESULTADO-"].Update(f"{valor:.2F} celcius = {F:.2F} Fahrenheit")
        else:
            # converter valor para Celcius
            C = (valor - 32) * 5 / 9
            # print(f"{valor} Fahrenheit = {C} Celcius")
            janela["-RESULTADO-"].Update(f"{valor:.2F} Fahrenheit = {C:.2F} Celcius")

janela.close()
