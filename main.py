import time
from services.cliente_service import cadastrar_cliente, listar_clientes
from services.pedido_service import cadastrar_pedido, retirar_proximo_pedido
from services.prato_service import cadastrar_prato, listar_pratos, remover_prato

def menu_principal():
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
            cadastrar_cliente()

        elif escolha == "2":
            cadastrar_prato()

        elif escolha == "3":
            listar_pratos()

        elif escolha == "4":
            listar_clientes()

        elif escolha == "5":
            remover_prato()

        elif escolha == "6":
            cadastrar_pedido()
        elif escolha == "7":
            retirar_proximo_pedido()

        elif escolha == "q":
            i = False

menu_principal()