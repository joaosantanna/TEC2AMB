import PySimpleGUI as sg
from faker import Faker
from funcionalidades import limpar_campos, novo_contato, listar_nomes, buscar_contatos


sg.theme("LightGrey1")
f = Faker("pt_BR")
agenda = []

layout_esquerda = [
    [sg.Text("Agenda de Contatos", font=("Arial", 20))],
    [sg.Text("Nome:", size=(10, 1)), sg.InputText(key="-NOME-", size=(20, 1))],
    [sg.Text("Telefone:", size=(10, 1)), sg.InputText(key="-TELEFONE-", size=(20, 1))],
    [sg.Text("Email:", size=(10, 1)), sg.InputText(key="-EMAIL-", size=(20, 1))],
    [sg.Text("Endereço:", size=(10, 1)), sg.InputText(key="-ENDERECO-", size=(20, 1))],
    [sg.Button("Adicionar"), sg.Button("CriarContatoFake"), sg.Button("Sair")],
]


layout_direita = [
    [sg.Listbox(values=agenda, size=(15, 6), key="-LISTA-", enable_events=True)],
]

layout = [[sg.Column(layout_esquerda), sg.Column(layout_direita)]]

janela = sg.Window("Agenda de Contatos", layout, font=("Arial", 14))

while True:

    eventos, valores = janela.read()

    if eventos in (sg.WINDOW_CLOSED, "Sair"):
        break

    if eventos == "Adicionar":
        nome = valores["-NOME-"]
        telefone = valores["-TELEFONE-"]
        email = valores["-EMAIL-"]
        endereco = valores["-ENDERECO-"]
        novo_contato(agenda, nome, telefone, email, endereco)
        limpar_campos(janela)
        janela["-LISTA-"].update(values=listar_nomes(agenda))

    if eventos == "CriarContatoFake":
        nome = f.name()
        telefone = f.phone_number()
        email = f.email()
        endereco = f.address()
        janela["-NOME-"].update(nome)
        janela["-TELEFONE-"].update(telefone)
        janela["-EMAIL-"].update(email)
        janela["-ENDERECO-"].update(endereco)

    if eventos == "-LISTA-":
        nome = janela["-LISTA-"].get()
        contato = buscar_contatos(agenda, nome[0])
        janela["-NOME-"].update(contato["nome"])
        janela["-TELEFONE-"].update(contato["telefone"])
        janela["-EMAIL-"].update(contato["email"])
        janela["-ENDERECO-"].update(contato["endereco"])

janela.close()

# TODO:
# 1. Adicionar um botão para remover um contato da lista
# 2 . funcionalidade de update de contato
# 3 . rotinas para salvar/ler os dados em disco
# 4 . melhorar o design da aplicação
# 5. tirar o botao de contato fake e suas funcionalidade coorespondentes
