import pickle
import os
from funcionalidades import novo_contato, listar_contatos, remover_contato


agenda = []

if os.path.isfile("agenda.db"):
    with open("agenda.db", "rb") as file:
        agenda = pickle.load(file)


while True:

    print(
        """
            Agenda de Contatos

            0 - sair
            1 - adicionar contato
            2 - listar contatos
            3 - editar contato 
            4 - excluir contato
            5 - salvar dados
        """
    )

    op = int(input("Digite a opção desejada: "))

    match op:

        case 0:
            print("Saindo...")
            break
        case 1:
            # criar novo contato
            contato = novo_contato()
            agenda.append(contato)
            print("Contato adicionado com sucesso!")

        case 2:
            # listar contatos
            listar_contatos(agenda)

        case 4:
            # excluir contato
            posicao = int(input("Digite a posição do contato que deseja excluir: "))
            remover_contato(posicao - 1, agenda)

        case 5:
            with open("agenda.db", "wb") as file:
                pickle.dump(agenda, file)
            print("Dados salvos com sucesso!")

        case _:
            print("Opção inválida")

# TODO
"""
- corrigir o uso do faker 
- implementar a rotina de update de dados
"""
