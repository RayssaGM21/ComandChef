class Cliente:
    contador_id = 0

    def __init__(self, nome: str):
        Cliente.contador_id += 1
        self.id = Cliente.contador_id
        self.nome = nome
        self.pedidos = []
        
    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
        }