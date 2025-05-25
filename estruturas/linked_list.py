class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

    def __eq__(self, other):
        if not isinstance(other, Node):
            return False

        return self.data == other.data


class LinkedList:
    def __init__(self, nodes: list = None):
        self.head = None

        if nodes:
            node = Node(data=nodes.pop(0))
            self.head = node

            for element in nodes:
                node.next = Node(data=element)
                node = node.next

    def __iter__(self):
        node = self.head

        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        node = self.head
        nodes = []

        while node is not None:
            nodes.append(node.data)
            node = node.next

        nodes.append("None")

        return " -> ".join(nodes)

    def add_first(self, node: Node):
        node.next = self.head
        self.head = node

    def add_last(self, node: Node):
        if self.head is None:
            self.head = node
            return

        for current_node in self:
            pass
        current_node.next = node

    def add_after(self, node: Node, new_node: Node):
        if self.head is None:
            raise Exception("A lista está vazia.")

        if node is None:
            return

        for current_node in self:
            if current_node == node:
                new_node.next = current_node.next
                current_node.next = new_node
                return

        raise Exception(f"O nó {node} não foi encontrado na lista.")

    def add_before(self, node: Node, new_node: Node):
        if self.head is None:
            raise Exception("A lista está vazia.")

        if node is None:
            return

        if self.head == node:
            return self.add_first(new_node)

        for current_node in self:
            if current_node.next == node:
                new_node.next = current_node.next
                current_node.next = new_node
                return

        raise Exception(f"O nó {node} não foi encontrado na lista.")

    def remove(self, node: Node):
        if self.head is None:
            raise Exception("A lista está vazia.")

        if self.head == node:
            self.head = self.head.next
            return

        for current_node in self:
            if current_node.next == node:
                current_node.next = current_node.next.next
                return

        raise Exception(f"O nó {node} não foi encontrado na lista.")
