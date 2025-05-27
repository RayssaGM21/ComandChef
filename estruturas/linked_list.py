import json

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        if isinstance(self.data, dict) and 'nome' in self.data:
            return f"Node(ID:{self.data.get('id', 'N/A')}, Nome:'{self.data['nome']}')"
        return f"Node({self.data})"

    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        return self.data == other.data

class LinkedList:
    def __init__(self, initial_data: list = None):
        self.head = None
        self._size = 0
        self._next_id = 1 

        # add dados iniciais
        if initial_data:
            for item_data in initial_data:
                self.add_last(Node(item_data))
            self._recalcula_next_id()

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        node = self.head
        nodes_data = []
        while node is not None:
            nodes_data.append(repr(node))
            node = node.next
        nodes_data.append("None")
        return " -> ".join(nodes_data)

    def __len__(self):
        return self._size

    def add_last(self, node: Node):
        if not isinstance(node, Node):
            raise TypeError("O argumento deve ser uma instância de Node.")

        if self.head is None:
            self.head = node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = node
        self._size += 1

    def remove(self, node: Node):
        if not isinstance(node, Node):
            raise TypeError("O argumento deve ser uma instância de Node.")

        if self.head is None:
            return None 

        # Caso 1: O nó a ser removido é o head
        if self.head == node:
            removed_data = self.head.data
            self.head = self.head.next
            self._size -= 1
            return removed_data

        # Caso 2: O nó a ser removido está no meio ou no final
        current_node = self.head
        while current_node.next is not None:
            if current_node.next == node:
                removed_data = current_node.next.data
                current_node.next = current_node.next.next
                self._size -= 1
                return removed_data
            current_node = current_node.next

        return None
    
    def _recalcula_next_id(self):
        max_id = 0
        for node in self:
            if node.data and isinstance(node.data, dict) and 'id' in node.data:
                current_item_id = node.data['id']
                if current_item_id > max_id:
                    max_id = current_item_id
        self._next_id = max_id + 1

    def proximo_id(self) -> int:
        current_id = self._next_id
        self._next_id += 1

        return current_id

    def to_json(self, indent=2) -> str:
        data_list = []

        for node in self:
            if node and node.data:
                data_list.append(node.data)
        
        return json.dumps(data_list, indent=indent, ensure_ascii=False)