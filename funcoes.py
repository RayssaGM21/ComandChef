from entidades import Cliente, Prato, Pedido
from collections import deque
import time

clientes = [
    {"id": 1, "nome": "Matheus", "pedidos": []},
    {"id": 2, "nome": "Rayssa", "pedidos": []},
    {"id": 3, "nome": "Rodrigo", "pedidos": []}
]

pratos = [
    {
        "id": 1,
        "nome": "Espaguete ao Alho e Óleo",
        "preco": 22.50,
        "ingredientes": ("macarrão", "alho", "azeite", "salsinha")
    },
    {
        "id": 2,
        "nome": "Frango Xadrez",
        "preco": 29.90,
        "ingredientes": ("frango", "pimentão", "cebola", "molho shoyu", "amendoim")
    },
    {
        "id": 3,
        "nome": "Pizza Margherita",
        "preco": 34.00,
        "ingredientes": ("massa", "molho de tomate", "muçarela", "manjericão")
    },
    {
        "id": 4,
        "nome": "Risoto de Cogumelos",
        "preco": 100.80,
        "ingredientes": ("arroz arbório", "champignon", "parmesão", "cebola", "creme de leite")
    },
    {
        "id": 19,
        "nome": "Hambúrguer Artesanal",
        "preco": 27.50,
        "ingredientes": ("pão brioche", "carne angus", "queijo cheddar", "alface", "tomate", "maionese caseira")
    }
]
fila_pedidos = deque()

def cadastrar_Cliente():
    nome = input("Nome do Cliente: ")
    cliente = Cliente(nome)
    clientes.append({
        "id": cliente.id,
        "nome": cliente.nome,
        "pedidos": cliente.pedidos
    })

def cadastrar_Prato():
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

def cadastrar_Pedido():
    print("Escolha um cliente para fazer este pedido")
    listar_Clientes()

    idCliente = input("Id: ")
    print("Escolha os Pratos do Pedido - Digite 'Sair' para finalizar")

    idPrato = ""
    escolhidos = []

    while idPrato.lower() != "sair":
        listar_Pratos()
        idPrato = input("Id: ")

        if idPrato.lower() != "sair":
            for i in pratos:
                if i['id'] == int(idPrato):
                    escolhidos.append({
                        "nome": i['nome'],
                        "preco": i["preco"]
                    })

    cliente = None
    for i in clientes:
        if i["id"] == int(idCliente):
            cliente = Cliente(i["nome"])

    pedido = Pedido(cliente, escolhidos)
    fila_pedidos.append(pedido)

    print("Pedido feito com sucesso!")
    posicao = list(fila_pedidos).index(pedido)
    if fila_pedidos.count == 1:
        print("Há 0 Pedidos na frente, logo poderá ser retirado!")
    else:
        print(f"Há {posicao} Pedidos na frete, aguarde e logo poderá ser retirado.")


def listar_Clientes():
    print("╔════╦════════════════════════╗")
    print("║ ID ║ Nome                   ║")
    print("╠════╬════════════════════════╣")
    for c in clientes:
        print(f"║ {c['id']:<2} ║ {c['nome']:<22} ║")
    print("╚════╩════════════════════════╝")

def listar_Pratos():
    print("╔══════╦══════════════════════════════════════════╦════════════╦═══════════════════════════════════════════════════════════════════════════════════════╗")
    print("║ ID   ║ Nome                                     ║ Preço      ║ Ingredientes                                                                          ║")
    print("╠══════╬══════════════════════════════════════════╬════════════╬═══════════════════════════════════════════════════════════════════════════════════════╣")
    for c in pratos:
        ingredientes_str = ", ".join(c["ingredientes"])
        print(f"║ {str(c['id']):<4} ║ {c['nome']:<40} ║ R$ {float(c['preco']):<7.2f} ║ {ingredientes_str:<85} ║")
    print("╚══════╩══════════════════════════════════════════╩════════════╩═══════════════════════════════════════════════════════════════════════════════════════╝")

def retirar_proximo_pedido():
    pedido = fila_pedidos.popleft()
    print("╔════════════════════════════════════════════════╗")
    print("║               Pedido retirado!                 ║")
    print("╚════════════════════════════════════════════════╝")
    print("╔══════════════════════╦════════════╦═══════════════════════════════════════════════════════════════════════════════════════╗")
    print("║ Nome                 ║ Preço      ║ Pratos                                                                                ║")
    print("╠══════════════════════║════════════║═══════════════════════════════════════════════════════════════════════════════════════╣")
    print(f"║{pedido.cliente.nome:<22}║R${pedido.valor_total:<13}║{pedido.pratos:<50}║")
    print("╚═════")

def menu_Principal():
    i = True
    while i != False:
        print("Bem vindo ao ComandChef. O seu restaurante preferido!!")
        time.sleep(2)
        print("""
                ======= MENU =======
                1 - Cadastrar Cliente
                2 - Cadastrar Prato
                3 - Listar Pratos
                4 - Listar Clientes
                5 - Remover Prato
                6 - Fazer pedido
                7 - Retirar próximo Pedido
                8 - Null
                9 - Null 
                10 - Sair
                ====================
                                    """)
        print(" ")
        escolha = input ("Digite a opção desejada: ")
        
        if escolha == "1":
            cadastrar_Cliente()

        elif escolha == "2":
            cadastrar_Prato()

        elif escolha == "3":
            listar_Pratos()

        elif escolha == "4":
            listar_Clientes()

        elif escolha == "5":
            remover_Prato()

        elif escolha == "6":
            cadastrar_Pedido()
        elif escolha == "7":
            retirar_proximo_pedido()

        elif escolha == "10":
            i = False


