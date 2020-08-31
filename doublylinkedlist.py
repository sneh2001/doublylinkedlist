class Node:
    def __init(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyList:
    
    def __init__(self):
        self.head = None

    def _len_(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def addNode(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next:
                cur = cur.next
            new_node.prev = cur
            new_node.next = None
            

    def display(self):
        if self.size == 0:
            print("No element")
            return
        first = self.head
        print(first.element)
        first = first.next
        while first:
            print(first.element)
            first = first.next
            
dlist = DoublyList()
dlist.addNode(1)
dlist.addNode(2)
dlist.addNode(3)
dlist.addNode(4)

dlist.print_list()






















