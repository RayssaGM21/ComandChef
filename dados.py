from collections import deque
from estruturas.linked_list import LinkedList

clientes = [
    {"id": 1, "nome": "Matheus", "pedidos": []},
    {"id": 2, "nome": "Rayssa", "pedidos": []},
    {"id": 3, "nome": "Rodrigo", "pedidos": []}
]

pratos = [
    {
        "id": 1,
        "nome": "Espaguete ao Alho e Óleo",
        "preco": 22.50,
        "ingredientes": ("macarrão", "alho", "azeite", "salsinha")
    },
    {
        "id": 2,
        "nome": "Frango Xadrez",
        "preco": 29.90,
        "ingredientes": ("frango", "pimentão", "cebola", "molho shoyu", "amendoim")
    },
    {
        "id": 3,
        "nome": "Pizza Margherita",
        "preco": 34.00,
        "ingredientes": ("massa", "molho de tomate", "muçarela", "manjericão")
    },
    {
        "id": 4,
        "nome": "Risoto de Cogumelos",
        "preco": 100.80,
        "ingredientes": ("arroz arbório", "champignon", "parmesão", "cebola", "creme de leite")
    },
    {
        "id": 19,
        "nome": "Hambúrguer Artesanal",
        "preco": 27.50,
        "ingredientes": ("pão brioche", "carne angus", "queijo cheddar", "alface", "tomate", "maionese caseira")
    }
]

fila_pedidos = deque()

pratos_em_promocao = LinkedList([
    {"id": 101, "nome": "Combo Hambúrguer + Batata + Refri", "preco_promocional": 30.00, "original_id": 19},
    {"id": 102, "nome": "Pizza Margherita G - 20% OFF", "preco_promocional": 27.20, "original_id": 3},
])
