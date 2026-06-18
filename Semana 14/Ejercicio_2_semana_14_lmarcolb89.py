# 2. Cree una estructura de objetos que asemeje un Double Ended Queue.
#    1. Debe incluir los métodos de `push_left` y `push_right` (para agregar nodos al inicio y al final) y `pop_left` y `pop_right` (para quitar nodos al inicio y al final).
#    2. Debe incluir un método para hacer `print` de toda la estructura.
#   3. No se permite el uso de tipos de datos compuestos como `lists`, `dicts` o `tuples` ni módulos como `collections`.


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoubleEndedQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def push_left(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
    
    def push_right(self, value):
        new_node = Node(value)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    def pop_left(self):
        value = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None
        self.length -= 1
        return value
    
    def pop_right(self):
        value = self.tail.value
        self.tail = self.tail.prev
        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None
        self.length -= 1
        return value
    
    def print_queue(self):
        current = self.head
        elements = []
        while current is not None:
            elements.append(str(current.value))
            current = current.next
        print("[" + ", ".join(elements) + "]")
    
    def __len__(self):
        return self.length
    
    def is_empty(self):
        return self.length == 0



if __name__ == "__main__":
    dq = DoubleEndedQueue()
    
    dq.push_left(10)
    dq.push_right(20)
    dq.push_left(5)
    dq.push_right(30)
    
    print("Queue content:")
    dq.print_queue()  
    
    print("Pop left:", dq.pop_left())  
    print("Pop right:", dq.pop_right())  
    
    print("Queue after pops:")
    dq.print_queue()  
    
    print("Queue length:", len(dq))  
