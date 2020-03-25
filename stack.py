class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

    def __repr__(self):
        return repr(self.data)

#add to the head
class Linked_list:
    def __init__(self):
        self.head = None

    def __repr__(self):
        nodes = []
        curr= self.head
        while curr:
            nodes.append(repr(curr))
            curr= curr.next
        return str(nodes)

#add to the head
    def add_head(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def remove_head(self):
        new_node = self.head
        self.head= self.head.next
        return new_node.data

class Stack:
    def __init__(self):
        self.mylist=Linked_list()

    def push(self,data):
        self.mylist.add_head(data)

    def pop(self):
        return self.mylist.remove_head()


