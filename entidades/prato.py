class Prato:
    contador_id = 0
    def __init__(self, nome: str, preco: float, ingredientes: tuple):

        Prato.contador_id += 1
        self.id = Prato.contador_id
        self.nome = nome
        self.preco = preco
        self.ingredientes = ingredientes