def novo_contato(agenda, nome, telefone, email, endereco):
    contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "endereco": endereco,
    }
    agenda.append(contato)
    return 0  # codigo de erro caso nao tenha erro


def buscar_contatos(agenda, nome):
    for posicao, contato in enumerate(agenda):
        if contato["nome"] == nome:
            return agenda[posicao]
    return -1  # codigo de erro caso nao encontre o contato


def remover_contato(posicao, agenda):
    if posicao > len(agenda):
        return 1  # codigo de erro caso queria apagar uma posicoao que nao existe
    else:
        contato = agenda.pop(posicao)
        return 0


def limpar_campos(janela):
    janela["-NOME-"].update("")
    janela["-TELEFONE-"].update("")
    janela["-EMAIL-"].update("")
    janela["-ENDERECO-"].update("")


def listar_nomes(agenda):
    nomes = []
    for contato in agenda:
        nomes.append(contato["nome"])
    return nomes
