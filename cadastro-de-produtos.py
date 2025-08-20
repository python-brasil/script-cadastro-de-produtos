# Lista para armazenar os produtos
estoque = []

# Função para adicionar produto
def adicionar_produto():
    nome = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade: "))
    produto = {"nome": nome, "quantidade": quantidade}
    estoque.append(produto)
    print("Produto adicionado com sucesso!\n")

# Função para listar produtos
def listar_produtos():
    if not estoque:
        print("Estoque vazio.\n")
    else:
        print("\n--- Estoque ---")
        for i, produto in enumerate(estoque):
            print(f"{i} - {produto['nome']} (Quantidade: {produto['quantidade']})")
        print()

# Função para atualizar produto
def atualizar_produto():
    listar_produtos()
    if estoque:
        indice = int(input("Digite o número do produto para atualizar: "))
        if 0 <= indice < len(estoque):
            novo_nome = input("Novo nome do produto: ")
            nova_quantidade = int(input("Nova quantidade: "))
            estoque[indice]["nome"] = novo_nome
            estoque[indice]["quantidade"] = nova_quantidade
            print("Produto atualizado com sucesso!\n")
        else:
            print("Índice inválido.\n")

# Função para deletar produto
def deletar_produto():
    listar_produtos()
    if estoque:
        indice = int(input("Digite o número do produto para deletar: "))
        if 0 <= indice < len(estoque):
            estoque.pop(indice)
            print("Produto deletado com sucesso!\n")
        else:
            print("Índice inválido.\n")

# Menu principal
def menu():
    while True:
        print("=== Menu ===")
        print("1 - Adicionar produto")
        print("2 - Listar produtos")
        print("3 - Atualizar produto")
        print("4 - Deletar produto")
        print("5 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            atualizar_produto()
        elif opcao == "4":
            deletar_produto()
        elif opcao == "5":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

# Executar programa
menu()
