from dados import pratos_em_promocao, pratos
from estruturas.linked_list import Node
from tabulate import tabulate
from services.prato_service import listar_pratos
import time

def adicionar_promocao(id_prato_original: int, nome_promocao: str, preco_promocional: float) -> dict | None:
    prato_original_encontrado = None
    for p in pratos:
        if p.get('id') == id_prato_original:
            prato_original_encontrado = p
            break
    
    if prato_original_encontrado is None:
        print(f"Prato com ID {id_prato_original} não encontrado para criar a promoção!")
        return None

    if not isinstance(preco_promocional, (int, float)) or preco_promocional <= 0:
        print("O preço promocional deve ser um número positivo válido!")
        return None

    novo_prato_promocional_data = {
        "id": pratos_em_promocao.proximo_id(),
        "nome": nome_promocao.strip(),
        "preco_promocional": preco_promocional,
        "original_id": id_prato_original
    }

    try:
        pratos_em_promocao.add_last(Node(novo_prato_promocional_data))
        print(f"Promoção '{nome_promocao}' para '{prato_original_encontrado['nome']}' adicionada com sucesso por R$ {preco_promocional:.2f}!")
        return novo_prato_promocional_data
    except:
        print(f"Erro ao adicionar promoção!")
        return None


def remover_promocao(identificador_promocao: str) -> dict | None:
    if not pratos_em_promocao.head:
        print("Não há promoções cadastradas para remover.")
        return None

    target_node = None
    identificador_promocao = identificador_promocao.strip()
    
    try:
        identificador_numerico = int(identificador_promocao)
        id_procurado = True

    except ValueError:
        identificador_numerico = None
        id_procurado = False

    for node in pratos_em_promocao:
        if node is None or node.data is None:
            continue 

        if id_procurado:
            if node.data.get('id') == identificador_numerico:
                target_node = node
                break
        else:
            if node.data.get('nome', '').lower() == identificador_promocao.lower():
                target_node = node
                break

    if target_node:
        try:
            removido_data = pratos_em_promocao.remove(target_node) 
            print(f"Promoção '{removido_data['nome']}' removida com sucesso!")
            return removido_data
        except:
            print(f"Erro ao remover promoção!")
            return None
    else:
        print(f"Promoção '{identificador_promocao}' não encontrada!")
        return None


def listar_promocoes():
    if not pratos_em_promocao.head:
        print("Não há promoções cadastradas no momento.")
        return

    dados = []
    for prato_promo_node in pratos_em_promocao:
        if prato_promo_node and prato_promo_node.data:
            dados.append([
                prato_promo_node.data["id"],
                prato_promo_node.data["nome"],
                f"R$ {prato_promo_node.data.get('preco_promocional', 0.0):.2f}"
            ])

    if dados:
        cabecalho = ["ID da Promoção", "Nome da Promoção", "Preço Promocional"]
        colalign = ('right', 'left', 'right')
        print("\nLista de Promoções")
        print(tabulate(dados, headers=cabecalho, tablefmt="fancy_grid", colalign=colalign))
    else:
        print("Nenhuma promoção para listar!")


def exibir_opcoes_promo():
    print("\nGerenciamento de Promoções Command Chef\n")
    menu = [
        ["1", "Adicionar Nova Promoção"],
        ["2", "Remover Promoção Existente"],
        ["3", "Listar Todas as Promoções"],
        ["q", "Voltar ao Menu Principal"]
    ]

    cabecalho_menu = ["Opção", "Descrição"]
    
    print(tabulate(menu, headers=cabecalho_menu, tablefmt="fancy_grid", numalign="center"))


def menu_promo():
    while True:
        time.sleep(2)
        exibir_opcoes_promo()
        escolha = input("Digite a opção desejada: ").strip().lower()
        match escolha:
            case "1":
                print("\n--- Adicionar Promoção ---")
                listar_pratos()
                try:
                    id_prato_original_str = input("Digite o ID do prato original para a promoção: ").strip()
                    id_prato_original = int(id_prato_original_str)

                    nome_promocao = input("Digite o nome da nova promoção: ").strip()
                    if not nome_promocao:
                        print("O nome da promoção não pode ser vazio!")
                        continue

                    preco_promocional_str = input("Digite o preço promocional (Ex: 19.99): R$ ").strip().replace(',', '.')
                    preco_promocional = float(preco_promocional_str)
                    
                    adicionar_promocao(id_prato_original, nome_promocao, preco_promocional)
                except ValueError:
                    print("Entrada inválida!")
                except:
                    print(f"Ocorreu um erro!")

            case "2":
                print("\n--- Remover Promoção ---")
                if not pratos_em_promocao.head:
                    print("Não há promoções para remover no momento.")
                    continue
                listar_promocoes()
                identificador = input("Digite o id ou nome da promoção a ser removida: ").strip()
                if not identificador:
                    print("O identificador da promoção não pode ser vazio.")
                    continue
                remover_promocao(identificador)

            case "3":
                print("\n--- Lista de Promoções ---")
                listar_promocoes()

            case "q":
                print("Voltando ao Menu Principal...")
                break

            case _:
                print("Opção inválida! Por favor, escolha uma das opções listadas.")