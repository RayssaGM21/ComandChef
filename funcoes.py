from entidades import Cliente, Prato, Pedido
from collections import deque
import time


fila_pedidos = deque()

# def cadastrar_Cliente():
#     atulizar_contador_cliente()

#     while True:
#         nome = input("Nome do Cliente: ").strip ()
#         if nome:
#             break
#         else:
#             print("Nome do Cliente não pode ser vazio.")
    
#     cliente = Cliente(nome)
#     clientes.append({
#         "id": cliente.id,
#         "nome": cliente.nome,
#         "pedidos": cliente.pedidos
#     })

# def atulizar_contador_cliente():
#     if clientes:
#         maior_id = max(i["id"] for i in clientes)
#         Cliente.contador_id = maior_id

# def atualizar_contador_prato():
#     if pratos:
#         maior_id = max(i["id"] for i in pratos)
#         Prato.contador_id = maior_id

# def cadastrar_Prato():
    # atualizar_contador_prato()

    # while True:
    #     nome = input("Nome do Prato: ").strip()
    #     if nome:
    #         break
    #     else:
    #         print("O nome do Prato não pode ser vazio.")
    

    # while True:
    #     preco_string = input("Preço: ").strip()
        
    #     try:
    #         preco = float(preco_string)
    #         if preco >0:
    #             break
    #         else:
    #             print("O preço do Prato deve ser maior que zero")
    #     except ValueError:
    #         print("Preço digitado inválido. Digite algo semelhante a '10.99' ")
            
    # print("Digite os ingredientes, quando acabar digite 'Sair'")

    # ingredientes = [] 
    # while True:
    #         ingrediente = input(":").strip()
    #         if ingrediente.lower() == "sair":
    #             break
    #         if ingrediente == "":
    #             print("O nome do ingrediente não pode ser vazio.")
    #             continue
    #         ingredientes.append(ingrediente)

    
    # ingredientes = tuple(ingredientes)

    # prato = Prato(nome, preco, ingredientes)
    # pratos.append(
    #     {
    #         "id": prato.id,
    #         "nome": prato.nome,
    #         "preco": prato.preco,
    #         "ingredientes": prato.ingredientes
    #     }
    # )

# def cadastrar_Pedido():
#     print("Escolha um cliente para fazer este pedido")
#     listar_Clientes()

#     idCliente = input("Id: ")
#     print("Escolha os Pratos do Pedido - Digite 'Sair' para finalizar")

#     idPrato = ""
#     escolhidos = []

#     while idPrato.lower() != "sair":
#         listar_Pratos()
#         idPrato = input("Id: ")

#         if idPrato.lower() != "sair":
#             for i in pratos:
#                 if i['id'] == int(idPrato):
#                     escolhidos.append({
#                         "nome": i['nome'],
#                         "preco": i["preco"]
#                     })

#     cliente = None
#     for i in clientes:
#         if i["id"] == int(idCliente):
#             cliente = Cliente(i["nome"])

#     pedido = Pedido(cliente, escolhidos)
#     fila_pedidos.append(pedido)

#     print("Pedido feito com sucesso!")
#     posicao = list(fila_pedidos).index(pedido)
#     if fila_pedidos.count == 1:
#         print("Há 0 Pedidos na frente, logo poderá ser retirado!")
#     else:
#         print(f"Há {posicao} Pedidos na frete, aguarde e logo poderá ser retirado.")


# def listar_Clientes():
#     print("╔════╦════════════════════════╗")
#     print("║ ID ║ Nome                   ║")
#     print("╠════╬════════════════════════╣")
#     for c in clientes:
#         print(f"║ {c['id']:<2} ║ {c['nome']:<22} ║")
#     print("╚════╩════════════════════════╝")

# def listar_Pratos():
#     print("╔══════╦══════════════════════════════════════════╦════════════╦═══════════════════════════════════════════════════════════════════════════════════════╗")
#     print("║ ID   ║ Nome                                     ║ Preço      ║ Ingredientes                                                                          ║")
#     print("╠══════╬══════════════════════════════════════════╬════════════╬═══════════════════════════════════════════════════════════════════════════════════════╣")
#     for c in pratos:
#         ingredientes_str = ", ".join(c["ingredientes"])
#         print(f"║ {str(c['id']):<4} ║ {c['nome']:<40} ║ R$ {float(c['preco']):<7.2f} ║ {ingredientes_str:<85} ║")
#     print("╚══════╩══════════════════════════════════════════╩════════════╩═══════════════════════════════════════════════════════════════════════════════════════╝")

# def retirar_proximo_pedido():
#     if fila_pedidos:
#         pedido = fila_pedidos.popleft()
#         pratos_string = ', '.join([p["nome"] for p in pedido.pratos])
#         print("╔════════════════════════════════════════════════╗")
#         print("║               Pedido retirado!                 ║")
#         print("╚════════════════════════════════════════════════╝")
#         print("╔══════════════════════╦════════════╦═══════════════════════════════════════════════════════════════════════════════════════╗")
#         print("║ Nome                 ║ Preço      ║ Pratos                                                                                ║")
#         print("╠══════════════════════║════════════║═══════════════════════════════════════════════════════════════════════════════════════╣")
#         print(f"║ {pedido.cliente.nome:<21}║ R${pedido.valor_total:<9}║ {pratos_string:<90} ║")
#         print("╚══════════════════════╩════════════╩════════════════════════════════════════╝")
#     else:
#         print("Não há pedidos para serem retirados. :(")

def menu_Principal():
    i = True
    while i != False:
        print("Bem vindo ao ComandChef. O seu restaurante preferido!!")
        time.sleep(2)
        print("""
======= Menu =======
1 - Cadastrar Cliente
2 - Cadastrar Prato
3 - Listar Pratos
4 - Listar Clientes
5 - Remover Prato
6 - Fazer pedido
7 - Retirar próximo Pedido
q - Sair
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

        elif escolha == "q":
            i = False


