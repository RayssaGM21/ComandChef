from .cliente import Cliente
class Pedido:
    contador_id = 0

    def __init__(self, cliente: Cliente, pratos: list):
        Pedido.contador_id += 1
        
        self.id = Pedido.contador_id
        self.cliente = cliente
        self.pratos = pratos
        self.valor_total = self.calcular_total()

    def calcular_total(self):
        return sum(p["preco"] for p in self.pratos)
    
    def to_dict(self):
        return {
            "id": self.id,
            "cliente": self.cliente.to_dict(),
            "pratos": self.pratos,
            "valor_total": self.valor_total
        }