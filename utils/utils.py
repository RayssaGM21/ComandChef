import os
import platform
from tabulate import tabulate
from services.chatbot_service import iniciar_chatchef
from services.cliente_service import cadastrar_cliente, listar_clientes
from services.pedido_service import cadastrar_pedido, listar_fila, retirar_proximo_pedido
from services.prato_service import cadastrar_prato, listar_pratos, remover_prato
from services.promo_service import menu_promo
from dados import pratos, clientes, fila_pedidos, pratos_em_promocao


def limpar_terminal():
    sistema = platform.system().lower()

    if sistema == "windows":
        os.system("cls")
    else:
        os.system("clear")


def exibir_opcoes():
    print("""

░█████╗░░█████╗░███╗░░░███╗███╗░░░███╗░█████╗░███╗░░██╗██████╗░  ░█████╗░██╗░░██╗███████╗███████╗
██╔══██╗██╔══██╗████╗░████║████╗░████║██╔══██╗████╗░██║██╔══██╗  ██╔══██╗██║░░██║██╔════╝██╔════╝
██║░░╚═╝██║░░██║██╔████╔██║██╔████╔██║███████║██╔██╗██║██║░░██║  ██║░░╚═╝███████║█████╗░░█████╗░░
██║░░██╗██║░░██║██║╚██╔╝██║██║╚██╔╝██║██╔══██║██║╚████║██║░░██║  ██║░░██╗██╔══██║██╔══╝░░██╔══╝░░
╚█████╔╝╚█████╔╝██║░╚═╝░██║██║░╚═╝░██║██║░░██║██║░╚███║██████╔╝  ╚█████╔╝██║░░██║███████╗██║░░░░░
░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░  ░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░░░░
""")
    print("Bem vindo ao ComandChef. O seu restaurante preferido!!\n")
    menu = [
        ["1", "Cadastrar Cliente"],
        ["2", "Cadastrar Prato"],
        ["3", "Listar Clientes"],
        ["4", "Listar Pratos"],
        ["5", "Fazer Pedido"],
        ["6", "Retirar Próximo Pedido"],
        ["7", "Remover Prato"],
        ["8", "Ver fila de pedidos"],
        ["9", "Gerenciar promoções"],
        ["10", "Converse com o ChatChefBot"],
        ["b", "Voltar à Tela Anterior"],
        ["q", "Sair"]
    ]

    cabecalho_menu = ["Opção", "Descrição"]
    
    print(tabulate(menu, headers=cabecalho_menu, tablefmt="fancy_grid", numalign="center"))


def continuar():
    input("\nPressione Enter para voltar ao menu principal...")
    limpar_terminal()


def menu_principal():  
    while True:
        exibir_opcoes()
        escolha = input("\nDigite a opção desejada: ").strip().lower()

        match escolha:
            case "1":
                cadastrar_cliente()
            case "2":
                cadastrar_prato()
            case "3":
                listar_clientes()
            case "4":
                listar_pratos()
            case "5":
                cadastrar_pedido()
            case "6":
                retirar_proximo_pedido()
            case "7":
                listar_pratos()
                remover_prato()
            case "8":
                listar_fila()
            case "9":
                menu_promo()
            case "10":
                iniciar_chatchef(pratos, clientes, fila_pedidos, pratos_em_promocao.to_json())
            case "q":
                print("Saindo do sistema...")
                break
            case _:
                print("Opção inválida! Tente novamente!")

        continuar()