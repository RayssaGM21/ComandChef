from entidades.prato import Prato
from dados import pratos
from tabulate import tabulate

def atualizar_contador_prato():
    if pratos:
        maior_id = max(i["id"] for i in pratos)
        Prato.contador_id = maior_id

def cadastrar_prato():
    atualizar_contador_prato()

    while True:
        nome = input("Nome do Prato: ").strip()
        if nome:
            break
        else:
            print("O nome do Prato não pode ser vazio.")
    

    while True:
        preco_string = input("Preço: ").strip()
        
        try:
            preco = float(preco_string)
            if preco > 0:
                break
            else:
                print("O preço do Prato deve ser maior que zero")
        except ValueError:
            print("Preço digitado inválido. Digite algo semelhante a '10.99' ")
            
    print("Digite os ingredientes, quando acabar digite 'Sair'")

    ingredientes = set()
    while True:
            ingrediente = input(":").strip()
            if ingrediente.lower() == "sair":
                break
            if ingrediente == "":
                print("O nome do ingrediente não pode ser vazio.")
                continue
            ingredientes.add(ingrediente)

    
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

def listar_pratos():
    dados = []
    for c in pratos:
        dados.append([c["id"], c["nome"], f"R$ {c['preco']:.2f}", ", ".join(c["ingredientes"])])

    cabecalho = ["ID", "Nome", "Preço", "Ingredientes"]
    colalign = ('right', 'left', 'right', 'left')
    print(tabulate(dados, headers=cabecalho, tablefmt="fancy_grid", colalign=colalign))


def buscar_prato_por_id(id_prato: int):
    for prato in pratos:
        if prato.id == id_prato:
            return prato
    return None


def remover_prato():
    id_prato = input("Digite o ID do prato que deseja remover: ").strip()
    global pratos

    try:
        id_prato = int(id_prato)
    except ValueError:
        print("ID inválido! Por favor, insira um número válido.")
        return
    
    prato_existente = None
    for prato in pratos:
        if prato["id"] == id_prato:
            prato_existente = prato
            break

    if prato_existente is None:
        print(f"Não existe prato com o ID {id_prato}.")
    else:
        pratos = [p for p in pratos if p["id"] != id_prato]
        print(f"Prato com ID {id_prato} removido com sucesso!")
