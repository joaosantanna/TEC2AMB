import pickle

agenda = []

while True:
    print(
        """
                    Agendinha - v 0.1
                    0 - sair
                    1 - novo contato
                    2 - listar contatos
                    3 - salvar dados
                    4 - ler dados
          """
    )
    op = int(input("->"))

    match op:

        case 0:
            print("bye bye ")
            break
        case 1:
            nome = input("Informe o nome:")
            telefone = input("Informe o telefone:")
            contato = {"nome": nome, "telefone": telefone}
            agenda.append(contato)
        case 2:
            for c in agenda:
                print(f"nome:{c['nome']} - Tel: {c['telefone']}")
        case 3:
            # salvar os dados no disco rigido
            with open("agenda.bin", "wb") as arquivo:
                pickle.dump(agenda, arquivo)
            print("Dados salvos com sucesso")

        case 4:
            # ler dados do disco
            with open("agenda.bin", "rb") as arquivo:
                agenda = pickle.load(arquivo)
            print("Dados carregados com sucesso")
        case _:
            print("Comando nao cadastrado")
