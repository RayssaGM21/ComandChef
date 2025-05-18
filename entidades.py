class Cliente:
    contador_id = 0

    def __init__(self, nome: str):
        Cliente.contador_id += 1
        self.id = Cliente.contador_id
        self.nome = nome
        self.pedidos = []


class Pedido:
    contador_id = 0

    def __init__(self, cliente: Cliente, pratos: list):
        Pedido.contador_id += 1
        
        self.id = Pedido.contador_id
        self.cliente = cliente
        self.pratos = pratos

class Prato:
    contador_id = 0
    def __init__(self, nome: str, preco: float, ingredientes: tuple):

        Prato.contador_id += 1
        self.id = Prato.contador_id
        self.nome = nome
        self.preco = preco
        self.ingredientes = ingredientes