# 1. Cree una estructura de objetos que asemeje un Stack.
#    1. Debe incluir los métodos de `push` (para agregar nodos) y `pop` (para quitar nodos).
#    2. Debe incluir un método para hacer `print` de toda la estructura.
#    3. No se permite el uso de tipos de datos compuestos como `lists`, `dicts` o `tuples` ni módulos como `collections`.


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
    
    def push(self, value):
        new_node = Node(value)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.size += 1
    
    def pop(self):
        popped_node = self.top
        self.top = self.top.next
        self.size -= 1
        return popped_node.value
    
    def print_stack(self):
        current = self.top
        print("Top -> ", end="")
        while current is not None:
            print(current.value, end=" -> ")
            current = current.next
        print("Bottom")
    

if __name__ == "__main__":
    stack = Stack()
    
    stack.push(100)
    stack.push(200)
    stack.push(300)
    
    print("Stack values:")
    stack.print_stack()  

    print("Removed:", stack.pop())    
    
    print("Stack after removals:")
    stack.print_stack() 
    
    print("Removed:", stack.pop())  

