from entidades.pedido import Pedido
from entidades.cliente import Cliente
from .cliente_service import listar_clientes
from .prato_service import listar_pratos
from dados import clientes
from dados import pratos
from collections import deque
from tabulate import tabulate

fila_pedidos = deque()

def cadastrar_pedido():
    print("Escolha um cliente para fazer este pedido")
    listar_clientes()

    id_cliente = input("Id: ")
    print("Escolha os Pratos do Pedido - Digite 'Sair' para finalizar")

    id_prato = ""
    escolhidos = []

    while id_prato.lower() != "sair":
        listar_pratos()
        id_prato = input("Id: ")

        if id_prato.lower() != "sair":
            for i in pratos:
                if i['id'] == int(id_prato):
                    escolhidos.append({
                        "nome": i['nome'],
                        "preco": i["preco"]
                    })

    cliente = None
    for i in clientes:
        if i["id"] == int(id_cliente):
            cliente = Cliente(i["nome"])

    pedido = Pedido(cliente, escolhidos)
    fila_pedidos.append(pedido)

    print("Pedido feito com sucesso!")
    posicao = list(fila_pedidos).index(pedido)
    if len(fila_pedidos) == 1:
        print("Há 0 Pedidos na frente, logo poderá ser retirado!")
    else:
        print(f"Há {posicao} Pedidos na frete, aguarde e logo poderá ser retirado.")


def retirar_proximo_pedido():
    if fila_pedidos:
        pedido = fila_pedidos.popleft()
        pratos_string = ', '.join([p["nome"] for p in pedido.pratos])
        
        dados = [[pedido.cliente.nome, f"R$ {pedido.valor_total:.2f}", pratos_string]]
        cabecalho = ["Nome", "Preço", "Pratos"]
        colalign = ('left', 'right', 'left')
        
        print("╔════════════════════════════════════════════════╗")
        print("║               Pedido retirado!                 ║")
        print("╚════════════════════════════════════════════════╝")
        
        print(tabulate(dados, headers=cabecalho, tablefmt="fancy_grid", colalign=colalign))
        
    else:
        print("Não há pedidos para serem retirados. :(")


def listar_fila():
    return list(fila_pedidos)
