class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self,data):
        new = Node(data)
        if not self.head:
            self.head = new
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new

    
    def display(self):
        current = self.head
        while current:
            print(current.data, end=' => ')
            current = current.next
        print('None')

    @classmethod
    def form_list(cls, node_list):
        linked_list = cls()
        for item in node_list:
            linked_list.append(item)
        return linked_list