class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def printLL(self):
        if self.head is None:
            print('list isi empty')
        else:
            node = self.head
            while node != None:
                print(node.data)
                node = node.next
    def insertAtBegin(self,data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def insetAtEnd(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            node = self.head
            while node.next != None:
                node = node.next
            node.next = newNode
         


linkedList = LinkedList()
linkedList.insertAtBegin(10)
linkedList.insertAtBegin(20)
linkedList.insetAtEnd(11)

linkedList.printLL()
