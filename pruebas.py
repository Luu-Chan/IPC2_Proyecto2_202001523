import graphviz

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

# Crear dos listas enlazadas
list1 = LinkedList()
list1.add_node(1)
list1.add_node(2)
list1.add_node(3)

list2 = LinkedList()
list2.add_node('A')
list2.add_node('B')
list2.add_node('C')

# Crear un gráfico DOT
dot = graphviz.Digraph(comment='Listas Enlazadas')

# Agregar nodos y conexiones al gráfico para la Lista 1
current = list1.head
while current:
    dot.node(str(current.data))
    if current.next:
        dot.edge(str(current.data), str(current.next.data))
    current = current.next

# Agregar nodos y conexiones al gráfico para la Lista 2
current = list2.head
while current:
    dot.node(str(current.data))
    if current.next:
        dot.edge(str(current.data), str(current.next.data))
    current = current.next

# Generar el archivo de imagen (por ejemplo, en formato PNG)
dot.render('listas_enlazadas', format='png')
