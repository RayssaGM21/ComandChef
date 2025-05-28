from entidades.pedido import Pedido
from entidades.cliente import Cliente
from .cliente_service import listar_clientes, verificar_cliente_existente
from .prato_service import listar_pratos
from dados import clientes, fila_pedidos, pratos, historico_pedidos_retirados, pedidos_visitados_recentemente
from tabulate import tabulate
import time



def cadastrar_pedido():
    print("Escolha um cliente para fazer este pedido")
    listar_clientes()

    while True:
        id_cliente = input("Id: ").strip()

        try:
            id_cliente_int = int(id_cliente)
        except ValueError:
            print("ID inválido, deve ser um número. Tente novamente.")
            continue 

        if not verificar_cliente_existente(id_cliente_int):
            print("ID do cliente não encontrado, tente novamente.")
        else:
            break

    print("Escolha os Pratos do Pedido - Digite 'Sair' para finalizar")

    id_prato = ""
    escolhidos = []

    listar_pratos()
    while True:
        id_prato = input("Id do prato: ")

        if id_prato.lower() == "sair":
            break

        try:
            id_prato_int = int(id_prato)
            prato_valido = False
            for prato in pratos:
                if prato["id"] == id_prato_int:
                    escolhidos.append({
                        "nome": prato["nome"],
                        "preco": prato["preco"],
                        "ingredientes": prato["ingredientes"]
                    })
                    prato_valido = True
                    break

            if not prato_valido:
                print("ID inválido! O prato com esse ID não existe.")
        except ValueError:
            print("Entrada inválida! Por favor, insira um número de ID válido.")

    cliente = None
    for i in clientes:
        if i["id"] == int(id_cliente):
            cliente = Cliente(i["nome"])
            break

    if cliente is None:
        print("Cliente não encontrado!")
        return

    pedido = Pedido(cliente, escolhidos)
    fila_pedidos.append(pedido)

    print("\nPedido feito com sucesso!\n")

    exibir_pedido(pedido)

    posicao = len(fila_pedidos) - 1
    if posicao == 0:
        print("Há 0 Pedidos na frente, logo poderá ser retirado!")
    else:
        print(f"Há {posicao} Pedidos na frente, aguarde e logo poderá ser retirado.")



def retirar_proximo_pedido():
    if fila_pedidos:
        pedido = fila_pedidos.popleft()
        pratos_string = ', '.join([p["nome"] for p in pedido.pratos])
        
        dados = [[pedido.cliente.nome, f"R$ {pedido.valor_total:.2f}", pratos_string]]
        cabecalho = ["Nome", "Preço", "Pratos"]
        colalign = ('left', 'right', 'left')

        simular_preparo(pedido)

        print("╔════════════════════════════════════════════════╗")
        print("║               Pedido retirado!                 ║")
        print("╚════════════════════════════════════════════════╝")
        
        print(tabulate(dados, headers=cabecalho, tablefmt="fancy_grid", colalign=colalign))
        historico_pedidos_retirados.append(pedido)
        
    else:
        print("Não há pedidos para serem retirados. :(")


def listar_fila():
    if not fila_pedidos:
        print("Não há pedidos na fila.")
        return
    
    dados = []
    for pedido in fila_pedidos:
        nome_cliente = pedido.cliente.nome
        pratos = ", ".join([prato['nome'] for prato in pedido.pratos])
        total = sum(prato['preco'] for prato in pedido.pratos)
        dados.append([nome_cliente, pratos, f"R${total:.2f}"])
    
    cabecalho = ["Cliente", "Pratos", "Total"]
    colalign = ('left', 'left', 'right')

    print("Lista de Pedidos na Fila:")
    print(tabulate(dados, headers=cabecalho, tablefmt="fancy_grid", colalign=colalign))


def exibir_pedido(pedido: Pedido, add_historico=True):
    dados = []
    for prato in pedido.pratos:
        dados.append([prato['nome'], f"R${prato['preco']:.2f}"])

    total = sum(prato['preco'] for prato in pedido.pratos)
    dados.append(["", f"Total: R${total:.2f}"])
    cabecalho = ["Prato", "Preço"]

    colalign = ('left', 'right')
    print(f"Cliente: {pedido.cliente.nome}")
    print("Pratos escolhidos:")
    print(tabulate(dados, headers=cabecalho, tablefmt="fancy_grid", colalign=colalign))
    if add_historico:
        pedidos_visitados_recentemente.append(pedido)


def simular_preparo(pedido):

    print(f"Preparando o pedido de {pedido.cliente.nome}")
    time.sleep(2)
    for prato in pedido.pratos:
        for i in prato['ingredientes']:
            print(f"Colocando/Preparando {i}")
            time.sleep(2)
    print("Colocando tudo no seu devido lugar e.......... PRONTO")


def voltar_ao_ultimo_pedido_visualizado():
    if len(pedidos_visitados_recentemente) >= 1:
        pedido_atual = pedidos_visitados_recentemente.pop()
        print("Voltando ao último pedido visualizado...")
        exibir_pedido(pedido_atual, False)  
    else:
        print("Não há pedidos no histórico de visualização para voltar.")