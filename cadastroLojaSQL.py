def validar_nome(nome):
    if not nome.strip():
        print("O nome do produto não pode ser vazio.")
        return False
    return True

def validar_preco(preco):
    try:
        preco = float(preco)
        if preco <= 0:
            print("O preço deve ser um número positivo.")
            return False
        return True
    except ValueError:
        print("O preço deve ser um número válido.")
        return False

def validar_quantidade(quantidade):
    try:
        quantidade = int(quantidade)
        if quantidade <= 0:
            print("A quantidade deve ser um número inteiro positivo.")
            return False
        return True
    except ValueError:
        print("A quantidade deve ser um número inteiro válido.")
        return False

def validar_id(id):
    try:
        id = int(id)
        if id <= 0:
            print("O ID deve ser um número inteiro positivo.")
            return False
        return True
    except ValueError:
        print("O ID deve ser um número inteiro válido.")
        return False

def adicionar_produto(loja):
    print("\nAdicionar Produto:")
    nome = input("Nome do produto: ")
    if not validar_nome(nome):
        return

    preco = input("Preço do produto: ")
    if not validar_preco(preco):
        return

    quantidade = input("Quantidade do produto: ")
    if not validar_quantidade(quantidade):
        return

    produto = {
        'id': loja['proximo_id'],
        'nome': nome,
        'preco': float(preco),
        'quantidade': int(quantidade)
    }
    loja['produtos'].append(produto)
    print(f"Produto {nome} adicionado com sucesso!")
    loja['proximo_id'] += 1

def listar_produtos(loja):
    print("\nLista de Produtos:")
    if not loja['produtos']:
        print("Nenhum produto cadastrado.")
    else:
        for produto in loja['produtos']:
            print(f"ID: {produto['id']}, Nome: {produto['nome']}, Preço: {produto['preco']}, Quantidade: {produto['quantidade']}")

def remover_produto(loja):
    print("\nRemover Produto:")
    id = input("ID do produto a ser removido: ")
    if not validar_id(id):
        return

    quantidade = input("Quantidade a ser removida: ")
    if not validar_quantidade(quantidade):
        return

    id = int(id)
    quantidade = int(quantidade)

    for produto in loja['produtos']:
        if produto['id'] == id:
            if produto['quantidade'] >= quantidade:
                produto['quantidade'] -= quantidade
                print(f"{quantidade} unidades do produto com ID {id} removidas com sucesso!")
                if produto['quantidade'] == 0:
                    loja['produtos'].remove(produto)
                return
            else:
                print(f"Quantidade insuficiente de produto com ID {id}.")
                return
    print(f"Produto com ID {id} não encontrado.")

# Função principal para interação com o usuário
def geral():
    loja = {
        'produtos': [],
        'proximo_id': 1
    }

    while True:
        print("\n===== Sistema de Loja =====")
        print("1. Adicionar Produto")
        print("2. Listar Produtos")
        print("3. Remover Produto")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_produto(loja)
        elif opcao == '2':
            listar_produtos(loja)
        elif opcao == '3':
            remover_produto(loja)
        elif opcao == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Escolha novamente.")

geral()
