from entidades import Cliente, Prato, Pedido

def cadastrar_Cliente(clientes):
    nome = input("Nome do Cliente: ")
    cliente = Cliente(nome)
    clientes.append({
        "id": cliente.id,
        "nome": cliente.nome,
        "pedidos": cliente.pedidos
    })

def cadastrar_Prato(pratos):
    nome = input("Nome do Prato: ")
    preco = input("Preço: ")
    print("Digite os ingredientes, quando acabar digite 'Sair'")

    ingredientes = []
    ingrediente = ""
    while ingrediente.lower() != "sair":
        
        ingrediente = input(":")
        if ingrediente.lower() != "sair":
            ingredientes.append(ingrediente)

    
    ingredientes = tuple(ingredientes)

    prato = Prato(nome, preco, ingredientes)
    pratos.append(
        {
            "id": prato.id,
            "nome": prato.nome,
            "preco": prato.preco,
            "ingredientes": prato.ingredientes
        }
    )
