def novo_contato():
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    email = input("Digite o email do contato: ")
    celular = input("Digite o celular do contato: ")
    endereco = input("Digite o endereço do contato: ")
    contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "celular": celular,
        "endereco": endereco,
    }
    return contato


def novo_contato_faker():
    from faker import Faker

    fake = Faker("pt_BR")
    nome = fake.name()
    telefone = fake.phone_number()
    email = fake.email()
    celular = fake.phone_number()
    endereco = fake.address()
    contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "celular": celular,
        "endereco": endereco,
    }
    return contato


def listar_contatos(agenda):
    for posicao, contato in enumerate(agenda):
        print(
            f"{posicao + 1} - Nome: {contato['nome']} - Telefone: {contato['telefone']} - Email: {contato['email']} - Celular: {contato['celular']} - Endereço: {contato['endereco']}"
        )


def remover_contato(posicao, agenda):
    if posicao > len(agenda):
        return 1  # codigo de erro caso queria apagar uma posicoao que nao existe
    else:
        contato = agenda.pop(posicao)
        return 0
