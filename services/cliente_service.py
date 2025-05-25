from entidades.cliente import Cliente
from dados import clientes
from tabulate import tabulate

def atualizar_contador_cliente():
    if clientes:
        maior_id = max(i["id"] for i in clientes)
        Cliente.contador_id = maior_id

def cadastrar_cliente():
    atualizar_contador_cliente()

    while True:
        nome = input("Nome do Cliente: ").strip ()
        if nome:
            break
        else:
            print("Nome do Cliente não pode ser vazio.")
    
    cliente = Cliente(nome)
    clientes.append({
        "id": cliente.id,
        "nome": cliente.nome,
        "pedidos": cliente.pedidos
    })


def listar_clientes():
    dados = [[c["id"], c["nome"]] for c in clientes]
    cabecalho = ["ID", "Nome"]
    print(tabulate(dados, headers=cabecalho, tablefmt="fancy_grid", numalign="right", stralign="left"))


def buscar_cliente_por_id(id_cliente: int):
    for cliente in clientes:
        if cliente.id == id_cliente:
            return cliente
    return None

def verificar_cliente_existente(id_cliente: int):
    for cliente in clientes:
        if cliente["id"] == id_cliente:
            return True
    return False
